import pandas as pd
import os

# [1] Set project root and file paths
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

gfi_path = os.path.join(project_root, 'data', 'processed', 'gfi_final_output.csv')
wdi_path = os.path.join(project_root, 'data', 'processed', 'wdi_final_output.csv')
processed_long_path = os.path.join(project_root, 'data', 'processed', 'merged_output.csv')
processed_wide_path = os.path.join(project_root, 'data', 'processed', 'merged_output_wide.csv')

# [2] Load datasets
df_gfi = pd.read_csv(gfi_path)
df_wdi = pd.read_csv(wdi_path)

# [3] Concatenate the two datasets vertically
df_merged = pd.concat([df_gfi, df_wdi], ignore_index=True)

# [4] Ensure correct type for date column and sort
df_merged['date'] = pd.to_numeric(df_merged['date'], errors='coerce')
df_merged = df_merged.dropna(subset=['date'])  # Remove rows with invalid dates

# [5] Remove invalid country codes (like 'South Asia', 'Southeast Asia')
df_merged = df_merged[df_merged['countryiso3code'].str.len() == 3]

# [6] Sort for long format
df_merged = df_merged.sort_values(by=['country', 'indicator', 'date'], ascending=[True, True, False])

# [7] Save long format
df_merged.to_csv(processed_long_path, index=False)
print(f"✅ Long-format file saved to: {processed_long_path}")

# [8] Pivot to wide format using ISO3 code and date only
df_wide = df_merged.pivot_table(
    index=['countryiso3code', 'date'],
    columns='indicator',
    values='value',
    aggfunc='first'
).reset_index()

# [9] Rename columns
df_wide = df_wide.rename(columns={
    'countryiso3code': 'country',
    'date': 'year'
})

# [10] Sort and save wide format
df_wide = df_wide.sort_values(by=['country', 'year'], ascending=[True, False])
df_wide.to_csv(processed_wide_path, index=False)
print(f"✅ Wide-format file saved to: {processed_wide_path}")