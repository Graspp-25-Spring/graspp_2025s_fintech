import pandas as pd
import numpy as np
import os

# [1] Set project root path based on current script location
try:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    project_root = os.getcwd()  # fallback for interactive environments

# [2] Define file path for input data
processed_data_path = os.path.join(project_root, 'data', 'processed', 'merged_output_wide.csv')

# [3] Load dataset
df = pd.read_csv(processed_data_path)

# [4] Replace '..' strings with actual NaN values
df = df.replace('..', np.nan).infer_objects(copy=False)  # suppress FutureWarning

# [5] Identify columns that contain numerical values (exclude country and year)
value_cols = [col for col in df.columns if col not in ['country', 'year']]
df[value_cols] = df[value_cols].apply(pd.to_numeric, errors='coerce')

# [6] Define full year range and unique countries
years = list(range(2011, 2023))
countries = df['country'].unique()

# [7] Create a full index for all country-year combinations
full_index = pd.MultiIndex.from_product([countries, years], names=["country", "year"])
df_full = pd.DataFrame(index=full_index).reset_index()

# [8] Merge original data with full index to include missing years
df_merged = pd.merge(df_full, df, on=["country", "year"], how="left")

# [9] For each numeric column, interpolate missing values and fill edge NaNs
for col in value_cols:
    df_merged[col] = df_merged.groupby('country')[col].transform(
        lambda group: group.interpolate(method='linear').bfill().ffill()
    )

# [10] Set output file path (within project directory)
clean_path = os.path.join(project_root, 'data', 'processed', 'cleaned_output_2011_2022.csv')

# [11] Ensure output directory exists
os.makedirs(os.path.dirname(clean_path), exist_ok=True)

# [12] Save the cleaned dataset to CSV
df_merged.to_csv(clean_path, index=False)

# [13] Print confirmation
print(f"✅ Cleaned file saved successfully: {clean_path}")