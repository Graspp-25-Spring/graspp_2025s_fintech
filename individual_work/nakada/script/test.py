import pandas as pd

data = pd.read_csv('data_original/rainfall_data.csv')
states = data['SUBDIVISION'].unique().tolist()
print(states)