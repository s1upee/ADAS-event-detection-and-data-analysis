import pandas as pd
import numpy as np
import os
import time

# Define the data directory
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(script_dir, "../data"))

# Ensure the data directory exists
if not os.path.exists(data_dir):
    raise FileNotFoundError(f"Error: Data directory '{data_dir}' not found.")

# Wait for the file system to sync
time.sleep(2)

# Use the symlinked dataset
dataset_path = os.path.join(data_dir, "adas_data.csv")

# Ensure the dataset exists
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Error: Dataset '{dataset_path}' not found. Run generate_synthetic_data.py first.")

print(f"✅ Using dataset: {dataset_path}")

# Load the dataset
try:
    data = pd.read_csv(dataset_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: {dataset_path} not found. Please check if the dataset exists.")
    exit()

# Display basic information
print("\nInitial Data Sample:\n", data.head())

# Handling missing values
data.ffill(inplace=True)  # Forward fill for consistency
data.dropna(inplace=True)  # Drop any remaining null values

# Convert timestamps to datetime format
if 'timestamp' in data.columns:
    data['timestamp'] = pd.to_datetime(data['timestamp'])

# Remove duplicate rows
data.drop_duplicates(inplace=True)

# Standardizing numeric data
numeric_cols = ['speed', 'acceleration', 'braking_force', 'steering_angle']
for col in numeric_cols:
    if col in data.columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')

# Output cleaned data sample
print("\nCleaned Data Sample:\n", data.head())

# Save the cleaned dataset
output_file = os.path.join(data_dir, "cleaned_adas_data.csv")
data.to_csv(output_file, index=False)
print(f"\n✅ Cleaned dataset saved to: {output_file}")
