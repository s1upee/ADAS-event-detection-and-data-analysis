import pandas as pd
import numpy as np
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report

# Load Processed Data
data_dir = "data"
train_file = os.path.join(data_dir, "train.csv")
test_file = os.path.join(data_dir, "test.csv")
model_file = os.path.join(data_dir, "adas_model.pkl")

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

# ✅ Hyperparameter Tuning for XGBoost
xgb_params = {
    "n_estimators": [100, 300, 500],
    "learning_rate": [0.01, 0.1, 0.2],
    "max_depth": [3, 5, 7],
    "subsample": [0.8, 1.0],
}
xgb_model = XGBClassifier(random_state=42)
xgb_search = RandomizedSearchCV(xgb_model, xgb_params, n_iter=10, cv=3, scoring="accuracy", verbose=1, random_state=42)
xgb_search.fit(X_train, y_train)
best_xgb = xgb_search.best_estimator_

# ✅ Train LightGBM Model
print("📌 Training LightGBM Classifier...")
lgbm_model = LGBMClassifier(n_estimators=300, learning_rate=0.1, max_depth=5, random_state=42)
lgbm_model.fit(X_train, y_train)

# ✅ Evaluate Models
xgb_preds = best_xgb.predict(X_test)
lgbm_preds = lgbm_model.predict(X_test)

xgb_acc = accuracy_score(y_test, xgb_preds)
lgbm_acc = accuracy_score(y_test, lgbm_preds)

print(f"✅ XGBoost Accuracy: {xgb_acc:.4f}")
print(f"✅ LightGBM Accuracy: {lgbm_acc:.4f}")

print("\n📌 XGBoost Classification Report:")
print(classification_report(y_test, xgb_preds, target_names=class_mapping.keys()))

print("\n📌 LightGBM Classification Report:")
print(classification_report(y_test, lgbm_preds, target_names=class_mapping.keys()))

# ✅ Save Best Model
best_model = best_xgb if xgb_acc > lgbm_acc else lgbm_model
joblib.dump(best_model, model_file)

print(f"✅ Best model saved as: {model_file}")
