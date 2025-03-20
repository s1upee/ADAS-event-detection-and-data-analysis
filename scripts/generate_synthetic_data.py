import os
import numpy as np
import pandas as pd
from datetime import datetime

# Define dataset size
num_samples = 5000

# Generate timestamps
timestamps = pd.date_range(start="2025-03-11 08:00:00", periods=num_samples, freq='s')

# Generate synthetic driving data
np.random.seed(42)
road_types = np.random.choice(["urban", "highway", "suburban"], num_samples)
weather_conditions = np.random.choice(["clear", "rain", "fog", "wet"], num_samples)

# Continuous telemetry features
speed = np.random.uniform(30, 120, num_samples)  
gps_speed = speed + np.random.normal(0, 2, num_samples)  
acceleration = np.random.uniform(-3, 3, num_samples)  
yaw_rate = np.random.uniform(-0.5, 0.5, num_samples)  
distance_to_vehicle = np.random.uniform(5, 50, num_samples)  
braking_force = np.random.uniform(0, 1, num_samples)  
steering_angle = np.random.uniform(-15, 15, num_samples)  

# Step 1: Generate synthetic events
event_types = np.random.choice(
    ["None", "Emergency Braking", "Lane Departure", "Harsh Acceleration", "Tailgating Risk"],
    num_samples,
    p=[0.7, 0.1, 0.1, 0.05, 0.05]
)

severity_map = {
    "None": None,
    "Emergency Braking": "Critical",
    "Lane Departure": "Moderate",
    "Harsh Acceleration": "Moderate",
    "Tailgating Risk": "Moderate"
}
severity = [severity_map[event] for event in event_types]

# Step 2: Construct Initial DataFrame
adas_data = pd.DataFrame({
    "timestamp": timestamps,
    "road_type": road_types,
    "weather": weather_conditions,
    "speed": speed,
    "gps_speed": gps_speed,
    "acceleration": acceleration,
    "yaw_rate": yaw_rate,
    "distance_to_vehicle": distance_to_vehicle,
    "braking_force": braking_force,
    "steering_angle": steering_angle,
    "event_type": event_types,
    "severity": severity
})

# Convert timestamp column to datetime
adas_data["timestamp"] = pd.to_datetime(adas_data["timestamp"])

# Step 3: Feature Engineering
adas_data["acceleration_var"] = adas_data["acceleration"].rolling(window=5).std().fillna(0)
adas_data["steering_smoothness"] = adas_data["steering_angle"].rolling(window=5).mean().fillna(0)
adas_data["speed_fluctuation"] = adas_data["speed"].diff().fillna(0)
adas_data["braking_before_event"] = adas_data["braking_force"].shift(1).fillna(0)

# Convert speed (km/h) into cumulative distance traveled (km)
adas_data["cumulative_distance"] = (adas_data["speed"] * (1 / 3600)).cumsum()  

# Compute Jerk (rate of change of acceleration over time) - Fixed!
adas_data["jerk"] = adas_data["acceleration"].diff().fillna(0) / adas_data["timestamp"].diff().dt.total_seconds().fillna(1)

# Create a combined road condition feature
adas_data["road_condition"] = adas_data["road_type"] + "_" + adas_data["weather"]

# Compute time elapsed since the last recorded event
adas_data["time_since_last_event"] = adas_data["timestamp"].diff().dt.total_seconds().fillna(0)

# Step 4: Save the dataset
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
new_filename = f"ml_ready_adas_data_{timestamp_str}.csv"
save_path = os.path.join(data_dir, new_filename)

adas_data.to_csv(save_path, index=False)

# Step 5: Update symbolic link
latest_symlink = os.path.join(data_dir, "ml_ready_adas_data.csv")
if os.path.exists(latest_symlink) or os.path.islink(latest_symlink):
    os.remove(latest_symlink)

os.symlink(os.path.abspath(save_path), os.path.abspath(latest_symlink))  # Ensure full path

print(f"✅ New synthetic ADAS dataset saved as '{save_path}'!")
print(f"🔗 Latest dataset linked as '{latest_symlink}'")

