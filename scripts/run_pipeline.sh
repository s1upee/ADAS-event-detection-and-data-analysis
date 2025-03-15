#!/bin/bash

echo "🚀 Running the ADAS Event Detection Pipeline..."

# 1️⃣ Generate Synthetic Data
echo "📌 Generating synthetic data..."
python scripts/generate_synthetic_data.py || { echo "❌ Error in data generation"; exit 1; }

# 2️⃣ Process Data
echo "📌 Processing data..."
python scripts/data_processing.py || { echo "❌ Error in data processing"; exit 1; }

# 3️⃣ Detect ADAS Events
echo "📌 Detecting ADAS events..."
python scripts/event_detection.py || { echo "❌ Error in event detection"; exit 1; }

# 4️⃣ Generate Visualizations
echo "📌 Generating visualizations..."
python scripts/visualization.py || { echo "❌ Error in visualization"; exit 1; }

# 5️⃣ Run the Dashboard
echo "📌 Starting the Streamlit dashboard..."
streamlit run scripts/dashboard.py || { echo "❌ Error in dashboard"; exit 1; }

echo "✅ Pipeline executed successfully!"
