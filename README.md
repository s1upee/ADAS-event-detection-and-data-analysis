# ADAS (Advanced Driver Assistance System) Event Detection and Data Analysis

🚗 **Project Status: Completed** 🚗

## 📌 Overview
This project develops a **Python-based data processing system** to analyze ADAS event logs such as **lane departure warnings, emergency braking events, and adaptive cruise control activations**. The system processes real or simulated vehicle telemetry data, detects ADAS-related events, and generates meaningful visualizations.

## 📅 Project Duration: 2-3 Days

## 📂 Project Structure
```
ADAS_Event_Detection/
│️── data/                  # Folder for datasets
│️   ├─ adas_data.csv      # Symlink to the latest generated dataset
│️   ├─ adas_data_YYYYMMDD_HHMMSS.csv  # Raw ADAS telemetry data (with timestamp)
│️   ├─ cleaned_adas_data.csv  # Preprocessed and standardized dataset
│️   └─ adas_events.csv    # Detected ADAS events
│️
│️── scripts/               # Python scripts for each task
│️   ├─ generate_synthetic_data.py  # Generates ADAS dataset
│️   ├─ data_processing.py          # Cleans and processes vehicle data
│️   ├─ event_detection.py          # Identifies significant ADAS events
│️   └─ visualization.py            # Generates visual reports
│️
│️── visuals/               # Generated graphs and reports
│️   ├─ event_timeline.png   # ADAS events over time
│️   ├─ braking_trends.png   # Braking force distribution
│️   ├─ severity_distribution.png  # Event severity breakdown
│️   ├─ lane_departure_trends.png  # Lane deviation trends
│️   ├─ speed_vs_braking.png  # Speed correlation with braking force
│️   └─ event_heatmap.png  # ADAS event occurrence heatmap
│️
│️── README.md              # Project description and instructions
│️── requirements.txt       # Dependencies (Pandas, NumPy, Matplotlib, etc.)
│️── .gitignore             # Ignore unnecessary files
```

## 🛠 Technologies Used
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Jupyter Notebook / VS Code** for scripting and visualization
- **CSV** datasets for vehicle telemetry & ADAS logs

## ✅ **Project Progress**
- ✅ **Data Processing & Cleaning** (Handled missing values, standardized data)
- ✅ **Event Detection & Analysis** (Detected braking events, lane departures, and emergency braking)
- ✅ **Data Visualization & Reporting** (Graphs, summary insights, and event severity tracking)

## 📊 **Key Insights**
- Emergency braking events are most frequent during **sudden speed drops**.
- Lane departures show a correlation with **high-speed sharp turns**.
- Braking force peaks correlate with **high-speed interventions** by ADAS.

## 🔜 Next Steps
- Further refine ADAS event classification based on real-world datasets.
- Apply machine learning techniques to predict potential **ADAS interventions**.
- Improve visualization clarity for event severity analysis.

🚀 **Project Completed! Ready for Review & Deployment!** 🚀

## 📩 Contact
If you have any questions, feel free to reach out! 😊  
🔗 **GitHub**: [s1upee](https://github.com/s1upee)  
🔗 **Email**: lisakrasiuk@gmail.com
