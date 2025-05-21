import pandas as pd
import os

# [1] Set file path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(project_root, 'data', 'raw', 'gfi.csv')

# [2] Load data
df = pd.read_csv(raw_data_path)

# [3] Target indicators to filter
target_indicators = [
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
    "Owns a debit or credit card (% age 15+)",
    "Owns a debit or credit card, female (% age 15+)",
    "Owns a debit or credit card, male (% age 15+)",
    "Owns a debit or credit card, rural (% age 15+)",
    "Owns a debit or credit card, urban (% age 15+)",
    "Made a digital payment (% age 15+)",
    "Made a digital payment, female (% age 15+)",
    "Made a digital payment, male (% age 15+)",
    "Made a digital payment, urban (% age 15+)",
    "Made a digital payment, rural (% age 15+)",
    "Made a digital merchant payment (% age 15+)",
    "Made a digital merchant payment, female (% age 15+)",
    "Made a digital merchant payment, male (% age 15+)",
    "Made a digital merchant payment, urban (% age 15+)",
    "Made a digital merchant payment, rural (% age 15+)",
    "Made a digital in-store merchant payment (age 15+)",
    "Made a digital in-store merchant payment: using a mobile phone (% age 15+)",
    "Made a digital in-store merchant payment: using a mobile phone, female (% age 15+)",
    "Made a digital in-store merchant payment: using a mobile phone, male (% age 15+)",
    "Made a digital in-store merchant payment: using a mobile phone, rural (% age 15+)",
    "Made a digital in-store merchant payment: using a mobile phone, urban (% age 15+)",
    "Made a digital online merchant payment for an online purchase (% age 15+)",
    "Made a digital online merchant payment for an online purchase (% of internet purchasers, age 15+)",
    "Made a utility payment (% age 15+)",
    "Made a utility payment, female (% age 15+)",
    "Made a utility payment, male (% age 15+)",
    "Made a utility payment, urban (% age 15+)",
    "Made a utility payment, rural (% age 15+)",
    "Made a utility payment: using a financial institution account (% age 15+)",
    "Made a utility payment: using a mobile phone (% age 15+)",
    "Used a mobile phone or the internet to access a financial institution account (% age 15+)",
    "Used a mobile phone or the internet to access a financial institution account (% with a financial institution account, age 15+)",
    "Used a mobile phone or the internet to access an account (% with an account, age 15+)",
    "Used a mobile phone or the internet to access an account(% age 15+)",
    "Used a mobile phone or the internet to access an account, female (% age 15+)",
    "Used a mobile phone or the internet to access an account, male (% age 15+)",
    "Used a mobile phone or the internet to access an account, rural (% age 15+)",
    "Used a mobile phone or the internet to access an account, urban (% age 15+)",
    "Used a mobile phone or the internet to buy something online (% age 15+)",
    "Used a mobile phone or the internet to buy something online, female (% age 15+)",
    "Used a mobile phone or the internet to buy something online, male (% age 15+)",
    "Used a mobile phone or the internet to buy something online, rural (% age 15+)",
    "Used a mobile phone or the internet to buy something online, urban (% age 15+)",
    "Used a mobile phone or the internet to check account balance(% age 15+)",
    "Used a mobile phone or the internet to check account balance(% with a financial institution account, age 15+)",
    "Used a mobile phone or the internet to send money (% age 15+)",
    "Used a mobile phone or the internet to send money, female (% age 15+)",
    "Used a mobile phone or the internet to send money, male (% age 15+)",
    "Used a mobile phone or the internet to send money, rural (% age 15+)",
    "Used a mobile phone or the internet to send money, urban (% age 15+)",
    "Used a mobile phone or the internet to pay bills, (% age 15+)",
    "Used a mobile phone or the internet to pay bills, female (% age 15+)",
    "Used a mobile phone or the internet to pay bills, male (% age 15+)",
    "Used a mobile phone or the internet to pay bills, rural (% age 15+)",
    "Used a mobile phone or the internet to pay bills, urban (% age 15+)",
    "Use a mobile phone or the internet to make payments, buy things, or to send or receive money using a financial institution account (% age 15+)",
    "Use a mobile phone or the internet to make payments, buy things, or to send or receive money using a financial institution account (% with a financial institution account, age 15+)",
    "Made a deposit (% with a financial institution account, age 15+)",
    "Made a withdrawal (% with a financial institution account, age 15+)",
    "Store money using a financial institution or a mobile money account (% age 15+)",
    "Store money using a financial institution or a mobile money account (% with an account,  age 15+)",
    "Store money using a mobile money account (% age 15+)",
    "Store money using a mobile money account (% with a mobile money account acount, age 15+)",
    "Made or received a digital payment (% age 15+)",
    "Made or received a digital payment, female (% age 15+)",
    "Made or received a digital payment, male (% age 15+)",
    "Made or received a digital payment, rural (% age 15+)",
    "Made or received a digital payment, urban (% age 15+)",
    "Received digital payments (% age 15+)",
    "Received digital payments, female (% age 15+)",
    "Received digital payments, male (% age 15+)",
    "Received digital payments, rural (% age 15+)",
    "Received digital payments, urban (% age 15+)",
    "Saved at a financial institution or using a mobile money account (% age 15+)",
    "Saved at a financial institution or using a mobile money account, female (% age 15+)",
    "Saved at a financial institution or using a mobile money account, male (% age 15+)",
    "Saved at a financial institution or using a mobile money account, rural (% age 15+)",
    "Saved at a financial institution or using a mobile money account, urban (% age 15+)",
    "Saved money using a mobile money account (% age 15+)",
    "Saved money using a mobile money account, female (% age 15+)",
    "Saved money using a mobile money account, male (% age 15+)",
    "Saved money using a mobile money account, rural (% age 15+)",
    "Saved money using a mobile money account, urban (% age 15+)"
]

df_filtered = df[df['Series Name'].isin(target_indicators)]

# [4] Melt wide → long format
df_long = df_filtered.melt(
    id_vars=["Country Name", "Country Code", "Series Name", "Series Code"],
    var_name="date",
    value_name="value"
)

# [5] Rename columns
df_long = df_long.rename(columns={
    'Country Name': 'country',
    'Country Code': 'countryiso3code',
    'Series Name': 'indicator'
})

# [6] Extract only year
df_long['date'] = df_long['date'].str.extract(r'(\d{4})')
df_long = df_long.dropna(subset=['date'])  # remove rows where year extraction failed
df_long['date'] = df_long['date'].astype(int)

# [7] Select needed columns
df_clean = df_long[['country', 'date', 'indicator', 'countryiso3code', 'value']]

# [8] Add required empty columns
df_clean['unit'] = pd.NA
df_clean['obs_status'] = pd.NA
df_clean['decimal'] = 0

# [9] Region classification
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

df_clean['Region'] = df_clean['country'].apply(assign_region)

# ✅ [10] Sort by country → indicator → date
df_clean = df_clean.sort_values(by=['country', 'indicator', 'date'], ascending=[True, True, False])

# [11] Rearrange column order
final_columns = [
    'country', 'date', 'indicator', 'countryiso3code', 'value',
    'unit', 'obs_status', 'decimal', 'Region'
]
df_final = df_clean[final_columns]

# [12] Save to file
processed_path = os.path.join(project_root, 'data', 'processed', 'gfi_final_output.csv')
df_final.to_csv(processed_path, index=False)

print(f"✅ Data successfully transformed and sorted by country → indicator → date. Saved to: {processed_path}")