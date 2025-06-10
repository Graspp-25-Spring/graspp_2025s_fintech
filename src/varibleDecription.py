def variableDescription(inputFile, outputFile='variableDescription.csv', filterCSV = False):
    """
    This function generates a summary of the variables in the dataset.
    It reads a CSV file, filters the data for specific years, converts
    object columns to numeric, and then creates a summary statistics
    DataFrame which is saved to a new CSV file.
    """
    import pandas as pd

    sourceFolder = 'Data/processed/'
    outFolder = 'Data/processed/'
    file = sourceFolder + inputFile
    df = pd.read_csv(file)
    df = df[(df['year'] >= 2010) & (df['year'] <= 2025)]

    # Convert object columns that are actually numbers to numeric
    if filterCSV:
        for col in df.select_dtypes(include='object').columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # create summary stats for all the varialbe
    df_summary = df.describe()
    df_summary = df_summary.transpose()
    df_summary.to_csv(outFolder + outputFile)
    return df_summary

# usage example #####################################################
#
# fileName = 'merged_data_2.csv'
# variableDescription(fileName)
# print("Variable description completed.")
# This code generates a summary of the variables in a dataset, providing insights into their types, non-missing values, missing values, and unique counts.
# It reads a CSV file, filters the data for the years 2010 to 2025, and creates a summary statistics DataFrame.
# The summary includes the type of each variable, the count of non-missing values, the count of missing values, and the number of unique values.
#
# end example #####################################################

variableDescription('merged_final.csv')
print("Variable description completed.")
