import pandas as pd
import requests
import io
import os

# 1. Load the CSV
df = pd.read_csv("../data/raw/gfi.csv")

# 2. Convert wide to long
df_long = pd.melt(
    df,
    id_vars=["Country Name", "Country Code", "Series Name", "Series Code"],
    var_name="Year",
    value_name="Value"
)

# 3. Clean Year column
df_long["Year"] = df_long["Year"].str.extract(r'(\d{4})').astype(int)

# 4. Convert 'Value' to numeric
df_long["Value"] = pd.to_numeric(df_long["Value"], errors="coerce")

# 5. Pivot to wide format
df_pivot = df_long.pivot_table(
    index=["Country Name", "Country Code", "Year"],
    columns="Series Code",
    values="Value"
).reset_index()

# 6. Preview
print(df_pivot.head())