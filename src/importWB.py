import requests
import pandas as pd
import faostat
from datetime import date
from myFunc import save_csv_with_incremental_number

# Set the root directory for saving data
root = 'Data/processed/'


def importWB_v2(indicatorId, indicatorName, countries, startYear, endYear, savetoCsv=False):
    # connect countries to string
    if isinstance(countries, list):
        country_str = ';'.join(countries)
    else:
        country_str = countries

    url = f"https://api.worldbank.org/v2/country/{country_str}/indicator/{indicatorId}"
    params = {
        'date': f"{startYear}:{endYear}",
        'format': 'json',
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Extract data part
    if len(data) > 1:
        records = data[1]
        df = pd.DataFrame(records)
        # Extract only necessary columns
        df = df[['country', 'date', 'value']]
        df['country'] = df['country'].apply(lambda x: x['id'])
        df = df.rename(columns={'date': 'Year', 'value': indicatorName})
        if savetoCsv:
            df.to_csv(
                f"{root}/temp/{indicatorName}_{startYear}_{endYear}.csv", index=False)
        return df
    else:
        print("No data found.")
        return pd.DataFrame()


# importFAO function
# this function imports data from FAO database using the faostat package and uses the parameters defined in setParams
    # # example parameters: FBSData  ####################################
    # FBSdata = {'db': 'FBS',
    #            'dbName': 'Food Balances (2010-)',
    #            'element': {'Food supply quantity (kg/capita/yr)': '645'},
    #            'item': {'Cereals - Excluding Beer + (Total)': '2905', 'Starchy Roots + (Total)': '2907'},
    #            'area':  {'-- Southern Asia > (List)': '5303>', '-- South-eastern Asia > (List)': '5304>'},
    #            'year': [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    #            }
    #######################################################################
def importFAO(myParam, pivot=False, savetoCsv=False):

    # Define parameters for importFAO: area, element, item, year using a dictionary
    def setParams(dbDictionary):
        db = dbDictionary['db']
        element_list = list(dbDictionary['element'].values())
        item_list = list(dbDictionary['item'].values())
        area_list = list(dbDictionary['area'].values())
        year_list = dbDictionary['year']
        result = {
            'db': db,
            'element': element_list,
            'item': item_list,
            'area': area_list,
            'year': year_list
        }
        return result

    # Set parameters for the FAO database
    params = setParams(myParam)

    # # Get the start and end year from the parameters
    # startYear = min(myParam['year'])
    # endYear = max(myParam['year'])

    # Download data as a pandas DataFrame
    df = faostat.get_data_df(params['db'], pars=params)

    if pivot == False:
        # if pivot = false, return the raw data
        if savetoCsv:
            today = date.today()
            # Create a filename with the current date
            save_csv_with_incremental_number(
                df, f"fao_{today}", f"{root}/temp/")
            # df.to_csv(
            #     f"{root}/temp/{indicator_Name}_{startYear}_{endYear}.csv", index=False)
            return df
        else:
            return df
    else:
        # if pivot = True, df is transformed by using "element" and "item"
        # Combine 'element' and 'item' into a single column for unique column names
        df['col_name'] = df['Element'] + '_' + df['Item']

        # convert text to numeric, it not working give NA
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

        # Pivot the table
        df_pivot = df.pivot_table(
            index=['Area', 'Year'],
            columns='col_name',
            values='Value'
        ).reset_index()

        if savetoCsv:
            today = date.today()
            # Create a filename with the current date
            save_csv_with_incremental_number(
                df_pivot, f"fao_{today}", f"{root}/temp/")
            # df.to_csv(
            #     f"{root}/temp/{indicator_Name}_{startYear}_{endYear}.csv", index=False)
            return df_pivot
        else:
            return df_pivot


# Importing World Bank data for various indicators across multiple countries
all_countries_list = ['VNM', 'LAO', 'THA', 'KHM', 'MYS', 'SGP', 'MMR',
                      'PHL', 'BRN', 'IDN', 'BGD', 'IND', 'PAK', 'NPL', 'LKA', 'BTN']
all_countries_list_fao = [704, 418, 764, 116, 458,
                          702, 104, 608, 96, 360, 50, 356, 586, 524, 144, 64]
all_countries_list_dic = dict(zip(all_countries_list, all_countries_list_fao))

indicators_imf = [
    {'indicator_ID': 'IMF_FAS_FCMT',
        'name': 'Use of Financial Services, Number of mobile money transactions (during the reference year)'},
    {'indicator_ID': 'IMF_FAS_FCMTV',
        'name': 'Use of Financial Services, Value of mobile money transactions (during the reference year)'},
    {'indicator_ID': 'IMF_FAS_FCMAA',
        'name': 'Use of Financial Services, Number of active mobile money accounts'}
]

indicators_v2 = [
    {'indicator_ID': 'IT.NET.BBND.P2',
        'name': 'Fixed Broadband Subscriptions (per 100 people)'},
    {'indicator_ID': 'IT.CEL.SETS.P2',
        'name': 'Mobile Cellular Subscriptions (per 100 people)'},
    {'indicator_ID': 'EG.ELC.ACCS.RU.ZS',
        'name': 'Access to Electricity, rural (% of Rural Pop.)'},
    {'indicator_ID': 'account.t.d', 'name': 'Account (% age 15+)'},
    {'indicator_ID': 'account.t.d.1', 'name': 'Account, female (% age 15+)'},
    {'indicator_ID': 'account.t.d.2', 'name': 'Account, male (% age 15+)'},
    {'indicator_ID': 'account.t.d.9', 'name': 'Account, rural (% age 15+)'},
    {'indicator_ID': 'account.t.d.10', 'name': 'Account, urban (% age 15+)'},
    {'indicator_ID': 'fin1.t.d',
        'name': 'Financial institution account (% age 15+)'},
    {'indicator_ID': 'fin1.t.d.1',
        'name': 'Financial institution account, female (% age 15+)'},
    {'indicator_ID': 'fin1.t.d.2',
        'name': 'Financial institution account, male (% age 15+)'},
    {'indicator_ID': 'fin1.t.d.9',
        'name': 'Financial institution account, rural (% age 15+)'},
    {'indicator_ID': 'fin1.t.d.10',
        'name': 'Financial institution account, urban (% age 15+)'},
    {'indicator_ID': 'mobileaccount.t.d',
        'name': 'Mobile money account (% age 15+)'},
    {'indicator_ID': 'mobileaccount.t.d.1',
        'name': 'Mobile money account, female (% age 15+)'},
    {'indicator_ID': 'mobileaccount.t.d.2',
        'name': 'Mobile money account, male (% age 15+)'},
    {'indicator_ID': 'mobileaccount.t.d.9',
        'name': 'Mobile money account, rural (% age 15+)'},
    {'indicator_ID': 'mobileaccount.t.d.10',
        'name': 'Mobile money account, urban (% age 15+)'},
    {'indicator_ID': 'Own.phone', 'name': 'Own a mobile phone (% age 15+)'},
    {'indicator_ID': 'fin2.7.t.d',
        'name': 'Owns a debit or credit card (% age 15+)'},
    {'indicator_ID': 'fin2.7.t.d.1',
        'name': 'Owns a debit or credit card, female (% age 15+)'},
    {'indicator_ID': 'fin2.7.t.d.2',
        'name': 'Owns a debit or credit card, male (% age 15+)'},
    {'indicator_ID': 'fin2.7.t.d.9',
        'name': 'Owns a debit or credit card, rural (% age 15+)'},
    {'indicator_ID': 'fin2.7.t.d.10',
        'name': 'Owns a debit or credit card, urban (% age 15+)'},
    {'indicator_ID': 'SP.POP.TOTL', 'name': 'Population, total'},
    {'indicator_ID': 'SP.URB.TOTL.IN.ZS',
        'name': 'Urban population (% of total population)'},
    {'indicator_ID': 'SP.RUR.TOTL.ZS',
        'name': 'Rural population (% of total population)'},
    {'indicator_ID': 'SP.DYN.LE00.IN',
        'name': 'Life expectancy at birth, total (years)'},
    {'indicator_ID': 'SP.DYN.IMRT.IN',
        'name': 'Mortality rate, infant (per 1,000 live births)'},
    {'indicator_ID': 'EN.POP.DNST',
        'name': 'Population density (people per sq. km of land area)'},
    {'indicator_ID': 'SI.POV.NAHC',
        'name': 'Poverty headcount ratio at national poverty lines (% of population)'},
    {'indicator_ID': 'SP.POP.GROW', 'name': 'Population growth (annual %)'},
    {'indicator_ID': 'SP.DYN.TFRT.IN',
        'name': 'Fertility rate, total (births per woman)'},
    {'indicator_ID': 'NY.GDP.PCAP.PP.KD',
        'name': 'GDP per capita, PPP (constant 2021 international $)'}
]

indicators_faoCredit = {
    'db': 'IC',
    'dbName': 'Credit to Agriculture',
    'element': {'Value US$, 2015 prices': '6179'},
    'item': {'Credit to Agriculture, Forestry and Fishing': '23068'},
    'area': {'-- Southern Asia > (List)': '5303>', '-- South-eastern Asia > (List)': '5304>'},
    'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
}

indicators_faoAddedValue = {
    'db': 'MK',
    'dbName': 'Macro Indicators',
    'element': {'Value US$, 2015 prices': '6179'},
    'item': {'Value Added (Agriculture, Forestry and Fishing)': '22016', 'Value Added (Manufacture of food and beverages)': '22077'},
    'area': {'-- Southern Asia > (List)': '5303>', '-- South-eastern Asia > (List)': '5304>'},
    'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
}

indicators_faoFertilizer = {
    'db': 'RFN',
    'dbName': 'Fertilizers by Nutrient',
    'element': {'Use per area of cropland': '5159'},
    'item': {'Nutrient nitrogen N (total)': '3102'},
    'area': {'-- Southern Asia > (List)': '5303>', '-- South-eastern Asia > (List)': '5304>'},
    'year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
}


# # Importing indicators from World Bank v2
# for item in indicators_v2:
#     indicator_Id = item['indicator_ID']
#     indicator_Name = item['name']
#     print(f"Importing {indicator_Name} ({indicator_Id})")
#     df = importWB_v2(
#         indicator_Id, indicator_Name, all_countries_list, 2010, 2023, savetoCsv=True)
#     if not df.empty:
#         print(df.head())
#     else:
#         print(f"No data found for {indicator_Name} ({indicator_Id})")

# # importing indicators from FAO
