import pandas as pd
from sys import exit as quit
import matplotlib.pyplot as plt
import os 

root_dir = os.getcwd()
dataset_dir = root_dir+"/dataset/"
data_file = dataset_dir+"Pluvio_GanjaLa.csv"
fixed_data_file = dataset_dir+"predicted_data.csv"
df = pd.read_csv(fixed_data_file)


#get df shape information
print(df.shape)

#get column information in df
print(df.info())

#peek at the first 5 rows of the df
print(df.head())

#check if datas are missing
print(df.isnull().sum())

# group the data by date 
# Date for Original file and datetime for predicted file
df['Date'] = pd.to_datetime(df['datetime']).dt.date  # for predicted file
df_daily = df.groupby('Date').mean()

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




