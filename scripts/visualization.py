import pandas as pd
import matplotlib.pyplot as plt
import os

# Define file paths
input_file = "../data/adas_events.csv"
visuals_dir = "../visuals/"

# Ensure visuals directory exists
if not os.path.exists(visuals_dir):
    os.makedirs(visuals_dir)

# Load the ADAS events dataset
try:
    events = pd.read_csv(input_file)
    print("ADAS events dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: {input_file} not found. Please run event_detection.py first.")
    exit()

# Convert timestamp to datetime if not already
if 'timestamp' in events.columns:
    events['timestamp'] = pd.to_datetime(events['timestamp'])

# Plot ADAS Event Timeline
def plot_event_timeline():
    plt.figure(figsize=(10, 5))
    plt.scatter(events['timestamp'], events['event_type'], c='red', alpha=0.6)
    plt.xlabel("Time")
    plt.ylabel("Event Type")
    plt.title("ADAS Events Over Time")
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig(visuals_dir + "event_timeline.png")
    print("Saved: event_timeline.png")

# Plot Braking Force Histogram
def plot_braking_trends():
    plt.figure(figsize=(8, 5))
    events['braking_force'].hist(bins=10, color='blue', alpha=0.7)
    plt.xlabel("Braking Force")
    plt.ylabel("Frequency")
    plt.title("Distribution of Braking Force")
    plt.grid()
    plt.savefig(visuals_dir + "braking_trends.png")
    print("Saved: braking_trends.png")

# Plot Severity Breakdown
def plot_severity_pie_chart():
    plt.figure(figsize=(6, 6))
    severity_counts = events['severity'].value_counts()
    severity_counts.plot.pie(autopct='%1.1f%%', colors=['red', 'orange', 'yellow'], startangle=90)
    plt.title("Distribution of Event Severity")
    plt.ylabel("")
    plt.savefig(visuals_dir + "severity_distribution.png")
    print("Saved: severity_distribution.png")

# Run all visualizations
plot_event_timeline()
plot_braking_trends()
plot_severity_pie_chart()

print("All visualizations saved successfully!")
