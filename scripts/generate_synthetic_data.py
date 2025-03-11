import pandas as pd
import numpy as np
import os
import glob
from datetime import datetime

# Set random seed for reproducibility
np.random.seed(42)

# Generate timestamps (simulating 1 hour of driving, 1 data point per second)
num_samples = 3600  # 1 hour of data
timestamps = pd.date_range(start="2025-03-11 08:00:00", periods=num_samples, freq='s')

# Generate speed values (fluctuating between 0 and 120 km/h)
speed = np.clip(np.random.normal(loc=80, scale=15, size=num_samples), 0, 120)

# Generate acceleration values (random fluctuations with occasional hard braking)
acceleration = np.random.normal(loc=0, scale=1.5, size=num_samples)
hard_braking_indices = np.random.choice(num_samples, size=30, replace=False)
acceleration[hard_braking_indices] = np.random.uniform(-5, -8, size=30)  # Hard braking events

# Generate braking force (correlating with hard braking events)
braking_force = np.zeros(num_samples)
braking_force[hard_braking_indices] = np.random.uniform(0.8, 1.0, size=30)

# Generate steering angles (normal driving vs. occasional sharp turns)
steering_angle = np.random.normal(loc=0, scale=5, size=num_samples)
sharp_turn_indices = np.random.choice(num_samples, size=25, replace=False)
steering_angle[sharp_turn_indices] = np.random.uniform(-30, 30, size=25)  # Lane departure events

# Generate ADAS event types
event_types = np.array(["None"] * num_samples, dtype=object)
event_types[hard_braking_indices] = "Emergency Braking"
event_types[sharp_turn_indices] = "Lane Departure"

# Generate severity levels based on event types
severity = np.array(["None"] * num_samples, dtype=object)
severity[hard_braking_indices] = "Critical"
severity[sharp_turn_indices] = "Moderate"

# Create DataFrame
adas_data = pd.DataFrame({
    "timestamp": timestamps,
    "speed": speed,
    "acceleration": acceleration,
    "braking_force": braking_force,
    "steering_angle": steering_angle,
    "event_type": event_types,
    "severity": severity
})

# Ensure data directory exists
data_dir = os.path.join(os.path.dirname(__file__), "../data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Generate a unique filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
new_filename = f"adas_data_{timestamp}.csv"

# Save the dataset with the new filename
save_path = os.path.join(data_dir, new_filename)
adas_data.to_csv(save_path, index=False)

# Update latest dataset link
latest_symlink = os.path.join(data_dir, "adas_data.csv")
if os.path.exists(latest_symlink):
    os.remove(latest_symlink)
os.symlink(new_filename, latest_symlink)

print(f"✅ New synthetic ADAS dataset saved as '{save_path}'!")
