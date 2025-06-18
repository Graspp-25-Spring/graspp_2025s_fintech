import requests
import pandas as pd
import faostat

# Set the root directory for saving data
root = 'Data/processed/'


def importWB_v2(indicator_Id, indicator_Name, countries, startYear, endYear, savetoCsv=False):
    # connect countries to string
    if isinstance(countries, list):
        country_str = ';'.join(countries)
    else:
        country_str = countries

    url = f"https://api.worldbank.org/v2/country/{country_str}/indicator/{indicator_Id}"
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
        df = df.rename(columns={'date': 'Year', 'value': indicator_Name})
        if savetoCsv:
            df.to_csv(
                f"{root}/temp/{indicator_Name}_{startYear}_{endYear}.csv", index=False)
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
    
def importFAO(db, myParam, pivot=False, savetoCsv=False):

    # Define parameters for importFAO: area, element, item, year using a dictionary
    def setParams(dbDictionary):
        element_list = list(dbDictionary['element'].values())
        item_list = list(dbDictionary['item'].values())
        area_list = list(dbDictionary['area'].values())
        year_list = dbDictionary['year']
        result = {
            # 'db': dbDictionary['db'],
            'element': element_list,
            'item': item_list,
            'area': area_list,
            'year': year_list
        }
        return result

    # Set parameters for the FAO database
    params = setParams(myParam) 

    # Get the start and end year from the parameters
    startYear = min(myParam['year'])
    endYear = max(myParam['year'])

    # Download data as a pandas DataFrame
    df = faostat.get_data_df(db, pars=params)

    if pivot == False:
        # if pivot = false, return the raw data
        if savetoCsv:
            df.to_csv(
                f"{root}/temp/{indicator_Name}_{startYear}_{endYear}.csv", index=False)
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
        return df_pivot


def importWB_v1(database_id, indicator_Id, indicator_Name, countries, startYear, endYear, savetoCsv=False):
    # connect countries to string
    if isinstance(countries, list):
        country_str = ';'.join(countries)
    else:
        country_str = countries

    url = f"https://data360api.worldbank.org/data360/data?DATABASE_ID={database_id}&INDICATOR={indicator_Id}&REF_AREA={country_str}&timePeriodFrom={startYear}&timePeriodTo={endYear}&skip=0"

    print(url)
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()
    records = data['data']
    df = pd.DataFrame(records)

    # Extract only necessary columns
    df = df[['REF_AREA', 'TIME_PERIOD', 'OBS_VALUE']]
    df = df.rename(columns={'REF_AREA': 'country',
                   'TIME_PERIOD': 'Year', 'OBS_VALUE': indicator_Name})
    if savetoCsv:
        root = 'Data/processed/'
        df.to_csv(
            f"{root}/temp/{indicator_Name}_{startYear}_{endYear}.csv", index=False)
    return df


# Importing World Bank data for various indicators across multiple countries
all_countries_list = ['VNM', 'LAO', 'THA', 'KHM', 'MYS', 'SGP', 'MMR',
                      'PHL', 'BRN', 'IDN', 'BGD', 'IND', 'PAK', 'NPL', 'LKA', 'BTN']

indicators_v1 = [
    {'indicator_ID': 'FAO_IC_23068',
        'name': 'Credit to Agriculture'},
    {'indicator_ID': 'NV.AGR.TOTL.CD',
        'name': 'Value Added (Agriculture, Forestry and Fishing)'},
    {'indicator_ID': 'NV.MNF.FBTO.CD',
        'name': 'Value Added (Manufacture of food and beverages)'},
    {'indicator_ID': 'AG.CON.FERT.ZS',
        'name': 'Fertilizer consumption (kilograms per hectare of arable land)'},
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

for i in range(len(indicators_v1)):
    indicator_Id = indicators_v1[i]['indicator_ID']
    indicator_Name = indicators_v1[i]['name']
    database_id = indicators_v1[i]['dbName']
    print(f"Importing {indicator_Name} ({indicator_Id})")
    df = importWB_v1(
        database_id, indicator_Id, indicator_Name, all_countries_list, 2010, 2023, savetoCsv=True)
    if not df.empty:
        print(df.head())
    else:
        print(f"No data found for {indicator_Name} ({indicator_Id})")
