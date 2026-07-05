import streamlit as st
import numpy as np
import pandas as pd
from Utils.data_loader import load_gtd_data

st.set_page_config(page_title="Threat Level Prediction", layout="wide")

st.title("🚨 Predictive Threat Level & Risk Classification")
st.markdown("Calculates operational risk indicators and assigns local threat posture tiers by processing incident frequency vectors and casualty weight distributions.")

# Fetch our data pipeline
data = load_gtd_data()

if data is not None:
    st.subheader("Select Area of Operations for Risk Assessment")
    
    col1, col2 = st.columns(2)
    with col1:
        target_country = st.selectbox("Select Target Nation Profile", sorted(data['country_txt'].unique()))
    with col2:
        evaluation_year = st.slider("Select Assessment Baseline Year", int(data['iyear'].min()), int(data['iyear'].max()), int(data['iyear'].max()))
        
    st.write("---")
    
    # Process risk scoring based on localized historical data windows
    country_filter = data[(data['country_txt'] == target_country) & (data['iyear'] == evaluation_year)]
    global_year_avg = len(data[data['iyear'] == evaluation_year]) / len(data['country_txt'].unique())
    
    incident_count = len(country_filter)
    total_casualties = country_filter['casualties'].sum()
    
    st.subheader(f"Strategic Risk Evaluation for {target_country} ({evaluation_year})")
    
    # Algorithmic scoring rules for Threat Indexing
    if incident_count == 0:
        threat_score = 0.0
        status_tier = "🟢 LOW RISK POSTURE (LEVEL 1)"
        alert_color = "success"
        description = "Minimal or baseline irregular tactical activity detected. Standard standby defensive parameters recommended."
    elif incident_count <= global_year_avg * 0.5:
        threat_score = 3.5
        status_tier = "🟡 GUARDED OPTIONAL RISK (LEVEL 2)"
        alert_color = "warning"
        description = "Sporadic organized tactical operations recorded. Increase monitoring protocols and maintain baseline security grids."
    elif incident_count <= global_year_avg * 1.5:
        threat_score = 6.2
        status_tier = "🟠 ELEVATED THREAT ALERT (LEVEL 3)"
        alert_color = "warning"
        description = "Consistent localized conflict activity noted. Deploy target profiling, bolster critical logistics, and coordinate regional joint intelligence networks."
    else:
        threat_score = 9.1
        status_tier = "🔴 CRITICAL COMBAT EMERGENCY (LEVEL 4)"
        alert_color = "error"
        description = "High-density active threat distribution profile. Implement strict regional counter-measures, deploy protective perimeters, and activate urgent threat suppression groups."

    # Render risk dial visualization metrics
    c1, c2 = st.columns([1, 2])
    with c1:
        st.metric(label="Computed Threat Index Score", value=f"{threat_score} / 10")
        st.metric(label="Local Incidents Evaluated", value=f"{incident_count:,}")
        st.metric(label="Calculated Casualty Severity Weight", value=f"{total_casualties:,}")
    
    with c2:
        if alert_color == "success":
            st.success(f"**Security Condition:** {status_tier}")
        elif alert_color == "warning":
            st.warning(f"**Security Condition:** {status_tier}")
        else:
            st.error(f"**Security Condition:** {status_tier}")
            
        st.info(f"**Operational Intelligence Briefing:** {description}")

else:
    st.error("Intelligence database data array offline.")