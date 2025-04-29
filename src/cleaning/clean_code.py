# [Step 1] Importing required libraries
import pandas as pd
import os

# [Step 2] Setting the file path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create a path to the raw file 
raw_data_path = os.path.join(project_root, 'data', 'raw', 'gfi.csv')

# [Step 3] Loading data
df = pd.read_csv(raw_data_path)

# [Step 4] Create a list of required columns 
target_columns = [
    "Account (% age 15+)",
    "Account, female (% age 15+)",
    "Account, male (% age 15+)",
    "Account, rural (% age 15+)",
    "Account, urban (% age 15+)",
    "Financial institution account (% age 15+)",
    "Financial institution account, female (% age 15+)",
    "Financial institution account, male (% age 15+)",
    "Financial institution account, rural (% age 15+)",
    "Financial institution account, urban (% age 15+)",
    "Mobile money account (% age 15+)",
    "Mobile money account, female (% age 15+)",
    "Mobile money account, male (% age 15+)",
    "Mobile money account, rural (% age 15+)",
    "Mobile money account, urban (% age 15+)",
    "Own a mobile phone (% age 15+)",
    "Owns a debit or credit card (% age 15+)"
]

# [Step 5] Extract only selected columns
id_columns = ["Country Name", "Country Code", "Series Name", "Series Code"]

# Total columns to extract = Identification + Inclusion related metrics
columns_to_keep = id_columns + target_columns
df_selected = df[df['Series Name'].isin(target_columns)]

# [Step 6] Create a path for the processed folder to be saved
processed_data_path = os.path.join(project_root, 'data', 'processed', 'gfi_financial_inclusion.csv')

# [Step 7] Save as a new file
df_selected.to_csv(processed_data_path, index=False)

print(f"✅ Data was saved successfully: {processed_data_path}")