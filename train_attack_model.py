import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def train_predictive_layers():
    print("🚀 Initializing Tactical Model Training Pipeline...")
    
    file_path = "Data/globalterrorismdb_0718dist.csv"
    columns_to_use = ['region_txt', 'country_txt', 'targtype1_txt', 'weaptype1_txt', 'attacktype1_txt']
    
    if not os.path.exists(file_path):
        print(f"❌ Error: Dataset not found at {file_path}. Please check directory positions.")
        return

    # Load data rows efficiently
    print("📥 Extracting contextual data records...")
    df = pd.read_csv(file_path, usecols=columns_to_use, encoding='ISO-8859-1').dropna()
    
    # Initialize Feature Encoders
    feature_encoders = {}
    feature_cols = ['region_txt', 'country_txt', 'targtype1_txt', 'weaptype1_txt']
    
    X = pd.DataFrame()
    
    print("⚙️ Encoding tactical categorical variables...")
    for col in feature_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(df[col])
        feature_encoders[col] = le
        
    # Initialize Target Encoder (What we want to predict: Attack Type)
    target_encoder = LabelEncoder()
    y = target_encoder.fit_transform(df['attacktype1_txt'])
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Classifier
    print("🧠 Training Agentic Attack Profile Classifier (Random Forest)...")
    model = RandomForestClassifier(n_estimators=50, max_depth=12, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Verify performance
    accuracy = model.score(X_test, y_test)
    print(f"✅ Model Training Complete! Evaluated Accuracy: {accuracy:.2%}")
    
    # Ensure destination models folder exists
    os.makedirs("Models", exist_ok=True)
    
    # Save objects to disk
    print("💾 Archiving prediction layers to storage...")
    with open("Models/attack_prediction_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("Models/feature_encoders.pkl", "wb") as f:
        pickle.dump(feature_encoders, f)
    with open("Models/target_encoder.pkl", "wb") as f:
        pickle.dump(target_encoder, f)
        
    print("🏁 All training binary artifacts successfully saved inside /Models directory!")

if __name__ == "__main__":
    train_predictive_layers()