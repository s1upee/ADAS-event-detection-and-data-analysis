# ADAS (Advanced Driver Assistance System) Event Detection and Data Analysis

🚗 **Project Status: In Progress** 🚗

## 📌 Overview
This project aims to develop a Python-based data processing system for analyzing ADAS event logs, such as lane departure warnings, automatic braking events, and adaptive cruise control activations. The system processes vehicle telemetry data, detects ADAS-related events such as sudden braking, lane departures, and emergency braking, and stores them in `adas_events.csv` for further analysis.

## 📅 Estimated Completion: 1-2 Days

## 📂 Project Structure
```
ADAS_Event_Detection/
│── data/                  # Folder for datasets
│   ├── adas_data.csv      # Raw ADAS telemetry data
│   ├── cleaned_adas_data.csv  # Processed dataset
│   ├── adas_events.csv    # Detected ADAS events
│
│── notebooks/             # Jupyter Notebooks (if using Jupyter)
│   ├── analysis.ipynb     # Notebook for data processing and visualization
│
│── scripts/               # Python scripts for each task
│   ├── data_processing.py # Script for data cleaning
│   ├── event_detection.py # Script for detecting ADAS events
│   ├── visualization.py   # Script for graphing and reporting
│
│── reports/               # Final analysis reports
│   ├── summary_report.pdf # Key insights and conclusions
│
│── visuals/               # Folder for images and graphs
│   ├── event_trends.png   # Example visualization output
│
│── README.md              # Project description and instructions
│── requirements.txt       # Dependencies (Pandas, NumPy, Matplotlib, etc.)
│── .gitignore             # Ignore unnecessary files
```

## 🛠 Technologies Used
- **Python** (Pandas, NumPy, Matplotlib, Plotly)
- **Jupyter Notebook / VS Code** for scripting and visualization
- **CSV** datasets for vehicle telemetry & ADAS logs

## ✅ Progress So Far
- [x] **Data Processing & Cleaning** (Handling missing values, standardizing data)
- [x] **Event Detection & Analysis** (Detected braking events, lane departures, and emergency braking)
- [ ] **Data Visualization & Reporting** (Graphs, summary reports)

## 🔜 Next Steps
- Visualize ADAS event activations over time
- Identify trends in braking, lane deviation, and system interventions
- Generate summary insights and recommendations

🚀 Stay tuned for updates! 🚀

## 📩 Contact
If you have any questions, feel free to reach out! 😊  
🔗 **GitHub**: [s1upee](https://github.com/s1upee)  
🔗 **Email**: lisakrasiuk@gmail.com
