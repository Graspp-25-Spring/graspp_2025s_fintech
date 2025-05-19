import pandas as pd
import os

# [1] Set project root and file paths
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

gfi_path = os.path.join(project_root, 'data', 'processed', 'gfi_final_output.csv')
wdi_path = os.path.join(project_root, 'data', 'processed', 'wdi_final_output.csv')
processed_path = os.path.join(project_root, 'data', 'processed', 'merged_output.csv')

# [2] Load datasets
df_gfi = pd.read_csv(gfi_path)
df_wdi = pd.read_csv(wdi_path)

# [3] Concatenate the two datasets vertically
df_merged = pd.concat([df_gfi, df_wdi], ignore_index=True)

# [4] Ensure correct type for date column and sort descending by date
df_merged['date'] = pd.to_numeric(df_merged['date'], errors='coerce')
df_merged = df_merged.sort_values(by=['country', 'indicator', 'date'], ascending=[True, True, False])

# [5] Save to CSV
df_merged.to_csv(processed_path, index=False)

print(f"✅ Successfully merged and saved to: {processed_path}")