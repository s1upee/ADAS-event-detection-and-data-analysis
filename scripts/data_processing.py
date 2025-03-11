import pandas as pd
import numpy as np
import os

# Define file paths
import glob

# Ensure data directory exists
data_dir = "../data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Find the latest dataset dynamically
latest_file = max(glob.glob(os.path.join(data_dir, "adas_data_*.csv")), key=os.path.getctime)

print(f"✅ Using latest dataset: {latest_file}")

# Load the dataset
try:
    data = pd.read_csv(latest_file)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: {latest_file} not found. Please check if the dataset exists.")
    exit()

output_file = "../data/cleaned_adas_data.csv"

# Ensure data directory exists
if not os.path.exists("../data"):
    os.makedirs("../data")

# Load the dataset
try:
    data = pd.read_csv(latest_file)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: {input_file} not found. Please place the dataset in the 'data/' folder.")
    exit()

# Display basic information
print("\nInitial Data Sample:\n", data.head())

# Handling missing values
data.ffill(inplace=True)  # Forward fill for consistency
data.dropna(inplace=True)  # Drop any remaining null values

# Converting timestamps to datetime format
if 'timestamp' in data.columns:
    data['timestamp'] = pd.to_datetime(data['timestamp'])

# Checking for duplicate rows
data.drop_duplicates(inplace=True)

# Standardizing numeric data
numeric_cols = ['speed', 'acceleration', 'braking_force', 'steering_angle']
for col in numeric_cols:
    if col in data.columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')

# Output cleaned data sample
print("\nCleaned Data Sample:\n", data.head())

# Save the cleaned dataset
data.to_csv(output_file, index=False)
print(f"\nCleaned dataset saved to: {output_file}")
