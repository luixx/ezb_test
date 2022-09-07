from ezb_api_exceptions import RemoteCommunicationException
import numpy as np
import requests
from xml.etree import ElementTree
import pandas as pd
import re
import validators
import argparse


ElementTree.register_namespace("ezb", "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic")
_XML_NS = {"ezb": "http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic"}
_EXCHANGE_RATE_URL = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.{}.{}.SP00.A?detail=dataonly"
_IDENTIFIER_URL = "https://sdw-wsrest.ecb.europa.eu/service/data/BP6/{}?detail=dataonly"
_STATUS_CODES_OK = 200
_REQUIRED_CURRENCY = "EUR"
_INDEX_SOURCE_CURRENCY_IDENTIFY = 12


def get_response_from_ezb(url: str) -> requests.Response:
    """Get request response from a given URL.

    Args:
        url (str): a url as string

    Returns:
        A requests.Response

    Raises:
        ValueError: An error occurred if given url not match requirements on the given url.
        RemoteCommunicationException: An error occurred if something went wrong to fetch data from the API.
    """
    url_validation_result = validators.url(url)
    if url_validation_result:
        try:
            response = requests.get(url=url)
        except Exception as e:
            raise RemoteCommunicationException(f'Exception getting data from EZB! url: {url}') from e
        return response
    else:
        raise ValueError(url_validation_result)


def validate_curr(currency: str) -> bool:
    """Validating if currency is acceptable for EZB API.

    Args:
        currency (str): currency that should be checked

    Returns:
        Boolean, if currency is acceptable.
    """

    supported_currs = ['USD', 'EUR', 'GBP', 'CAD']  # Note here supported currencies or a DB access could be implemented

    if currency in supported_currs:
        return True
    else:
        return False


def check_request_response(response: requests.Response) -> bool:
    """Check that response status is ok.

    Args:
        response (requests.Response): response that should be checked

    Returns:
        Boolean, if status is ok, true will be returned.
    """
    if response.status_code == _STATUS_CODES_OK:
        return True
    else:
        return False


def convert_to_float_value(string_float: str):
    """Check and convert a float value.

    Args:
        string_float (str): a string value that should be converted

    Returns:
        The converted float value or np.nan if the provided string is empty or contains nan.
    Raises:
        TypeError: An error occurred if the given value can not be converted to a float.
    """
    string_float = str(string_float).lower()
    if string_float and re.search("^(-|)[0-9.]*$", string_float):
        return float(string_float)
    else:
        if "nan" in string_float or not string_float:
            return np.nan
        else:
            raise TypeError(f"ERROR: The given string \"{string_float}\" can not be converted to float.")


def isXml(xml_value: str):
    """Validate if given string is a xml.

    Args:
        xml_value (str): A string that contains xml.

    Returns:
        A boolean, if it is a xml true will be returned, otherwise false
    """
    try:
        ElementTree.fromstring(xml_value)
        return True
    except ElementTree.ParseError:
        return False


def get_pdf_from_ezb_xml(response: requests.Response):
    """Creates a pandas dataframe from a given response.

    Args:
        response (requests.Response): a response containing xml data.

    Returns:
        Pandas dataframe containing the data retrieved from the response.
    Raises:
        ValueError: An error occurred if no values can be retrieved from the api.
        ValueError: An error occurred if in response no parsable xml content is contained.
    """
    if isXml(response.content):
        root = ElementTree.fromstring(response.content)
        data = []
        cols = ['TIME_PERIOD', 'OBS_VALUE']

        for obs_element in root.findall('.//ezb:Obs', _XML_NS):
            obs_dimension = obs_element[0].attrib['value']
            obs_value = obs_element[1].attrib['value']
            obs_value_float = convert_to_float_value(obs_value)
            data.append([obs_dimension, obs_value_float])
        if not data:
            raise ValueError(f"No values can be retrieved from API")
        else:
            ezb_data = pd.DataFrame(data=data, columns=cols)
            return ezb_data
    else:
        raise ValueError("In response content no XML parseable content contained.")


def validate_curr_requirements(source: str, target: str) -> bool:
    """Validate that currency requirements are satisfied.

    Args:
        source (str): source currency
        target (str): target currency

    Returns:
        A boolean, it is false if currency does not statisfy the requirements and true if it matches the requirements.
    """
    validation_result = False
    if validate_curr(source) and validate_curr(target):
        if target == _REQUIRED_CURRENCY:
            if target != source:
                return True
    return validation_result


def get_exchange_rate(source: str, target: str = "EUR") -> pd.DataFrame:
    """Get the exchange rate between a currency pair

    Sends API request to EZP, for requesting past exchange rate of a currency pair
    and returns pandas dataframe with the time period and exchange rate.

    Args:
        source (str): source currency
        target (str): target currency, Default to EUR

    Returns:
        pandas Dataframe with TIME_PERIOD and OBS_VALUE column

    Raises:
        ValueError: An error occurred if EZB API responds with other status code than 200
        ValueError: An error occurred if other currencies, string values, int values, bool values are parsed to the method
    """

    if validate_curr_requirements(source, target):
        currency_pair_exchange_rate_url = _EXCHANGE_RATE_URL.format(source, target)
        ezb_request = get_response_from_ezb(currency_pair_exchange_rate_url)
        if check_request_response(ezb_request):
            curr_exchange_rate_pdf = get_pdf_from_ezb_xml(ezb_request)
            return curr_exchange_rate_pdf
        else:
            raise ValueError(
                f"REST API retrieves for {currency_pair_exchange_rate_url} following code: {ezb_request.status_code}")

    else:
        raise ValueError("Currency does not match the requirements.")


def check_identifier(identifier: str):
    """Check validity of the identifier.

    Args:
        identifier (str): the identifier given as string

    Returns:
        A boolean, it is false if identifier does not statisfy the requirements and true if it matches the requirements.
    """
    validation_result = False
    identifier = str(identifier)
    if re.search("^[A-Z0-9.\_]*$", identifier):
        identifier_elements = identifier.split('.')
        if len(identifier_elements) > _INDEX_SOURCE_CURRENCY_IDENTIFY:
            if validate_curr(identifier_elements[_INDEX_SOURCE_CURRENCY_IDENTIFY]):
                return True
    return validation_result


def get_raw_data(identifier: str) -> pd.DataFrame:
    """Creates pandas dataframe from the retrieved data, based on the identifier.

    Args:
        identifier (str): the identifier given as string

    Returns:
        A pandas dataframe with retrieved data from the api.

    Raises:
        ValueError: An error occurred if identifier is not matching the requirements.
    """
    if check_identifier(identifier):
        identifier_url = _IDENTIFIER_URL.format(identifier)
        ezb_request = get_response_from_ezb(identifier_url)
        ezb_data_pdf = get_pdf_from_ezb_xml(ezb_request)
        return ezb_data_pdf
    else:
        raise ValueError("Identifier is not matching the requirements")


def extract_currency_from_identifier(identifier: str):
    """Extracts currency from the api.

    Args:
        identifier (str): the identifier given as string

    Returns:
        Return None if no currency exist in identifier, otherwise the currency will be returned.

    Raises:
        ValueError: An error occurred if identifier is not matching the requirements
    """
    currency = None
    if check_identifier(identifier):
        identifier = str(identifier)
        identifier_elements = identifier.split('.')
        currency = identifier_elements[_INDEX_SOURCE_CURRENCY_IDENTIFY]
    else:
        raise ValueError(f"Identifier does not met the requirements: {identifier}")
    return currency


def validate_dataframes_for_multiplication(df_left: pd.DataFrame, df_right: pd.DataFrame, calc_col_name: str = 'OBS_VALUE') -> pd.DataFrame:
    """Validates if multiplikation between two dataframes is possible.

    Args:
        df_left (pd.DataFrame): left pandas dataframe for multiplikation
        df_right (pd.DataFrame): right pandas dataframe for multiplikation
        calc_col_name (str): column which should be multiplied and exists in both dataframes

    Returns:
        A boolean, it is false if dataframes does not statisfy the requirements for multiplication and true if it matches the requirements.
    """
    validation_result = False
    if isinstance(df_left, pd.DataFrame) and isinstance(df_right, pd.DataFrame):
        if not df_left.empty and not df_right.empty:
            if calc_col_name in df_left.columns and calc_col_name in df_right.columns:
                if df_left[calc_col_name].dtypes in [int, float] and df_right[calc_col_name].dtypes in [int, float]:
                    validation_result = True
    return validation_result



def convert_to_target_currency(ezb_data: pd.DataFrame, curr_exchange_rate_pdf: pd.DataFrame) -> pd.DataFrame:
    """Converts numerical data to target currency.

    Args:
        ezb_data (pd.DataFrame): data that should be converted
        curr_exchange_rate_pdf (pd.DataFrame): exchange rate from target currency

    Returns:
        A pandas dataframe with data converted to target currency.

    Raises:
        ValueError: An error occurred if dataframes can not be used for calculation, due to validation error.
    """

    converted_ezb_data_pdf = ezb_data
    if validate_dataframes_for_multiplication(ezb_data, curr_exchange_rate_pdf):
        converted_ezb_data_pdf['OBS_VALUE'] = ezb_data['OBS_VALUE'] * curr_exchange_rate_pdf['OBS_VALUE']
        return converted_ezb_data_pdf
    else:
        raise ValueError("Dataframes can not be used for calculation, due to validation error.")


def get_data(identifier: str, target_currency: str = None) -> pd.DataFrame:
    """Provides raw data retrieved from api or convert it to target currency.

    Args:
        identifier (str): identifier given as string
        target_currency (str): target currency e.g. GBP

    Returns:
        A pandas dataframe, with 'TIME_PERIOD' and 'OBS_VALUE' as column, 'OBS_VALUE' is raw data retrieved from the api or raw data that is converted to target currency.
    Raises:
        An error occurred if for identifier no source currency could be found.
    """

    ezb_data_response_pdf = get_raw_data(identifier)
    if target_currency:
        source = extract_currency_from_identifier(identifier)
        if source:
            curr_exchange_rate_pdf = get_exchange_rate(target_currency, source)
            converted_ezb_data = convert_to_target_currency(ezb_data_response_pdf, curr_exchange_rate_pdf)
            return converted_ezb_data
        else:
            raise ValueError(f"For the identifier {identifier} no source currency could be found.")

    else:
        return get_raw_data(identifier)


def main():
    parser = argparse.ArgumentParser(description='ezb_api specifications')
    parser.add_argument('--source_curr', dest='source_curr', type=str, help='source currency', default="GBP")
    parser.add_argument('--target_curr', dest='target_curr', type=str, help='target currency', default="EUR")
    parser.add_argument('--identifier', dest='identifier', type=str, help='identifier', default="M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N")
    args = parser.parse_args()
    print("Result of get_exchange_rate:")
    print(get_exchange_rate(args.source_curr, args.target_curr).head())
    print("Result of get_raw_data:")
    print(get_raw_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N").head())
    print("Result of get_data:")
    print(get_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N", "GBP").head())


if __name__ == '__main__':
    main()
