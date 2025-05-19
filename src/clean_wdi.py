import pandas as pd
import os

# [1] Load raw WDI data
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(project_root, 'data', 'raw', 'wdi.csv')

# [2] Load data
df = pd.read_csv(raw_data_path)

# [3] Melt wide → long format
df_long = df.melt(
    id_vars=["Country Name", "Country Code", "Series Name", "Series Code"],
    var_name="date",
    value_name="value"
)

# [4] Clean and extract year from date
df_long['date'] = df_long['date'].str.extract(r'(\d{4})')
df_long = df_long.dropna(subset=['date'])
df_long['date'] = df_long['date'].astype(int)

# [5] Rename columns
df_long = df_long.rename(columns={
    'Country Name': 'country',
    'Country Code': 'countryiso3code',
    'Series Name': 'indicator'
})

# [6] Add required empty columns
df_long['unit'] = pd.NA
df_long['obs_status'] = pd.NA
df_long['decimal'] = 0

# [7] Region classification
asean_countries = [
    'Brunei Darussalam', 'Cambodia', 'Indonesia', 'Lao PDR', 'Malaysia',
    'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Viet Nam'
]
south_asia_countries = [
    'Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka'
]

def assign_region(country):
    if country in asean_countries:
        return 'ASEAN'
    elif country in south_asia_countries:
        return 'South Asia'
    else:
        return 'Other'

df_long['Region'] = df_long['country'].apply(assign_region)

# [8] Sort by country → indicator → date
df_sorted = df_long.sort_values(by=['country', 'indicator', 'date'], ascending=[True, True, False])

# [9] Select and reorder columns
final_columns = [
    'country', 'date', 'indicator', 'countryiso3code', 'value',
    'unit', 'obs_status', 'decimal', 'Region'
]
df_final = df_sorted[final_columns]

# [10] Save to file
processed_path = os.path.join(project_root, 'data', 'processed', 'wdi_final_output.csv')
df_final.to_csv(processed_path, index=False)

print(f"✅ WDI data successfully transformed and sorted by country → indicator → date. Saved to: {processed_path}")