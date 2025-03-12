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

# Track last 10 speeds for Cruise Control detection
speed_history = []

for i, row in data.iterrows():
    event_type = None
    severity = None
    
    # Sudden Braking
    if row.get("acceleration", 0) < -3:
        event_type = "Sudden Braking"
        severity = "Critical" if row["acceleration"] < -5 else "Moderate"
    
    # Lane Departure
    if abs(row.get("steering_angle", 0)) > 10:
        event_type = "Lane Departure"
        severity = "Critical" if abs(row["steering_angle"]) > 20 else "Moderate"
    
    # Emergency Braking
    if row.get("braking_force", 0) > 0.8:
        event_type = "Emergency Braking"
        severity = "Critical"
    
    # Harsh Acceleration
    if row.get("acceleration", 0) > 3:
        event_type = "Harsh Acceleration"
        severity = "Critical" if row["acceleration"] > 5 else "Moderate"
    
    # Cruise Control Detection (Check if speed is stable for 10+ seconds)
    speed_history.append(row.get("speed", 0))
    if len(speed_history) > 10:
        speed_history.pop(0)
        if max(speed_history) - min(speed_history) <= 2:
            event_type = "Cruise Control Active"
            severity = "None"

    # Tailgating Detection
    if row.get("speed", 0) > 80 and row.get("braking_force", 0) > 0.5:
        event_type = "Tailgating Risk"
        severity = "Moderate"

    # Save detected event
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
