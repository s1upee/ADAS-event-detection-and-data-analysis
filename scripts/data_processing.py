import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load latest dataset
data_dir = "data"
input_file = os.path.join(data_dir, "ml_ready_adas_data.csv")
output_train = os.path.join(data_dir, "train.csv")
output_test = os.path.join(data_dir, "test.csv")

if not os.path.exists(input_file):
    raise FileNotFoundError(f"Error: {input_file} not found. Run generate_synthetic_data.py first.")

print(f"✅ Using dataset: {input_file}")

# Load dataset
data = pd.read_csv(input_file)
data["timestamp"] = pd.to_datetime(data["timestamp"])

# 🔥 Select Features and Target Variable
feature_columns = [
    "speed", "gps_speed", "acceleration", "yaw_rate",
    "distance_to_vehicle", "braking_force", "steering_angle",
    "acceleration_var", "steering_smoothness", "speed_fluctuation",
    "braking_before_event"
]
target_column = "event_type"  # Predicting ADAS events

# Drop rows where event_type is missing
data = data.dropna(subset=[target_column])

# Convert categorical variables (road_type, weather) into dummy variables
data = pd.get_dummies(data, columns=["road_type", "weather"], drop_first=True)

# 🔹 Apply MinMaxScaler (0 to 1) for most features
minmax_features = ["speed", "gps_speed", "acceleration", "distance_to_vehicle",
                   "braking_force", "acceleration_var", "steering_smoothness",
                   "speed_fluctuation", "braking_before_event"]

scaler_minmax = MinMaxScaler()
data[minmax_features] = scaler_minmax.fit_transform(data[minmax_features])

# 🔹 Apply StandardScaler (Z-score) for yaw_rate & steering_angle
std_features = ["yaw_rate", "steering_angle"]
scaler_std = StandardScaler()
data[std_features] = scaler_std.fit_transform(data[std_features])

# 🔹 Split Data (80% Train, 20% Test)
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42, stratify=data[target_column])

# Save processed datasets
train_data.to_csv(output_train, index=False)
test_data.to_csv(output_test, index=False)

print(f"✅ Training set saved: {output_train}")
print(f"✅ Test set saved: {output_test}")
