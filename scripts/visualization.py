import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define absolute paths
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(script_dir, "../data"))
visuals_dir = os.path.abspath(os.path.join(script_dir, "../visuals"))
input_file = os.path.join(data_dir, "adas_events.csv")

# Ensure visuals directory exists
if not os.path.exists(visuals_dir):
    os.makedirs(visuals_dir)

# Ensure ADAS events dataset exists
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Error: {input_file} not found. Please run event_detection.py first.")

print(f"✅ Using ADAS events dataset: {input_file}")

# Load dataset
events = pd.read_csv(input_file)
print("ADAS events dataset loaded successfully!")

# Convert timestamp to datetime if needed
if 'timestamp' in events.columns:
    events['timestamp'] = pd.to_datetime(events['timestamp'])

# Generate Visualizations
def plot_event_timeline():
    plt.figure(figsize=(10, 5))
    plt.scatter(events['timestamp'], events['event_type'], c='red', alpha=0.6)
    plt.xlabel("Time")
    plt.ylabel("Event Type")
    plt.title("ADAS Events Over Time")
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig(os.path.join(visuals_dir, "event_timeline.png"))
    print("Saved: visuals/event_timeline.png")

def plot_braking_trends():
    plt.figure(figsize=(8, 5))
    plt.hist(events['braking_force'], bins=20, color='blue', alpha=0.7, edgecolor='black')
    plt.xlabel("Braking Force")
    plt.ylabel("Frequency")
    plt.title("Distribution of Braking Force")
    plt.grid()
    plt.savefig(os.path.join(visuals_dir, "braking_trends.png"))
    print("Saved: visuals/braking_trends.png")

def plot_severity_pie_chart():
    plt.figure(figsize=(6, 6))
    severity_counts = events['severity'].value_counts()
    severity_counts.plot.pie(autopct='%1.1f%%', colors=['red', 'orange', 'yellow'], startangle=90)
    plt.title("Distribution of Event Severity")
    plt.ylabel("")
    plt.savefig(os.path.join(visuals_dir, "severity_distribution.png"))
    print("Saved: visuals/severity_distribution.png")

def plot_lane_departure():
    plt.figure(figsize=(10, 5))
    plt.plot(events['timestamp'], events['steering_angle'], color='purple', alpha=0.7)
    plt.xlabel("Time")
    plt.ylabel("Steering Angle")
    plt.title("Lane Departure Trends")
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig(os.path.join(visuals_dir, "lane_departure_trends.png"))
    print("Saved: visuals/lane_departure_trends.png")

def plot_speed_vs_braking():
    plt.figure(figsize=(8, 5))
    plt.scatter(events['speed'], events['braking_force'], alpha=0.6, color='blue', edgecolors='black')
    plt.xlabel("Speed (km/h)")
    plt.ylabel("Braking Force")
    plt.title("Speed vs Braking Force")
    plt.grid()
    plt.savefig(os.path.join(visuals_dir, "speed_vs_braking.png"))
    print("Saved: visuals/speed_vs_braking.png")

def plot_event_heatmap():
    events['hour'] = events['timestamp'].dt.hour  # Extract hour from timestamp
    pivot_table = events.pivot_table(index='hour', columns='event_type', aggfunc='size', fill_value=0)
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, cmap='coolwarm', annot=True, fmt="d")
    plt.xlabel("Event Type")
    plt.ylabel("Hour of Day")
    plt.title("Event Occurrence Heatmap")
    plt.savefig(os.path.join(visuals_dir, "event_heatmap.png"))
    print("Saved: visuals/event_heatmap.png")

# Run all visualizations
plot_event_timeline()
plot_braking_trends()
plot_severity_pie_chart()
plot_lane_departure()
plot_speed_vs_braking()
plot_event_heatmap()

print("✅ All visualizations saved successfully in 'visuals/' directory!")
