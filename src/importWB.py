import requests
import pandas as pd

def importWB_v2(indicator_Id, indicator_Name, countries, startYear, endYear, savetoCsv=False):
    root = 'Data/processed/'

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
            df.to_csv(f"{root}/temp/{indicator_Name}_{startYear}_{endYear}.csv", index=False)
        return df
    else:
        print("No data found.")
        return pd.DataFrame()

def importWB_v1(database_id, indicator_Id, indicator_Name, countries, startYear, endYear, savetoCsv=False):
    url= f"https://data360api.worldbank.org/data360/data?DATABASE_ID={database_id}&INDICATOR={indicator_Id}&REF_AREA={countries}&timePeriodFrom={startYear}&timePeriodTo={endYear}&skip=0"
    response = requests.get(url)
    data = response.json()
    records = data['data']
    df = pd.DataFrame(records)

    # Extract only necessary columns
    df = df[['REF_AREA', 'TIME_PERIOD', 'OBS_VALUE']]
    df = df.rename(columns={'REF_AREA': 'country', 'TIME_PERIOD': 'Year', 'OBS_VALUE': indicator_Name})
    if savetoCsv:
        root = 'Data/processed/'
        df.to_csv(f"{root}/temp/{indicator_Name}_{startYear}_{endYear}.csv", index=False)
    return df



# Importing World Bank data for various indicators across multiple countries
all_countries_list = ['VNM','LAO','THA','KHM','MYS','SGP','MMR','PHL','BRN','IDN','BGD','IND','PAK','NPL','LKA','BTN']

all_indicator_Ids_list_v2 = ['IT.NET.BBND.P2', 'IT.CEL.SETS.P2', 'EG.ELC.ACCS.RU.ZS', 'account.t.d', 'account.t.d.1', 'account.t.d.2', 'account.t.d.9', 'account.t.d.10', 'fin1.t.d', 'fin1.t.d.1', 'fin1.t.d.2', 'fin1.t.d.9', 'fin1.t.d.10', 'mobileaccount.t.d', 'mobileaccount.t.d.1', 'mobileaccount.t.d.2', 'mobileaccount.t.d.9', 'mobileaccount.t.d.10', 'Own.phone', 'fin2.7.t.d', 'fin2.7.t.d.1', 'fin2.7.t.d.2', 'fin2.7.t.d.9', 'fin2.7.t.d.10', 'SP.POP.TOTL', 'SP.URB.TOTL.IN.ZS', 'SP.RUR.TOTL.ZS', 'SP.DYN.LE00.IN', 'SP.DYN.IMRT.IN', 'EN.POP.DNST', 'SI.POV.NAHC', 'SP.POP.GROW', 'SP.DYN.TFRT.IN', 'NY.GDP.PCAP.PP.KD', 'FAO_IC_23068']

all_indicator_Names_list_v2 = ['Fixed Broadband Subscriptions (per 100 people)', 'Mobile Cellular Subscriptions (per 100 people)', 'Access to Electricity, rural (% of Rural Pop.)', 'Account (% age 15+)', 'Account, female (% age 15+)', 'Account, male (% age 15+)', 'Account, rural (% age 15+)', 'Account, urban (% age 15+)', 'Financial institution account (% age 15+)', 'Financial institution account, female (% age 15+)', 'Financial institution account, male (% age 15+)', 'Financial institution account, rural (% age 15+)', 'Financial institution account, urban (% age 15+)', 'Mobile money account (% age 15+)', 'Mobile money account, female (% age 15+)', 'Mobile money account, male (% age 15+)', 'Mobile money account, rural (% age 15+)', 'Mobile money account, urban (% age 15+)', 'Own a mobile phone (% age 15+)', 'Owns a debit or credit card (% age 15+)', 'Owns a debit or credit card, female (% age 15+)', 'Owns a debit or credit card, male (% age 15+)', 'Owns a debit or credit card, rural (% age 15+)', 'Owns a debit or credit card, urban (% age 15+)', 'Population, total', 'Urban population (% of total population)', 'Rural population (% of total population)', 'Life expectancy at birth, total (years)', 'Mortality rate, infant (per 1,000 live births)', 'Population density (people per sq. km of land area)', 'Poverty headcount ratio at national poverty lines (% of population)', 'Population growth (annual %)', 'Fertility rate, total (births per woman)', 'GDP per capita, PPP (constant 2021 international $)']

all_indicator_Ids_list_v1 = ['FAO_IC_23068', 'FAO_MK_22016', 'FAO_MK_22077', 'WB_WDI_AG_CON_FERT_ZS', 'IMF_FAS_FCMT', 'IMF_FAS_FCMTV', 'IMF_FAS_FCMAA']

all_indicator_Names_list_v1 = ['Credit to Agriculture', 'Value Added (Agriculture, Forestry and Fishing)', 'Value Added (Manufacture of food and beverages)', 'Fertilizer consumption (kilograms per hectare of arable land)', 'Use of Financial Services, Number of mobile money transactions (during the reference year)', 'Use of Financial Services, Value of mobile money transactions (during the reference year)', 'Use of Financial Services, Number of active mobile money accounts']

all_db_list_v1 =['FAO_IC', 'FAO_MK', 'FAO_MK', 'WB_WDI', 'IMF_FAS', 'IMF_FAS', 'IMF_FAS']

indicators_v2 = zip(all_indicator_Ids_list_v2, all_indicator_Names_list_v2)
print(list(indicators_v2))

indicators_v1 = [
    ('FAO_IC_23068', 'Credit to Agriculture', 'FAO_IC'), 
    ('FAO_MK_22016', 'Value Added (Agriculture, Forestry and Fishing)', 'FAO_MK'), 
    ('FAO_MK_22077', 'Value Added (Manufacture of food and beverages)', 'FAO_MK'), 
    ('WB_WDI_AG_CON_FERT_ZS', 'Fertilizer consumption (kilograms per hectare of arable land)', 'WB_WDI'), 
    ('IMF_FAS_FCMT', 'Use of Financial Services, Number of mobile money transactions (during the reference year)', 'IMF_FAS'), 
    ('IMF_FAS_FCMTV', 'Use of Financial Services, Value of mobile money transactions (during the reference year)', 'IMF_FAS'), 
    ('IMF_FAS_FCMAA', 'Use of Financial Services, Number of active mobile money accounts', 'IMF_FAS')
    ]

indicators_v2 = [
    ('IT.NET.BBND.P2', 'Fixed Broadband Subscriptions (per 100 people)'), 
    ('IT.CEL.SETS.P2', 'Mobile Cellular Subscriptions (per 100 people)'), 
    ('EG.ELC.ACCS.RU.ZS', 'Access to Electricity, rural (% of Rural Pop.)'), 
    ('account.t.d', 'Account (% age 15+)'), 
    ('account.t.d.1', 'Account, female (% age 15+)'), 
    ('account.t.d.2', 'Account, male (% age 15+)'), 
    ('account.t.d.9', 'Account, rural (% age 15+)'), 
    ('account.t.d.10', 'Account, urban (% age 15+)'), 
    ('fin1.t.d', 'Financial institution account (% age 15+)'), 
    ('fin1.t.d.1', 'Financial institution account, female (% age 15+)'), 
    ('fin1.t.d.2', 'Financial institution account, male (% age 15+)'), 
    ('fin1.t.d.9', 'Financial institution account, rural (% age 15+)'), 
    ('fin1.t.d.10', 'Financial institution account, urban (% age 15+)'), ('mobileaccount.t.d', 'Mobile money account (% age 15+)'), ('mobileaccount.t.d.1', 'Mobile money account, female (% age 15+)'), ('mobileaccount.t.d.2', 'Mobile money account, male (% age 15+)'), ('mobileaccount.t.d.9', 'Mobile money account, rural (% age 15+)'), ('mobileaccount.t.d.10', 'Mobile money account, urban (% age 15+)'), ('Own.phone', 'Own a mobile phone (% age 15+)'), ('fin2.7.t.d', 'Owns a debit or credit card (% age 15+)'), ('fin2.7.t.d.1', 'Owns a debit or credit card, female (% age 15+)'), ('fin2.7.t.d.2', 'Owns a debit or credit card, male (% age 15+)'), ('fin2.7.t.d.9', 'Owns a debit or credit card, rural (% age 15+)'), ('fin2.7.t.d.10', 'Owns a debit or credit card, urban (% age 15+)'), ('SP.POP.TOTL', 'Population, total'), ('SP.URB.TOTL.IN.ZS', 'Urban population (% of total population)'), ('SP.RUR.TOTL.ZS', 'Rural population (% of total population)'), ('SP.DYN.LE00.IN', 'Life expectancy at birth, total (years)'), ('SP.DYN.IMRT.IN', 'Mortality rate, infant (per 1,000 live births)'), ('EN.POP.DNST', 'Population density (people per sq. km of land area)'), ('SI.POV.NAHC', 'Poverty headcount ratio at national poverty lines (% of population)'), ('SP.POP.GROW', 'Population growth (annual %)'), ('SP.DYN.TFRT.IN', 'Fertility rate, total (births per woman)'), ('NY.GDP.PCAP.PP.KD', 'GDP per capita, PPP (constant 2021 international $)')
    ]

exit()

for i in range(len(all_indicator_Ids_list_v1)):
    indicator_Id = all_indicator_Ids_list_v1[i]
    indicator_Name = all_indicator_Names_list_v1[i]
    print(f"Importing {indicator_Name} ({indicator_Id})")
    df = importWB_v1(indicator_Id, indicator_Name, all_countries_list, 2010, 2023, savetoCsv=True)
    if not df.empty:
        print(df.head())
    else:
        print(f"No data found for {indicator_Name} ({indicator_Id})")