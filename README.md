# 🚗 ADAS Event Detection and Data Analysis

## Overview
This project focuses on Advanced Driver Assistance Systems (ADAS) event detection and data analysis using Python. The workflow includes:

- **Synthetic Data Generation**: Creates a dataset with realistic vehicle telemetry.
- **Data Processing**: Cleans and formats raw ADAS data.
- **Event Detection**: Identifies driving events such as lane departures, harsh braking, and tailgating risks.
- **Advanced Event Classification**: Enhances event detection by categorizing risks more accurately.
- **Data Visualization**: Generates insightful charts to analyze driving trends.
- **Interactive Dashboard**: Provides a real-time interface to explore ADAS events using Streamlit.

## 📂 Project Structure
```
📦 ADAS Event Detection and Data Analysis
 ┣ 📂 data
 ┃ ┣ 📜 adas_data.csv
 ┃ ┣ 📜 cleaned_adas_data.csv
 ┃ ┣ 📜 adas_events.csv
 ┣ 📂 notebooks
 ┣ 📂 reports
 ┣ 📂 scripts
 ┃ ┣ 📜 generate_synthetic_data.py
 ┃ ┣ 📜 data_processing.py
 ┃ ┣ 📜 event_detection.py
 ┃ ┣ 📜 visualization.py
 ┃ ┣ 📜 dashboard.py
 ┣ 📂 visuals
 ┃ ┣ 📜 braking_trends.png
 ┃ ┣ 📜 event_heatmap.png
 ┃ ┣ 📜 event_timeline.png
 ┃ ┣ 📜 lane_departure_trends.png
 ┃ ┣ 📜 severity_distribution.png
 ┃ ┣ 📜 severity_over_time.png
 ┃ ┣ 📜 speed_vs_braking.png
 ┣ 📜 README.md
```

## 🚀 Setup and Usage
### 1️⃣ Install Dependencies
Ensure you have Python installed, then install required packages:
```bash
pip install -r requirements.txt
```

### 2️⃣ Generate Synthetic Data
Run the script to create a realistic ADAS dataset:
```bash
python scripts/generate_synthetic_data.py
```

### 3️⃣ Process Data
Clean and preprocess the generated dataset:
```bash
python scripts/data_processing.py
```

### 4️⃣ Detect ADAS Events
Analyze the processed data and detect key ADAS events:
```bash
python scripts/event_detection.py
```

### 5️⃣ Visualize Data
Generate graphical insights based on detected events:
```bash
python scripts/visualization.py
```

### 6️⃣ Launch Interactive Dashboard
Explore ADAS events interactively using Streamlit:
```bash
streamlit run scripts/dashboard.py
```

## 📊 Advanced Event Classification
Recent updates have enhanced the accuracy of event detection by incorporating:
- **Tailgating Detection**: Identifies vehicles driving too close.
- **Harsh Acceleration Detection**: Flags rapid speed increases.
- **Severe Lane Departure Detection**: Detects dangerous steering angles.
- **Sudden Braking Events**: Differentiates between normal and emergency braking.

## 📈 Data Visualizations
The system generates various insightful charts, including:
- **Braking Trends**: Tracks braking intensity over time.
- **Severity Over Time**: Highlights the frequency of severe driving events.
- **Event Heatmap**: Shows when ADAS events occur most frequently.
- **Lane Departure Trends**: Detects patterns in unsafe lane changes.
- **Speed vs. Braking**: Analyzes speed correlation with emergency braking.

## 🛠️ Future Improvements
- Enhance dashboard interactivity with filtering and real-time updates.
- Expand dataset with more driving scenarios.
- Integrate machine learning for predictive analytics.

---
## 📩 Contact
 If you have any questions, feel free to reach out! 😊  
 🔗 **GitHub**: [s1upee](https://github.com/s1upee)  
 🔗 **Email**: lisakrasiuk@gmail.com

🎯 **Status:** Ongoing Development 🚀
