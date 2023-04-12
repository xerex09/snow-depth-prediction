import pandas as pd
from sys import exit as quit
import matplotlib.pyplot as plt

df = pd.read_csv('Pluvio_GanjaLa.csv')

#get df shape information
print(df.shape)

#get column information in df
print(df.info())

#peek at the first 5 rows of the df
print(df.head())

#check if datas are missing
print(df.isnull().sum())


plt.plot(df['Date'], df['SnowD'])


## 8349:18240 >> 42K

#df = df.iloc[0:8349]
df = df[["Date","Time","Status_pluvio","Prec","Temp","SnowD","Wind"]]
# df["Date"] = pd.to_datetime(df["Date"])
# df_groupbymonth = df.groupby(df.Date.dt.month)
# print(df.head())


#handle missing data with weighted rolling average
df["Fixed_Prec_spline"] = df['Prec'].interpolate(option='spline')
df["Fixed_Temp_spline"] = df['Temp'].interpolate(option='spline')
df["Fixed_SnowD_spline"] = df['SnowD'].interpolate(option='spline')
df["Fixed_Wind_spline"] = df['Wind'].interpolate(option='spline')

df["Fixed_SnowD_MA"] = df['SnowD'].rolling(window=10, min_periods=1).mean()




# #handle missing data with weighted rolling average
# df["Fixed_Prec_time"] = df['Prec'].interpolate(option='time')
# df["Fixed_Temp_time"] = df['Temp'].interpolate(option='time')
# df["Fixed_SnowD_time"] = df['SnowD'].interpolate(option='time')
# df["Fixed_Wind_time"] = df['Wind'].interpolate(option='time')

# #handle missing data with linear interpolation
# df["Fixed_Prec"] = df['Prec'].interpolate()
# df["Fixed_Temp"] = df['Temp'].interpolate()
# df["Fixed_SnowD"] = df['SnowD'].interpolate()
# df["Fixed_Wind"] = df['Wind'].interpolate()


plt.plot(df['Date'], df['Fixed_SnowD_spline'])
plt.plot(df['Date'], df['Fixed_SnowD_MA'])
plt.show()
quit()

# #get df shape information
# print(df.shape)

# #get column information in df
# print(df.info())

# #peek at the first 5 rows of the df
# print(df.head())

# #check if datas are missing
# print(df.isnull().sum())

# new_df = df.groupby([df['Date']]).mean()
# print(new_df.head())

# #fill the data where there is no data from fixed columns
# new_df.iloc[8349:18240, 1:5] = new_df.iloc[8349:18240, 5:10]



