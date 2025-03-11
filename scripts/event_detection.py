import pandas as pd
import os

import pandas as pd
import os

# Define absolute paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(script_dir, "../data"))
input_file = os.path.join(data_dir, "cleaned_adas_data.csv")
output_file = os.path.join(data_dir, "adas_events.csv")

# Ensure the dataset exists
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Error: {input_file} not found. Please run data_processing.py first.")

print(f"✅ Using cleaned dataset: {input_file}")

# Load the cleaned dataset
data = pd.read_csv(input_file)
print("Cleaned dataset loaded successfully!")

# Detect ADAS events
EVENTS = []

for i, row in data.iterrows():
    event_type = None
    severity = None
    
    # Sudden braking event
    if row.get("acceleration", 0) < -3:
        event_type = "Sudden Braking"
        severity = "Critical" if row["acceleration"] < -5 else "Moderate"
    
    # Lane departure warning (steering angle change > 10 degrees within one frame)
    if abs(row.get("steering_angle", 0)) > 10:
        event_type = "Lane Departure"
        severity = "Critical" if abs(row["steering_angle"]) > 20 else "Moderate"
    
    # ADAS intervention detection (e.g., emergency braking)
    if row.get("braking_force", 0) > 0.8:
        event_type = "Emergency Braking"
        severity = "Critical"
    
    if event_type:
        EVENTS.append({
            "timestamp": row["timestamp"],
            "event_type": event_type,
            "severity": severity,
            "speed": row.get("speed", "N/A"),
            "acceleration": row.get("acceleration", "N/A"),
            "braking_force": row.get("braking_force", "N/A"),
            "steering_angle": row.get("steering_angle", "N/A"),
        })

# Convert detected events into a DataFrame
events_df = pd.DataFrame(EVENTS)

# Save to CSV
events_df.to_csv(output_file, index=False)
print(f"✅ ADAS events saved to: {output_file}")

# Display sample output
print("\nDetected Events Sample:")
print(events_df.head())
