import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

st.set_page_config(page_title="Attack Prediction Engine", layout="wide")

st.title("🤖 Agentic Attack Profiling & Prediction Engine")
st.markdown("Utilizes trained classification architectures to evaluate tactical vector characteristics and predict potential attack methodologies.")

# Define paths to saved model files
MODEL_PATH = "Models/attack_prediction_model.pkl"
ENCODERS_PATH = "Models/feature_encoders.pkl"
TARGET_PATH = "Models/target_encoder.pkl"

# Check if model binaries are generated
if not (os.path.exists(MODEL_PATH) and os.path.exists(ENCODERS_PATH) and os.path.exists(TARGET_PATH)):
    st.error("⚠️ Prediction models are offline. Please run `python train_attack_model.py` in your terminal workspace to build deployment files.")
else:
    # Load archived models
    @st.cache_resource
    def load_prediction_artifacts():
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        with open(ENCODERS_PATH, "rb") as f:
            encoders = pickle.load(f)
        with open(TARGET_PATH, "rb") as f:
            target_le = pickle.load(f)
        return model, encoders, target_le

    model, encoders, target_le = load_prediction_artifacts()

    st.subheader("Input Operational Intelligence Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        region = st.selectbox("Geographic Focus Region", encoders['region_txt'].classes_)
        country = st.selectbox("Target Nation", encoders['country_txt'].classes_)
        
    with col2:
        target_type = st.selectbox("Anticipated Objective/Target Entity", encoders['targtype1_txt'].classes_)
        weapon_type = st.selectbox("Identified Weapon Classification", encoders['weaptype1_txt'].classes_)

    st.write("---")
    
    if st.button("Analyze & Predict Operational Profile", type="primary"):
        # Transform inputs using loaded encoders
        try:
            encoded_inputs = [
                encoders['region_txt'].transform([region])[0],
                encoders['country_txt'].transform([country])[0],
                encoders['targtype1_txt'].transform([target_type])[0],
                encoders['weaptype1_txt'].transform([weapon_type])[0]
            ]
            
            # Predict
            prediction_idx = model.predict([encoded_inputs])[0]
            predicted_attack = target_le.inverse_transform([prediction_idx])[0]
            
            # Show output prediction
            st.success("### 📊 Calculated Analysis Profile")
            st.info(f"**Predicted Tactical Attack Methodology:** `{predicted_attack}`")
            
        except Exception as e:
            st.error(f"Error calculating operational values: {e}")