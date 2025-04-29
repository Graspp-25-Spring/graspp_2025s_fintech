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
    "Made a digital payment (% age 15+)",
    "Made a digital merchant payment (% age 15+)",
    "Made a digital online merchant payment for an online purchase (% age 15+)",
    "Made a utility payment (% age 15+)",
    "Made a utility payment: using a financial institution account (% age 15+)",
    "Made a utility payment: using a mobile phone (% age 15+)",
    "Used a mobile phone or the internet to make payments, buy things, or to send or receive money using a financial institution account (% age 15+)",
    "Used a mobile phone or the internet to buy something online (% age 15+)",
    "Used a mobile phone or the internet to send money (% age 15+)",
    "Made a deposit (% with a financial institution account, age 15+)",
    "Made a withdrawal (% with a financial institution account, age 15+)",
    "Store money using a financial institution or a mobile money account (% age 15+)",
    "Made or received a digital payment (% age 15+)",
    "Received digital payments (% age 15+)",
    "Saved at a financial institution or using a mobile money account (% age 15+)",
    "Saved money using a mobile money account (% age 15+)"
]

# [Step 5] Extract only selected columns
id_columns = ["Country Name", "Country Code", "Series Name", "Series Code"]

# Total columns to extract = Identification + Inclusion related metrics
columns_to_keep = id_columns + target_columns
df_selected = df[df['Series Name'].isin(target_columns)]

# [Step 6] Create a path for the processed folder to be saved
processed_data_path = os.path.join(project_root, 'data', 'processed', 'gfi_digital_transaction_history.csv')

# [Step 7] Save as a new file
df_selected.to_csv(processed_data_path, index=False)

print(f"✅ Data was saved successfully: {processed_data_path}")