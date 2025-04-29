import pandas as pd
import os

# [1] Setting the project path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(project_root, 'data', 'processed', 'gfi_digital_transaction_history.csv')

# [2] Loading data
df = pd.read_csv(file_path)

# [3] Filter Southeast Asia & South Asia countries
southeast_asia_list = ['VNM','LAO','THA','KHM','MYS','SGP','MMR','PHL','BRN','IDN']
south_asia_list = ['BGD','IND','PAK','NPL','LKA','BTN']
target_countries = southeast_asia_list + south_asia_list
df = df[df["Country Code"].isin(target_countries)]

# [4] Separate years in wide → long format
df_long = pd.melt(
    df,
    id_vars=["Country Name", "Country Code", "Series Name", "Series Code"],
    var_name="year",
    value_name="value"
)

# [5] Extract only the year number ("2011 [YR2011]" → 2011)
df_long["year"] = df_long["year"].str.extract(r"(\d{4})")
df_long["year"] = df_long["year"].astype(int)

# [6] Number conversion
df_long["value"] = pd.to_numeric(df_long["value"], errors="coerce")

# [7] pivot: Organize indicators into columns, organize values ​​by country and year
df_pivot = df_long.pivot_table(
    index=["Country Code", "year"],
    columns="Series Name",
    values="value"
).reset_index()

# [8] Preview results
print(df_pivot.head())

# Saving Path
save_path = os.path.join(project_root, 'data', 'processed', 'gfi_digital_transaction_pivot_table.csv')
df_pivot.to_csv(save_path, index=False)
print(f"✅ Save complete: {save_path}")