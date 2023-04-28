import pandas as pd
from sys import exit as quit
import matplotlib.pyplot as plt

df = pd.read_csv('predicted_data.csv')


#get df shape information
print(df.shape)

#get column information in df
print(df.info())

#peek at the first 5 rows of the df
print(df.head())

#check if datas are missing
print(df.isnull().sum())

# group the data by date
df_daily = df.groupby('datetime').mean()

# plot the data
plt.figure(figsize=(10, 5))
plt.plot(df_daily['Prec'], label='Prec')
plt.plot(df_daily['Temp'], label='Temp')
plt.plot(df_daily['SnowD'], label='SnowD')
plt.plot(df_daily['Wind'], label='Wind')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()




