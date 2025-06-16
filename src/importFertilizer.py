import pandas as pd
fileName = 'Data/raw/fertilizer_FUCB_raw.csv'

df_fertilizer = pd.read_csv(fileName)
# Filter for specific countries in South Asia and Southeast Asia
country_list = ['AFG', 'BGD', 'BRN', 'BTN', 'IDN', 'IND', 'IRN', 'KHM', 'LAO',
                'LKA', 'MDV', 'MMR', 'MYS', 'NPL', 'PAK', 'PHL', 'SGP', 'THA',
                'TLS', 'VNM', 'WLD']

# Filter the DataFrame to include only the specified countries
# Convert 'ISO3_code' to country
df_fertilizer = df_fertilizer[df_fertilizer['ISO3_code'].isin(country_list)]
df_fertilizer = df_fertilizer.drop(columns=['Country'])
df_fertilizer = df_fertilizer.rename(columns={'ISO3_code': 'country'})

# Convert 'Year' to a consistent format
df_fertilizer['Year'] = df_fertilizer['Year'].transform(lambda x: (
    1989 if x == '1989/90' else
    1990 if x == '1990/91' else
    1991 if x == '1991/92' else
    1992 if x == '1992/93' else
    1997 if x == '1997-98' else
    1998 if x == '1998/99' else
    x
))

# Group by 'country' and 'Year', then sum 'Crop_area_k_ha' and 'N_k_t'
df_fertilizer = df_fertilizer.groupby(['country', 'Year'], as_index=False)[
    ['Crop_area_k_ha', 'N_k_t']].sum()

df_fertilizer['nitrogen_ha'] = df_fertilizer['N_k_t'] / \
    df_fertilizer['Crop_area_k_ha']
df_fertilizer = df_fertilizer.rename(
    columns={'Crop_area_k_ha': 'crop_area_kha', 'N_k_t': 'nitrogen_t'})

print(df_fertilizer.head(20))
df_fertilizer.to_csv(
    'Data/processed/fertilizer_FUCB_processed.csv', index=False)
# Save the processed DataFrame to a CSV file
