import pandas as pd


def variable_summary(inputFile, sourceFolder='Data/processed/', outFolder='Data/processed/', country_col='code'):
    # This script summarizes the variables in a dataset, providing insights into their types, non-missing values, missing values, and unique counts.
    # It also generates summaries for each country in the dataset, saving them to CSV files.

    df = pd.read_csv(sourceFolder + inputFile)
    # Ensure 'Year' is renamed to 'year' for consistency
    df = df.rename(columns={'Year': 'year'})

    df = df[(df['year'] >= 2010) & (df['year'] <= 2025)]

    def make_summary(df):
        return pd.DataFrame({
            'type': df.dtypes,
            'non_missing': df.notna().sum(),
            'missing': df.isna().sum(),
            'nunique': df.nunique()
        })

    # Whole dataset summary
    summary = make_summary(df)
    summary.to_csv(outFolder + 'variable_summary_all.csv')
    print(df.columns)

    # Country by country summary
    print(f'Country column used for summary: {country_col}')
    if country_col in df.columns:
        for country, group in df.groupby(country_col):
            country_summary = make_summary(group)
            country_name = str(country).replace('/', '_').replace(' ', '_')
            country_summary.to_csv(
                f"{outFolder}variable_summary_{country_name}.csv")
    else:
        print('No country column found for per-country summary.')
    return summary


# usage example #####################################################
#
# inputFile = 'fertilizer_FUCB_processed.csv'
# variable_summary(inputFile, outFolder='Data/processed/temp/',
#                  country_col='country')
#
# This code summarizes the variables in a dataset, providing insights into their types, non-missing values, missing values, and unique counts.
# It also generates summaries for each country in the dataset, saving them to CSV files.
# The function variable_summary reads a CSV file, filters the data for the years 2010 to 2025, and creates a summary of the variables.
# The summary includes the type of each variable, the count of non-missing values, the count of missing values, and the number of unique values.
# end example #####################################################
