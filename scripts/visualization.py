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

# Convert timestamp to datetime
if 'timestamp' in events.columns:
    events['timestamp'] = pd.to_datetime(events['timestamp'])

# Define severity colors
severity_colors = {"Critical": "red", "Moderate": "orange", "None": "green"}

# 📌 **Enhanced Event Timeline Plot**
def plot_event_timeline():
    plt.figure(figsize=(12, 6))
    colors = events["severity"].map(severity_colors)
    plt.scatter(events["timestamp"], events["event_type"], c=colors, s=80, alpha=0.7, edgecolors="black")
    plt.xlabel("Time")
    plt.ylabel("Event Type")
    plt.title("ADAS Events Over Time (Colored by Severity)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig(os.path.join(visuals_dir, "event_timeline.png"))
    print("Saved: visuals/event_timeline.png")

# 📌 **Enhanced Braking Force Distribution (KDE Plot)**
def plot_braking_trends():
    plt.figure(figsize=(10, 5))
    sns.kdeplot(events["braking_force"], fill=True, color="blue", alpha=0.6)
    plt.xlabel("Braking Force")
    plt.ylabel("Density")
    plt.title("Smoothed Distribution of Braking Force")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig(os.path.join(visuals_dir, "braking_trends.png"))
    print("Saved: visuals/braking_trends.png")

# 📌 **New: Event Severity Over Time**
def plot_severity_over_time():
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=events, x="timestamp", y="severity", hue="event_type", marker="o", palette="coolwarm", alpha=0.7)
    plt.xlabel("Time")
    plt.ylabel("Severity Level")
    plt.title("ADAS Event Severity Over Time")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig(os.path.join(visuals_dir, "severity_over_time.png"))
    print("Saved: visuals/severity_over_time.png")

# 📌 **Improved Event Heatmap**
def plot_event_heatmap():
    events["hour"] = events["timestamp"].dt.hour  # Extract hour from timestamp
    pivot_table = events.pivot_table(index="hour", columns="event_type", aggfunc="size", fill_value=0)

    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot_table, cmap="coolwarm", annot=True, fmt="d", linewidths=0.5)
    plt.xlabel("Event Type")
    plt.ylabel("Hour of Day")
    plt.title("Event Occurrence Heatmap")
    plt.savefig(os.path.join(visuals_dir, "event_heatmap.png"))
    print("Saved: visuals/event_heatmap.png")

# 📌 **Improved Speed vs. Braking Force Scatter Plot**
def plot_speed_vs_braking():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=events["speed"], y=events["braking_force"], hue=events["event_type"], style=events["severity"], palette="coolwarm", s=100, edgecolor="black")
    plt.xlabel("Speed (km/h)")
    plt.ylabel("Braking Force")
    plt.title("Speed vs Braking Force (Colored by Event Type & Severity)")
    plt.legend(title="Event Type", bbox_to_anchor=(1, 1), loc="upper left")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig(os.path.join(visuals_dir, "speed_vs_braking.png"))
    print("Saved: visuals/speed_vs_braking.png")

# 📌 **Run All Visualizations**
plot_event_timeline()
plot_braking_trends()
plot_severity_over_time()
plot_event_heatmap()
plot_speed_vs_braking()

print("✅ All improved visualizations saved in 'visuals/' directory!")
