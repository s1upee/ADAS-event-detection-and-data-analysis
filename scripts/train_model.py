import pandas as pd
import numpy as np
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import RandomOverSampler

# Define paths
data_dir = "data"
train_file = os.path.join(data_dir, "train.csv")
test_file = os.path.join(data_dir, "test.csv")
model_file = os.path.join(data_dir, "adas_model.pkl")

# Ensure train and test datasets exist
if not os.path.exists(train_file) or not os.path.exists(test_file):
    raise FileNotFoundError("Error: Training or test data not found. Run data_processing.py first.")

print(f"✅ Using training set: {train_file}")
print(f"✅ Using test set: {test_file}")

# Load train & test datasets
train_data = pd.read_csv(train_file)
test_data = pd.read_csv(test_file)

# Define Features & Target
feature_columns = [
    "speed", "gps_speed", "acceleration", "yaw_rate",
    "distance_to_vehicle", "braking_force", "steering_angle",
    "acceleration_var", "steering_smoothness", "speed_fluctuation",
    "braking_before_event"
]
target_column = "event_type"

# Extract features & labels
X_train, y_train = train_data[feature_columns], train_data[target_column]
X_test, y_test = test_data[feature_columns], test_data[target_column]

# Convert Categorical Target to Numbers
class_mapping = {label: idx for idx, label in enumerate(y_train.unique())}
y_train = y_train.map(class_mapping)
y_test = y_test.map(class_mapping)

# Apply Oversampling
ros = RandomOverSampler(random_state=42)
X_train, y_train = ros.fit_resample(X_train, y_train)

# Train Random Forest Model
print("📌 Training Random Forest Classifier...")
rf_model = RandomForestClassifier(
    n_estimators=300,   # More trees
    max_depth=10,       # Control overfitting
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42)
rf_model.fit(X_train, y_train)

# Train XGBoost Model
print("📌 Training XGBoost Classifier...")
xgb_model = XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,  # Reduce learning rate
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42)
xgb_model.fit(X_train, y_train)

# Evaluate Models
rf_preds = rf_model.predict(X_test)
xgb_preds = xgb_model.predict(X_test)

rf_acc = accuracy_score(y_test, rf_preds)
xgb_acc = accuracy_score(y_test, xgb_preds)

print(f"✅ Random Forest Accuracy: {rf_acc:.4f}")
print(f"✅ XGBoost Accuracy: {xgb_acc:.4f}")

print("\n📌 Random Forest Classification Report:")
print(classification_report(y_test, rf_preds, target_names=class_mapping.keys()))

print("\n📌 XGBoost Classification Report:")
print(classification_report(y_test, xgb_preds, target_names=class_mapping.keys()))

# Save Best Model
best_model = rf_model if rf_acc > xgb_acc else xgb_model
joblib.dump(best_model, model_file)

print(f"✅ Best model saved as: {model_file}")
