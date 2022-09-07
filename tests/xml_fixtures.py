"""XML fixtures."""

XML_EXAMPLE = """<?xml version="1.0" encoding="UTF-8"?><message:GenericData xmlns:message="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message" xmlns:common="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:generic="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic" xsi:schemaLocation="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message https://sdw-wsrest.ecb.europa.eu:443/vocabulary/sdmx/2_1/SDMXMessage.xsd http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common https://sdw-wsrest.ecb.europa.eu:443/vocabulary/sdmx/2_1/SDMXCommon.xsd http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic https://sdw-wsrest.ecb.europa.eu:443/vocabulary/sdmx/2_1/SDMXDataGeneric.xsd">
<message:Header>
<message:ID>7cfed662-11e7-435d-bd58-9320bf518a1a</message:ID>
<message:Test>false</message:Test>
<message:Prepared>2022-08-23T14:58:25.491+02:00</message:Prepared>
<message:Sender id="ECB"/>
<message:Structure structureID="BOP" dimensionAtObservation="TIME_PERIOD">
<common:Structure>
<URN>urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=IMF:BOP(1.5)</URN>
</common:Structure>
</message:Structure>
</message:Header>
<message:DataSet action="Replace" validFromDate="2022-08-23T14:58:25.491+02:00" structureRef="BOP">
<generic:Series>
<generic:SeriesKey>
<generic:Value id="FREQ" value="M"/>
<generic:Value id="ADJUSTMENT" value="N"/>
<generic:Value id="REF_AREA" value="I8"/>
<generic:Value id="COUNTERPART_AREA" value="W1"/>
<generic:Value id="REF_SECTOR" value="S1"/>
<generic:Value id="COUNTERPART_SECTOR" value="S1"/>
<generic:Value id="FLOW_STOCK_ENTRY" value="T"/>
<generic:Value id="ACCOUNTING_ENTRY" value="N"/>
<generic:Value id="INT_ACC_ITEM" value="FA"/>
<generic:Value id="FUNCTIONAL_CAT" value="F"/>
<generic:Value id="INSTR_ASSET" value="F7"/>
<generic:Value id="MATURITY" value="T"/>
<generic:Value id="UNIT_MEASURE" value="EUR"/>
<generic:Value id="CURRENCY_DENOM" value="_T"/>
<generic:Value id="VALUATION" value="T"/>
<generic:Value id="COMP_METHOD" value="N"/>
</generic:SeriesKey>
<generic:Attributes>
<generic:Value id="DECIMALS" value="0"/>
<generic:Value id="TITLE" value="Financial Derivatives and Employee Stock Options, Financial derivatives and employee stock options"/>
<generic:Value id="UNIT_MULT" value="6"/>
<generic:Value id="COMMENT_TS" value="- Monthly- Neither seasonally adjusted nor calendar adjusted data- Euro area 19 (fixed composition) as of 1 January 2015 vis-a-vis Rest of the World- sector: Total economy vis-a-vis Total economy- Transactions- Net (Assets minus Liabilities)- Financial account- Financial Derivatives and Employee Stock Options- Financial derivatives and employee stock options- All original maturities- Euro- All currencies- Net marked to market value- Compilation methodology based on international standards"/>
<generic:Value id="COMPILING_ORG" value="4F0"/>
<generic:Value id="TIME_FORMAT" value="P1M"/>
<generic:Value id="TIME_PER_COLLECT" value="S"/>
</generic:Attributes>
<generic:Obs>
<generic:ObsDimension value="1999-01"/>
<generic:ObsValue value="1427.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-02"/>
<generic:ObsValue value="379.666666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-03"/>
<generic:ObsValue value="-1597.33333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-04"/>
<generic:ObsValue value="-3788.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-05"/>
<generic:ObsValue value="1690.33333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-06"/>
<generic:ObsValue value="614.333333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-07"/>
<generic:ObsValue value="-1805.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-08"/>
<generic:ObsValue value="-2664.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-09"/>
<generic:ObsValue value="-1423.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-10"/>
<generic:ObsValue value="2729"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-11"/>
<generic:ObsValue value="-1347"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="1999-12"/>
<generic:ObsValue value="2077"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-01"/>
<generic:ObsValue value="348.333333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-02"/>
<generic:ObsValue value="-1784.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-03"/>
<generic:ObsValue value="623.333333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-04"/>
<generic:ObsValue value="-2490.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-05"/>
<generic:ObsValue value="-76.6666666666666"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-06"/>
<generic:ObsValue value="-1338.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-07"/>
<generic:ObsValue value="3316.33333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-08"/>
<generic:ObsValue value="974.333333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-09"/>
<generic:ObsValue value="739.333333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-10"/>
<generic:ObsValue value="1904.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-11"/>
<generic:ObsValue value="3595.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2000-12"/>
<generic:ObsValue value="4343.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-01"/>
<generic:ObsValue value="2335"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-02"/>
<generic:ObsValue value="-509"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-03"/>
<generic:ObsValue value="-3489"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-04"/>
<generic:ObsValue value="-8383.33333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-05"/>
<generic:ObsValue value="-5883.33333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-06"/>
<generic:ObsValue value="2198.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-07"/>
<generic:ObsValue value="5887.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-08"/>
<generic:ObsValue value="2851.66666666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-09"/>
<generic:ObsValue value="87.6666666666674"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-10"/>
<generic:ObsValue value="2139.33333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-11"/>
<generic:ObsValue value="2644.33333333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2001-12"/>
<generic:ObsValue value="856.333333333334"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-01"/>
<generic:ObsValue value="-2707.813752"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-02"/>
<generic:ObsValue value="-2958.261728"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-03"/>
<generic:ObsValue value="1423.097028"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-04"/>
<generic:ObsValue value="-1348.894885"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-05"/>
<generic:ObsValue value="2435.548688"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-06"/>
<generic:ObsValue value="2110.818825"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-07"/>
<generic:ObsValue value="8533.68956766667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-08"/>
<generic:ObsValue value="2617.57702066667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-09"/>
<generic:ObsValue value="-604.272640333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-10"/>
<generic:ObsValue value="-522.604052"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-11"/>
<generic:ObsValue value="707.097126"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2002-12"/>
<generic:ObsValue value="2625.898142"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-01"/>
<generic:ObsValue value="2188.35608533333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-02"/>
<generic:ObsValue value="528.506035333334"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-03"/>
<generic:ObsValue value="657.479042333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-04"/>
<generic:ObsValue value="3398.953767"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-05"/>
<generic:ObsValue value="-1461.733065"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-06"/>
<generic:ObsValue value="784.967256"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-07"/>
<generic:ObsValue value="2237.85661833333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-08"/>
<generic:ObsValue value="2275.08897433333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-09"/>
<generic:ObsValue value="-830.448354666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-10"/>
<generic:ObsValue value="-1559.132904"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-11"/>
<generic:ObsValue value="-859.025733"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2003-12"/>
<generic:ObsValue value="6388.001162"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-01"/>
<generic:ObsValue value="-356.121786666666"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-02"/>
<generic:ObsValue value="-456.569938666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-03"/>
<generic:ObsValue value="-3341.06246366667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-04"/>
<generic:ObsValue value="3807.276844"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-05"/>
<generic:ObsValue value="4323.839545"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-06"/>
<generic:ObsValue value="-329.881882"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-07"/>
<generic:ObsValue value="-2557.27751505973"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-08"/>
<generic:ObsValue value="3544.59448611945"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-09"/>
<generic:ObsValue value="-2956.12868505973"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-10"/>
<generic:ObsValue value="5507.21409233333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-11"/>
<generic:ObsValue value="-550.682038666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2004-12"/>
<generic:ObsValue value="1852.38441033333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-01"/>
<generic:ObsValue value="4486.674259"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-02"/>
<generic:ObsValue value="26.1184800000003"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-03"/>
<generic:ObsValue value="3899.631078"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-04"/>
<generic:ObsValue value="233.183858006483"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-05"/>
<generic:ObsValue value="1414.13829600648"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-06"/>
<generic:ObsValue value="-998.836344993517"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-07"/>
<generic:ObsValue value="-2309.31634133333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-08"/>
<generic:ObsValue value="533.193181666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-09"/>
<generic:ObsValue value="1126.10015566667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-10"/>
<generic:ObsValue value="3825.34828727195"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-11"/>
<generic:ObsValue value="1577.65844627195"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2005-12"/>
<generic:ObsValue value="3595.45225427195"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-01"/>
<generic:ObsValue value="2986.304902"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-02"/>
<generic:ObsValue value="2492.997552"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-03"/>
<generic:ObsValue value="2984.63238"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-04"/>
<generic:ObsValue value="8043.74470566667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-05"/>
<generic:ObsValue value="370.914912666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-06"/>
<generic:ObsValue value="-4296.25125433333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-07"/>
<generic:ObsValue value="-3813.93423966667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-08"/>
<generic:ObsValue value="1937.87750833333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-09"/>
<generic:ObsValue value="-12607.9909326667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-10"/>
<generic:ObsValue value="-5604.406806"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-11"/>
<generic:ObsValue value="3804.433792"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2006-12"/>
<generic:ObsValue value="4260.840971"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-01"/>
<generic:ObsValue value="4165.235722"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-02"/>
<generic:ObsValue value="4615.703663"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-03"/>
<generic:ObsValue value="4108.42025"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-04"/>
<generic:ObsValue value="1997.491899"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-05"/>
<generic:ObsValue value="265.829707"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-06"/>
<generic:ObsValue value="6786.510263"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-07"/>
<generic:ObsValue value="10908.5308756667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-08"/>
<generic:ObsValue value="6651.94640466667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-09"/>
<generic:ObsValue value="5043.25726166667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-10"/>
<generic:ObsValue value="2777.445147"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-11"/>
<generic:ObsValue value="12572.140468"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2007-12"/>
<generic:ObsValue value="6880.161197"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="E"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-01"/>
<generic:ObsValue value="-4080.1424866666657"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-02"/>
<generic:ObsValue value="-10445.504970666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-03"/>
<generic:ObsValue value="-2165.254940666665"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-04"/>
<generic:ObsValue value="9151.356552433179"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-05"/>
<generic:ObsValue value="12886.852688764975"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-06"/>
<generic:ObsValue value="10835.966406801841"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-07"/>
<generic:ObsValue value="-3046.300913"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-08"/>
<generic:ObsValue value="6192.721807000001"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-09"/>
<generic:ObsValue value="-4278.341922999999"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-10"/>
<generic:ObsValue value="14077.746409009826"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-11"/>
<generic:ObsValue value="22857.386118104798"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2008-12"/>
<generic:ObsValue value="-2685.3412513513467"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-01"/>
<generic:ObsValue value="-2492.395234740918"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-02"/>
<generic:ObsValue value="-1050.6358617669573"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-03"/>
<generic:ObsValue value="-4418.231702438384"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-04"/>
<generic:ObsValue value="-9669.537429896878"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-05"/>
<generic:ObsValue value="-10663.857258016262"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-06"/>
<generic:ObsValue value="-2979.5076342582647"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-07"/>
<generic:ObsValue value="-553.9631146304598"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-08"/>
<generic:ObsValue value="10378.977842853763"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-09"/>
<generic:ObsValue value="2955.619660718496"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-10"/>
<generic:ObsValue value="4743.689762934324"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-11"/>
<generic:ObsValue value="3119.7071416603017"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2009-12"/>
<generic:ObsValue value="2999.932096313"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-01"/>
<generic:ObsValue value="123.09233654505357"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-02"/>
<generic:ObsValue value="-2347.210105933386"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-03"/>
<generic:ObsValue value="5711.065419466693"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-04"/>
<generic:ObsValue value="6611.837455552102"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-05"/>
<generic:ObsValue value="5449.087013047964"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-06"/>
<generic:ObsValue value="4101.377036399933"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-07"/>
<generic:ObsValue value="2078.9976682739684"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-08"/>
<generic:ObsValue value="-151.7722807651079"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-09"/>
<generic:ObsValue value="-4618.924168508861"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-10"/>
<generic:ObsValue value="-7928.055884882679"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-11"/>
<generic:ObsValue value="-596.6783129257456"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2010-12"/>
<generic:ObsValue value="-11717.515660191575"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-01"/>
<generic:ObsValue value="-2645.419261662325"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-02"/>
<generic:ObsValue value="-1158.3888526688377"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-03"/>
<generic:ObsValue value="2103.910100331162"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-04"/>
<generic:ObsValue value="-9549.859085040665"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-05"/>
<generic:ObsValue value="-2144.0792563357663"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-06"/>
<generic:ObsValue value="-3832.615528623567"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-07"/>
<generic:ObsValue value="250.0281231568534"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-08"/>
<generic:ObsValue value="5618.128162421574"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-09"/>
<generic:ObsValue value="5221.534383421575"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-10"/>
<generic:ObsValue value="8857.378882311583"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-11"/>
<generic:ObsValue value="892.6246453395484"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2011-12"/>
<generic:ObsValue value="159.60466488439528"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-01"/>
<generic:ObsValue value="5805.996264851306"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-02"/>
<generic:ObsValue value="-2755.5258000636877"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-03"/>
<generic:ObsValue value="5121.672226329747"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-04"/>
<generic:ObsValue value="-630.1599430599874"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-05"/>
<generic:ObsValue value="11129.353821226709"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-06"/>
<generic:ObsValue value="3961.8415898373237"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-07"/>
<generic:ObsValue value="7954.653559420926"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-08"/>
<generic:ObsValue value="-1547.5856516315228"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-09"/>
<generic:ObsValue value="5650.014054593936"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-10"/>
<generic:ObsValue value="-754.4511812296684"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-11"/>
<generic:ObsValue value="-5260.832401754772"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2012-12"/>
<generic:ObsValue value="1481.3749400511617"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="P"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-01"/>
<generic:ObsValue value="-980.8062996038254"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-02"/>
<generic:ObsValue value="2680.0201754337386"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-03"/>
<generic:ObsValue value="3729.066885888836"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-04"/>
<generic:ObsValue value="-3441.975196391221"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-05"/>
<generic:ObsValue value="6482.895489102567"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-06"/>
<generic:ObsValue value="-2748.9398239613465"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-07"/>
<generic:ObsValue value="3940.0301235924935"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-08"/>
<generic:ObsValue value="-4191.569426722475"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-09"/>
<generic:ObsValue value="4630.760494536233"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-10"/>
<generic:ObsValue value="-2031.4033698138935"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-11"/>
<generic:ObsValue value="-2340.382176735781"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2013-12"/>
<generic:ObsValue value="-4214.1744143878295"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-01"/>
<generic:ObsValue value="408.5263281229808"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-02"/>
<generic:ObsValue value="3062.583731368036"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-03"/>
<generic:ObsValue value="-7819.838575116019"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-04"/>
<generic:ObsValue value="2558.1541846340165"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-05"/>
<generic:ObsValue value="5342.007014937456"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-06"/>
<generic:ObsValue value="2368.227472303528"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-07"/>
<generic:ObsValue value="5138.310110774258"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-08"/>
<generic:ObsValue value="8506.995188832061"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-09"/>
<generic:ObsValue value="1958.1673566436834"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-10"/>
<generic:ObsValue value="6063.437156354167"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-11"/>
<generic:ObsValue value="4790.9446473541675"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2014-12"/>
<generic:ObsValue value="5044.376985354167"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-01"/>
<generic:ObsValue value="8631.198563416669"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-02"/>
<generic:ObsValue value="27026.993976416667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-03"/>
<generic:ObsValue value="12394.123866416669"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-04"/>
<generic:ObsValue value="4504.268549410156"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-05"/>
<generic:ObsValue value="423.57962341015593"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-06"/>
<generic:ObsValue value="-4363.705411589844"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-07"/>
<generic:ObsValue value="11572.726690083335"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-08"/>
<generic:ObsValue value="-3416.456811916668"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-09"/>
<generic:ObsValue value="-3380.8909719166672"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-10"/>
<generic:ObsValue value="16779.117089916665"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-11"/>
<generic:ObsValue value="24428.955805916667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2015-12"/>
<generic:ObsValue value="19401.095072916665"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-01"/>
<generic:ObsValue value="12086.985348166667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-02"/>
<generic:ObsValue value="15165.700474166666"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-03"/>
<generic:ObsValue value="2703.696990166667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-04"/>
<generic:ObsValue value="-22449.598232583336"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-05"/>
<generic:ObsValue value="-16882.81007558333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-06"/>
<generic:ObsValue value="-8828.61903558333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-07"/>
<generic:ObsValue value="9840.3430535"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-08"/>
<generic:ObsValue value="7285.286154499997"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-09"/>
<generic:ObsValue value="4983.3317295"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-10"/>
<generic:ObsValue value="7860.575871010417"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-11"/>
<generic:ObsValue value="-1687.8565629895838"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2016-12"/>
<generic:ObsValue value="53.12102401041636"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-01"/>
<generic:ObsValue value="-3556.8692650000007"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-02"/>
<generic:ObsValue value="15095.321777"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-03"/>
<generic:ObsValue value="10099.297488"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-04"/>
<generic:ObsValue value="2621.0959923749997"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-05"/>
<generic:ObsValue value="-400.2438096249998"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-06"/>
<generic:ObsValue value="-10654.600229625"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-07"/>
<generic:ObsValue value="-1771.9353963333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-08"/>
<generic:ObsValue value="-4979.873077333332"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-09"/>
<generic:ObsValue value="550.7772236666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-10"/>
<generic:ObsValue value="475.1681413749996"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-11"/>
<generic:ObsValue value="1447.3732203749998"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2017-12"/>
<generic:ObsValue value="2465.960591375"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-01"/>
<generic:ObsValue value="-6950.021118083332"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-02"/>
<generic:ObsValue value="-4987.290144083332"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-03"/>
<generic:ObsValue value="-3996.3801440833317"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-04"/>
<generic:ObsValue value="7203.092260291666"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-05"/>
<generic:ObsValue value="7998.037728291666"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-06"/>
<generic:ObsValue value="2231.4774332916677"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-07"/>
<generic:ObsValue value="9836.25213733333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-08"/>
<generic:ObsValue value="10374.280826333335"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-09"/>
<generic:ObsValue value="3714.4045363333316"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-10"/>
<generic:ObsValue value="8252.43139825"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-11"/>
<generic:ObsValue value="10894.296347250001"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2018-12"/>
<generic:ObsValue value="-5043.075401749998"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-01"/>
<generic:ObsValue value="-153.75998877083293"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-02"/>
<generic:ObsValue value="-9137.602729770832"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-03"/>
<generic:ObsValue value="-536.3999767708324"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-04"/>
<generic:ObsValue value="8862.051059833333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-05"/>
<generic:ObsValue value="4504.576229833333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-06"/>
<generic:ObsValue value="5802.583647833333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-07"/>
<generic:ObsValue value="9670.752047510417"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-08"/>
<generic:ObsValue value="-3576.8044184895844"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-09"/>
<generic:ObsValue value="-3152.583859489584"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-10"/>
<generic:ObsValue value="7250.706902302083"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-11"/>
<generic:ObsValue value="1262.0662913020842"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2019-12"/>
<generic:ObsValue value="-13123.325439697917"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-01"/>
<generic:ObsValue value="12334.27781904167"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-02"/>
<generic:ObsValue value="9789.699407041668"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-03"/>
<generic:ObsValue value="460.3059770416689"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-04"/>
<generic:ObsValue value="14454.841277333331"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-05"/>
<generic:ObsValue value="11883.350916333331"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-06"/>
<generic:ObsValue value="23519.901556333334"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-07"/>
<generic:ObsValue value="-6655.280712791667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-08"/>
<generic:ObsValue value="-15657.796320791664"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-09"/>
<generic:ObsValue value="-8492.710075791667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-10"/>
<generic:ObsValue value="5088.5592234375"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-11"/>
<generic:ObsValue value="11770.1090334375"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2020-12"/>
<generic:ObsValue value="-28792.0461865625"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-01"/>
<generic:ObsValue value="11070.439339979166"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-02"/>
<generic:ObsValue value="-1764.500843020834"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-03"/>
<generic:ObsValue value="-6045.916036020833"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-04"/>
<generic:ObsValue value="6968.979683317708"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-05"/>
<generic:ObsValue value="-6940.143235682292"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-06"/>
<generic:ObsValue value="-2297.8313206822922"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-07"/>
<generic:ObsValue value="18310.744325375"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-08"/>
<generic:ObsValue value="1635.4017423750004"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-09"/>
<generic:ObsValue value="4115.777760375"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-10"/>
<generic:ObsValue value="13982.7705245"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-11"/>
<generic:ObsValue value="26205.421808500003"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2021-12"/>
<generic:ObsValue value="4426.893604499999"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2022-01"/>
<generic:ObsValue value="2742.741796333333"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2022-02"/>
<generic:ObsValue value="-3776.5449166666667"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2022-03"/>
<generic:ObsValue value="-4280.259379666666"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2022-04"/>
<generic:ObsValue value="12755.701375999999"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2022-05"/>
<generic:ObsValue value="-2733.5890050000003"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
<generic:Obs>
<generic:ObsDimension value="2022-06"/>
<generic:ObsValue value="-9894.277891000002"/>
<generic:Attributes>
<generic:Value id="OBS_STATUS" value="A"/>
<generic:Value id="CONF_STATUS" value="F"/>
</generic:Attributes>
</generic:Obs>
</generic:Series>
</message:DataSet>
</message:GenericData>
"""