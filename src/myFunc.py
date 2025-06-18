import os
import csv
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import faostat
import pandas as pd


def getFileDialogue():
    # Get the absolute path to the top-level project folder
    project_root = Path(__file__).resolve().parent.parent  # Adjust as needed

    # Example: 'data' folder under the project root
    data_dir = project_root / 'data'

    root = tk.Tk()
    root.withdraw()

    # Use the absolute path as initialdir
    file_path = filedialog.askopenfilename(initialdir=data_dir)
    print(file_path)

    # df = pd.read_stata('data_original/ZAAHM71FL/ZAAHM71FL.DTA', iterator = True)
    # labels = df.variable_labels()
    # for key, value in labels.items():
    #     print(key, ": ", value)


def get_year_range():
    while True:
        try:
            # Get input for startYear and endYear
            startYear = int(input("Please enter the start year (1950-2025): "))
            endYear = int(input("Please enter the end year (1950-2025): "))

            # Verify the years are within the valid range
            if not (1950 <= startYear <= 2025):
                print("Invalid input. Start year must be between 1950 and 2025.")
                continue
            if not (1950 <= endYear <= 2025):
                print("Invalid input. End year must be between 1950 and 2025.")
                continue

            # Verify startYear <= endYear
            if startYear > endYear:
                print(
                    "Invalid input. Start year must be less than or equal to end year.")
                continue

            # Generate the list of years
            year_range = list(range(startYear, endYear + 1))
            print(f"Generated year range: {year_range}")
            return year_range

        except ValueError:
            print("Invalid input. Please enter valid numbers.")


# # Example usage
# years = get_year_range()
# print("Final year range:", years)


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

# # Define parameters: area, element, item, year
# mypars = {
#     'area': '4',  # Afghanistan (use faostat.get_par('QCL', 'area') to get codes)
#     'element': [2413],  # Area harvested (use faostat.get_par('QCL', 'element') to get codes)
#     'item': '1735>',  # Almonds, with shell (use faostat.get_par('QCL', 'item') to get codes)
#     'year': [2014, 2023]
# }


def dictToCSV(myDict, fileName):
    with open(fileName, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Key', 'Value'])  # Optional: write header
        for key, value in myDict.items():
            writer.writerow([key, value])


def getDbParams(dbName, saveToCsv=False, output_folder='data_output/', params=None):
    # Set default params if not provided
    if params is None:
        params = ['area', 'element', 'item']

    # set Dict to save the results
    myRes = {}

    # Fetch data based on parameters
    if 'area' in params:
        df_area = faostat.get_par(dbName, 'area')
        myRes['area'] = df_area

    if 'element' in params:
        df_element = faostat.get_par(dbName, 'element')
        myRes['element'] = df_element

    if 'item' in params:
        df_item = faostat.get_par(dbName, 'item')
        myRes['item'] = df_item

    if saveToCsv:
        if myRes['area'] is not None:
            output_file = output_folder + dbName + '_area.csv'
            dictToCSV(df_area, output_file)

        if myRes['element'] is not None:
            output_file = output_folder + dbName + '_element.csv'
            dictToCSV(df_element, output_file)

        if myRes['item'] is not None:
            output_file = output_folder + dbName + '_item.csv'
            dictToCSV(df_item, output_file)

    return myRes


def getUserChoiceFromList(myList, pageBy=20, multiSelect=False):
    if not isinstance(myList, (dict, list)):
        print("Error: myList should be a dictionary or list")
        return False

    if isinstance(myList, list):
        # Convert list to dictionary with index as key
        myList = {i: item for i, item in enumerate(myList)}

    # Initialize variables
    db_code = {}
    rowNum = 0
    userInput = ''
    endOfList = len(myList)
    exit_for_loop = False  # Flag to exit the for loop

    # Iterate through the list
    # for key, value in myList.items():
    while True:
        rowNum += 1
        # Access the key-value pair
        key, value = list(myList.items())[rowNum - 1]
        print(f'[{rowNum}] {key}: {value}')

        if (rowNum % pageBy == 0 or rowNum >= endOfList):
            print("Please select the element code you want to use: multiple numbers are allowed, separated by comma")
            print("put 'x' to quit")

            # Check if we need to pause for user input
            while True:
                # Placeholder logic to avoid indentation error
                userInput = input()
                if userInput == 'x':
                    print("Exiting...")
                    return False
                elif userInput == '':
                    if rowNum >= endOfList:
                        rowNum = 0  # Reset rowNum for the next page
                        print("next page...")
                    break  # Continue to the next set of rows

                elif all(part.strip().isdigit() for part in userInput.split(',')):
                    print("You entered a list of numbers separated by commas.")
                    for myNum in userInput.split(','):
                        db_index = int(myNum) - 1
                        if 0 <= db_index < len(myList):
                            # Correctly access the 'code' column
                            key, value = list(myList.items())[db_index]
                            db_code[key] = value
                        else:
                            print("omit Invalid number...")

                    exit_for_loop = True  # Set the flag to exit the for loop
                    break

                else:
                    print(
                        f"Invalid input. Please enter a valid number (1..{len(myList)}), 'x' to quit, or press Enter to continue.")

            if exit_for_loop:  # Check the flag after the while loop
                break  # Exit the for loop

    return db_code
    # usage example
    # myList = {
    #     'a': 1,
    #     'b': 2,
    #     'c': 3,
    #     'd': 4,
    #     'e': 5,
    #     'f': 6,
    #     'g': 7,
    #     'h': 8,
    #     'i': 9,
    #     'j': 10
    # }
    # myResult = getUserChoiceFromList(myList, pageBy=5)
    # print(myResult)


def getDbInfo():
    # Get the list of available FAO databases
    dbParams = {}
    result = {}

    db_list = faostat.list_datasets_df()
    # Select only the 'code' and 'label' columns and convert to a dictionary
    db_list = db_list.set_index('label')['code'].to_dict()

    myDb = getUserChoiceFromList(db_list)
    dbName, dbCode = list(myDb.items())[0]

    dbParams = getDbParams(dbCode)
    myElements = getUserChoiceFromList(dbParams['element'])
    myItems = getUserChoiceFromList(dbParams['item'])
    myAreas = getUserChoiceFromList(dbParams['area'])
    myYears = get_year_range()

    result['db'] = dbCode
    result['dbName'] = dbName
    result['element'] = myElements
    result['item'] = myItems
    result['area'] = myAreas
    result['year'] = myYears

    print(result)

    return result


def importWB(database_id, indicator_id, year_from, year_to):
    import requests
    import pandas as pd

    url = (
        f"https://data360api.worldbank.org/data360/data"
        f"?DATABASE_ID={database_id}&INDICATOR={indicator_id}"
        f"&timePeriodFrom={year_from}&timePeriodTo={year_to}&skip=0"
    )
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)
    data = response.json()

    # The data is under the "value" key
    if "value" in data and data["value"]:
        df = pd.DataFrame(data["value"])
        return df
    else:
        print("No data available for the requested indicator and database.")
        return False

# example of function usage
# mydf_ICTPolicy = importWB("ITU_ICT", "ITU_ICT_G5_DIG_ECON", "2000", "2025")
# mydf_FarmCredit = importWB("FAO_IC", "FAO_IC_23068", "2000", "2025")
# mydf_Value_AgProduction = importWB("FAO_MK", "FAO_MK_22016", "2000", "2025")
# mydf_Value_AgProcessing = importWB("FAO_MK", "FAO_MK_22077", "2000", "2025")
# mydf_Fertilizer = importWB("WB_WDI", "WB_WDI_AG_CON_FERT_ZS", "2000", "2025")
# print(mydf_ICTPolicy.head())


###################### function test ##############################################
# df = importFAO(mypars)
# df = faostat.list_datasets_df()
# df.to_csv("fao_db_list.csv")
# getDbParams('CP')
# res = getDbInfo()
# print(res)
getDbInfo()
