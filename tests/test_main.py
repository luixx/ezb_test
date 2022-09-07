from ezb_api import get_exchange_rate, get_response_from_ezb, validate_curr, convert_to_float_value, check_identifier, \
    check_request_response, get_pdf_from_ezb_xml, isXml, validate_curr_requirements, get_raw_data, \
    extract_currency_from_identifier, validate_dataframes_for_multiplication
from ezb_api_exceptions import RemoteCommunicationException
import pandas as pd
import pytest as pytest
from math import isclose, isnan
from unittest import mock
from tests.xml_fixtures import XML_EXAMPLE

_DF_COLS = ['TIME_PERIOD', 'OBS_VALUE']
_RESPONSE_TEST_CASE = {
        "successful_case": {
            "content": XML_EXAMPLE,
            "status_code": 200,
        },
        "failed_case": {
            "content": "not_available",
            "status_code": 400,
        },
}
# TODO write setup and tearDown for patch
# def setUp(self):
#     self.patcher = mock.patch('ezb_api.requests.get', return_value=MockResponse(content=XML_EXAMPLE, status_code=200))
#     self.patcher.start()


class MockResponse:
    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code


def test_validate_curr__return_value():
    assert validate_curr('GBP') == True
    assert validate_curr(True) == False
    assert validate_curr(42) == False


def test_convert_to_float_type_error():
    with pytest.raises(TypeError):
        convert_to_float_value('GBP')
    with pytest.raises(TypeError):
        convert_to_float_value(True)


def test_convert_to_float_value_return_value():
    assert isclose(convert_to_float_value(42), 42.0)
    assert isclose(convert_to_float_value(42.42),42.42)
    assert isnan(convert_to_float_value("NaN"))
    assert isnan(convert_to_float_value(""))


def test_get_exchange_rate_source_value_error():
    with pytest.raises(ValueError):
        get_exchange_rate('not_available')


def test_get_exchange_rate_source_return_value():
    assert isinstance(get_exchange_rate('GBP'), pd.core.frame.DataFrame) == True
    assert isinstance(get_exchange_rate('GBP', 'EUR'), pd.core.frame.DataFrame) == True


def test_get_data_from_ezb_RemoteCommunicationException():
    with pytest.raises(RemoteCommunicationException):
        get_response_from_ezb('https://sdw-wsrest.ecb.europa.ef/service/data/EXR')


def test_check_identifier_return_value():
    assert check_identifier("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N") == True
    assert check_identifier(42) == False
    assert check_identifier("not_available") == False
    assert check_identifier(True) == False


def test_get_response_from_ezb_return_value():
    with mock.patch('ezb_api.requests.get', return_value=MockResponse(content=XML_EXAMPLE, status_code=200)):
        response = get_response_from_ezb(
            "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.GBP.EUR.SP00.A?detail=dataonly")
        assert response.status_code == 200


def test_get_response_from_ezb_value_error():
    with pytest.raises(ValueError):
        get_response_from_ezb(url='https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.{}.{}.SP00.A?detail=dataonly')


def test_check_request_response() -> None:
    with mock.patch('ezb_api.requests.get', return_value=MockResponse(content=XML_EXAMPLE, status_code=200)):
        response = get_response_from_ezb(
            "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.GBP.EUR.SP00.A?detail=dataonly")
        check_request = check_request_response(response)
        assert check_request == True
    with mock.patch('ezb_api.requests.get', return_value=MockResponse(content='not_available', status_code=400)):
        response = get_response_from_ezb(
            "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.EUR.EUR.SP00.A?detail=dataonly")
        check_request = check_request_response(response)
        assert check_request == False


def test_isXml_return_value():
    assert isXml(XML_EXAMPLE) == True
    assert isXml('not_available') == False


def test_get_pdf_from_ezb_xml_return_value():
    with mock.patch('ezb_api.requests.get',
                    return_value=MockResponse(content=_RESPONSE_TEST_CASE["successful_case"]["content"],
                                              status_code=_RESPONSE_TEST_CASE["successful_case"]["status_code"])):
        response = get_response_from_ezb(
            "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.EUR.EUR.SP00.A?detail=dataonly")
        curr_exchange_rate_pdf = get_pdf_from_ezb_xml(response)
        assert isinstance(curr_exchange_rate_pdf, pd.DataFrame) == True
        assert curr_exchange_rate_pdf.empty == False
        assert curr_exchange_rate_pdf.columns.tolist() == _DF_COLS
        assert curr_exchange_rate_pdf[_DF_COLS[1]].dtypes == float


def test_get_pdf_from_ezb_xml_value_error():
    with pytest.raises(ValueError):
        with mock.patch('ezb_api.requests.get',
                        return_value=MockResponse(content=_RESPONSE_TEST_CASE["failed_case"]["content"],
                                                  status_code=_RESPONSE_TEST_CASE["failed_case"]["status_code"])):
            response = get_response_from_ezb(
                "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.EUR.EUR.SP00.A?detail=dataonly")
            curr_exchange_rate_pdf = get_pdf_from_ezb_xml(response)


def test_validate_curr_requirements_return_value():
    assert validate_curr_requirements(source="not_available", target="EUR") == False
    assert validate_curr_requirements(source="GBP", target="USD") == False
    assert validate_curr_requirements(source="EUR", target="EUR") == False
    assert validate_curr_requirements(source="GBP", target="EUR") == True


def test_get_exchange_rate_return_value():
    #Return value testing is covered by test_get_pdf_from_ezb_xml_return_value
    pass


def test_get_exchange_rate_value_error():
    with pytest.raises(ValueError):
        with mock.patch('ezb_api.requests.get',
                        return_value=MockResponse(content=_RESPONSE_TEST_CASE["successful_case"]["content"],
                                                  status_code=_RESPONSE_TEST_CASE["successful_case"]["status_code"])):
            get_exchange_rate(source="GBP", target="USD")

    with pytest.raises(ValueError):
        with mock.patch('ezb_api.requests.get',
                        return_value=MockResponse(content=_RESPONSE_TEST_CASE["failed_case"]["content"],
                                                  status_code=_RESPONSE_TEST_CASE["failed_case"]["status_code"])):
            get_exchange_rate(source="GBP", target="EUR")


def test_get_raw_data_value_error():
    with pytest.raises(ValueError):
        get_raw_data("not_available")


def test_extract_currency_from_identifier_return_value():
    assert extract_currency_from_identifier("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N") == "EUR"


def test_extract_currency_from_identifier_value_error():
    with pytest.raises(ValueError):
        extract_currency_from_identifier("not_available")


def test_validate_dataframes_for_multiplication_return_value():
    example_currency_data_one = {
        _DF_COLS[0]: ['1999-01', '1999-02', '1999-03'],
        _DF_COLS[1]: [0.8, 0.72, -0.2]
    }
    example_currency_data_two = {
        _DF_COLS[0]: ['1999-01', '1999-02', '1999-03'],
        _DF_COLS[1]: ['1999-01', '1999-02', '1999-03']
    }
    example_currency_data_three = {
        "not_available": ['1999-01', '1999-02', '1999-03'],
        "not_available_2": [0.8, 0.72, 0.2]
    }
    example_currency_data_four = {
        _DF_COLS[0]: ['1999-01', '1999-02', '1999-03', '1999-04'],
        _DF_COLS[1]: [0.8, 0.72, 0.2, 0.9]
    }
    test_df_one = pd.DataFrame(example_currency_data_one)
    test_df_two = pd.DataFrame(example_currency_data_two)
    test_df_three = pd.DataFrame(example_currency_data_three)
    test_df_four = pd.DataFrame(example_currency_data_four)
    assert validate_dataframes_for_multiplication(df_left= test_df_one, df_right="not_available", calc_col_name= _DF_COLS[1]) == False
    assert validate_dataframes_for_multiplication(df_left=test_df_one, df_right=pd.DataFrame, calc_col_name=_DF_COLS[1]) == False
    assert validate_dataframes_for_multiplication(df_left=test_df_one, df_right=test_df_three, calc_col_name=_DF_COLS[1]) == False
    assert validate_dataframes_for_multiplication(df_left=test_df_one, df_right=test_df_two, calc_col_name=_DF_COLS[1]) == False
    assert validate_dataframes_for_multiplication(df_left= test_df_one, df_right= test_df_one, calc_col_name= _DF_COLS[1]) == True


def test_convert_to_target_currency_return_value():
    pass

def test_get_data_return_value():
    pass