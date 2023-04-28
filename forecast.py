import pandas as pd
import numpy as np
import statsmodels.api as sm
import os 

root_dir = os.getcwd()
dataset_dir = root_dir+"/dataset/"
data_file = dataset_dir+"Pluvio_GanjaLa.csv"
# Load data
df = pd.read_csv(data_file)

# Convert date and time columns to datetime format
df["datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"])

# Set datetime column as index
df.set_index("datetime", inplace=True)

# Define columns to be used for modeling
cols = ["Prec", "Temp", "SnowD", "Wind"]

train_size = 8349
training_till = 18240
# Split data into train and test sets
train_data = df.iloc[:train_size][cols]
test_data = df.iloc[training_till:][cols]

# Create SARIMA model for each column
models = {}
for col in cols:
    model = sm.tsa.statespace.SARIMAX(train_data[col], order=(1, 0, 0), seasonal_order=(1, 1, 0, 12))
    models[col] = model.fit()

# Make predictions for each column for test period
predictions = {}
for col in cols:
    predictions[col] = models[col].predict(start="2014-01-20", end="2014-05-03")

# Combine predictions with original data
predicted_data = pd.concat(predictions, axis=1)
predicted_data.columns = cols
predicted_data.index.name = "datetime"
predicted_data.reset_index(inplace=True)

# Save predicted data to file
result_file = dataset_dir+"predicted_data.csv"
predicted_data.to_csv(result_file, index=False)

