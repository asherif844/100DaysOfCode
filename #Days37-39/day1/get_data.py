import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/fivethirtyeight/data/master/us-weather-history/KSEA.csv')

df.to_csv('/Users/asherif844/p_v_e/100DaysOfCode/#Days37-39/KSEA.csv')

# print(df.head())
