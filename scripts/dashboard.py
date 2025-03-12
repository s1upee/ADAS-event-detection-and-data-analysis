import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define file paths
DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/adas_events.csv")

# Load data
@st.cache_data
def load_data():
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    else:
        return None

# Streamlit UI
st.set_page_config(page_title="ADAS Dashboard", layout="wide")

st.title("🚗 ADAS Event Detection Dashboard")
st.sidebar.header("🔍 Filter Events")

# Load dataset
data = load_data()

if data is not None:
    # Filter by event type
    event_types = st.sidebar.multiselect("Select Event Type:", data["event_type"].unique(), default=data["event_type"].unique())
    filtered_data = data[data["event_type"].isin(event_types)]

    # Filter by severity
    severities = st.sidebar.multiselect("Select Severity:", data["severity"].unique(), default=data["severity"].unique())
    filtered_data = filtered_data[filtered_data["severity"].isin(severities)]

    # 📌 **1. Display Event Summary Table**
    st.subheader("📋 ADAS Events Summary")
    st.dataframe(filtered_data)

    # 📌 **2. Interactive Event Timeline**
    st.subheader("⏳ Event Timeline")
    fig, ax = plt.subplots(figsize=(12, 4))
    colors = {"Critical": "red", "Moderate": "orange", "None": "green"}
    ax.scatter(filtered_data["timestamp"], filtered_data["event_type"], c=filtered_data["severity"].map(colors), alpha=0.7, edgecolors="black")
    ax.set_xlabel("Time")
    ax.set_ylabel("Event Type")
    ax.set_title("ADAS Events Over Time")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    st.pyplot(fig)

    # 📌 **3. Speed vs Braking Force**
    st.subheader("⚡ Speed vs. Braking Force")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=filtered_data, x="speed", y="braking_force", hue="event_type", style="severity", palette="coolwarm", s=100, edgecolor="black", ax=ax)
    ax.set_xlabel("Speed (km/h)")
    ax.set_ylabel("Braking Force")
    ax.set_title("Relationship Between Speed & Braking Force")
    plt.grid(True, linestyle="--", alpha=0.6)
    st.pyplot(fig)

    # 📌 **4. Event Heatmap**
    st.subheader("🔥 Event Occurrence Heatmap")
    data["hour"] = data["timestamp"].dt.hour
    pivot_table = data.pivot_table(index="hour", columns="event_type", aggfunc="size", fill_value=0)
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.heatmap(pivot_table, cmap="coolwarm", annot=True, fmt="d", linewidths=0.5, ax=ax)
    ax.set_xlabel("Event Type")
    ax.set_ylabel("Hour of Day")
    ax.set_title("Event Heatmap (Frequency by Hour)")
    st.pyplot(fig)

    # 📌 **5. Upload Custom ADAS Data**
    st.sidebar.subheader("📂 Upload New ADAS Data")
    uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])
    if uploaded_file:
        new_data = pd.read_csv(uploaded_file)
        st.sidebar.success("✅ New dataset uploaded!")
        st.write("📋 Preview of Uploaded Data:")
        st.dataframe(new_data)

else:
    st.error("⚠ No ADAS event data found! Run `event_detection.py` first.")

st.sidebar.markdown("---")
st.sidebar.info("Built with ❤️ using Streamlit.")
