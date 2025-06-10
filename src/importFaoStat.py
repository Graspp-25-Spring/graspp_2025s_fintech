import pandas as pd
import faostat

root = 'Data/processed/'


# exportCSV function
# this function exports a pandas DataFrame to a CSV file
def exportCSV(df, fileName):
    output = root + fileName + '.csv'
    df.to_csv(output)
    return True


#
# Define parameters: area, element, item, year
FBSdata = {'db': 'FBS',
           'dbName': 'Food Balances (2010-)',
           'element': {'Food supply quantity (kg/capita/yr)': '645'},
           'item': {'Cereals - Excluding Beer + (Total)': '2905', 'Starchy Roots + (Total)': '2907'},
           'area':  {'-- Southern Asia > (List)': '5303>', '-- South-eastern Asia > (List)': '5304>'},
           'year': [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
           }
# # Define parameters: area, element, item, year
# mypars = {
#     'area': '4',  # Afghanistan (use faostat.get_par('QCL', 'area') to get codes)
#     'element': [2413],  # Area harvested (use faostat.get_par('QCL', 'element') to get codes)
#     'item': '1735>',  # Almonds, with shell (use faostat.get_par('QCL', 'item') to get codes)
#     'year': [2014, 2023]
# }  


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


# importFAO function
# this function imports data from FAO database using the faostat package and uses the parameters defined in setParams
def importFAO(db, params, pivot=False):
    # Download data as a pandas DataFrame
    df = faostat.get_data_df(db, pars=params)

    if pivot == False:
        # if pivot = false, return the raw data
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


################################ calculate stability of staple food supply #################################
mypars = setParams(FBSdata)

df_FBS = importFAO('FBS', mypars, pivot=True)

# Calculate rolling mean for comparison
df_FBS['rolling_std'] = df_FBS['Food supply quantity (kg/capita/yr)_Cereals - Excluding Beer'].rolling(
    window=5).std()

exportCSV(df_FBS, 'StapleFoodStability')
