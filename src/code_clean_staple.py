import pandas as pd
import os
import pycountry

# [1] Load the dataset
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(project_root, 'data', 'raw', 'StapleFoodStability.csv')

# read data
df = pd.read_csv(raw_data_path)

# [2] Create a dictionary mapping country names to ISO3 codes using pycountry
country_to_iso3 = {country.name: country.alpha_3 for country in pycountry.countries}

# [3] Handle exceptions: manually map names that differ from pycountry's naming
manual_mappings = {
    "Côte d'Ivoire": "CIV",
    "Democratic Republic of the Congo": "COD",
    "Republic of the Congo": "COG",
    "Eswatini": "SWZ",
    "Iran (Islamic Republic of)": "IRN",
    "Lao People's Democratic Republic": "LAO",
    "Republic of Korea": "KOR",
    "Micronesia (Federated States of)": "FSM",
    "Republic of Moldova": "MDA",
    "Russian Federation": "RUS",
    "Syrian Arab Republic": "SYR",
    "The former Yugoslav Republic of Macedonia": "MKD",
    "United Republic of Tanzania": "TZA",
    "Venezuela (Bolivarian Republic of)": "VEN",
    "Viet Nam": "VNM",
    "Bolivia (Plurinational State of)": "BOL",
    "Brunei Darussalam": "BRN"
}
country_to_iso3.update(manual_mappings)

# [4] Map 'Area' column values to ISO3 codes
df['Area'] = df['Area'].map(country_to_iso3)

# [5] Rename column
df = df.rename(columns={'Area': 'country'})
df = df.rename(columns={'Year': 'year'})

# [6] Overwrite the original file with updated data
df.to_csv(raw_data_path, index=False)

# [7] Print confirmation message
print("✅ ISO3 code replacement complete and file successfully overwritten.")