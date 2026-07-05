import streamlit as st
import pandas as pd
from Utils.data_loader import load_gtd_data

st.set_page_config(page_title="AI Intelligence Report", layout="wide")

st.title("📋 Automated Tactical Intelligence Reporting")
st.markdown("Generates a unified executive briefing report based on localized threat vectors, high-frequency targets, and statistical severity indices.")

# Fetch centralized data pipeline
data = load_gtd_data()

if data is not None:
    st.subheader("Report Generation Parameters")
    
    col1, col2 = st.columns(2)
    with col1:
        target_country = st.selectbox("Select Theater of Operations", sorted(data['country_txt'].unique()), index=sorted(data['country_txt'].unique()).index("India") if "India" in data['country_txt'].unique() else 0)
    with col2:
        security_classification = st.selectbox("Document Classification Label", ["CONFIDENTIAL", "SECRET", "TOP SECRET // NOFORN"])
        
    st.write("---")
    
    # Process localized information for compilation
    country_data = data[data['country_txt'] == target_country]
    
    if not country_data.empty:
        total_events = len(country_data)
        total_fatalities = int(country_data['nkill'].sum())
        total_wounded = int(country_data['nwound'].sum())
        
        # Extract highest-frequency attributes
        top_attack = country_data['attacktype1_txt'].value_counts().index[0] if not country_data['attacktype1_txt'].empty else "Unknown"
        top_target = country_data['targtype1_txt'].value_counts().index[0] if not country_data['targtype1_txt'].empty else "Unknown"
        top_group = country_data['gname'].value_counts().index[0] if not country_data['gname'].empty else "Unknown"
        if top_group == "Unknown" or top_group == "unknown":
            top_group = "Unidentified Cells"
            
        # Compile plain-text report format
        report_content = f"""================================================================================
TACTICAL INTELLIGENCE BREIFING REGISTRY
CLASSIFICATION: {security_classification}
THEATER OF OPERATIONS: {target_country.upper()}
================================================================================

1. EXECUTIVE SUMMARY
--------------------------------------------------------------------------------
This document compiles an agentic AI data synthesis of historical threat parameters
tracked within the specified operational zone. A total of {total_events:,} unique 
hostile incidents have been indexed and analyzed for structural vector alignment.

2. QUANTITATIVE SEVERITY INDICES
--------------------------------------------------------------------------------
* Total Tracked Incidents       : {total_events:,}
* Aggregated Fatalities         : {total_fatalities:,}
* Aggregated Wounded Personnel  : {total_wounded:,}
* Total Operational Casualties   : {total_fatalities + total_wounded:,}

3. HIGH-FREQUENCY THREAT PROFILING
--------------------------------------------------------------------------------
* Primary Attack Methodology   : {top_attack}
* Principal Objective Target    : {top_target}
* Dominant Active Adversary     : {top_group}

4. ANALYTICAL CONCLUSION & POSTURE RECOMMENDATION
--------------------------------------------------------------------------------
The threat grid for {target_country} indicates structured activity profiles heavily 
relying on '{top_attack}' tactics aimed primarily at '{top_target}' targets. 
Command elements should allocate specialized defensive grids and tactical monitoring 
resources aligned against these verified profiles to neutralize regional risk.

--------------------------------------------------------------------------------
Generated automatically by AI-Based Military Intelligence Dashboard.
END OF BRIEFING LOG.
================================================================================
"""

        # Display report block on UI
        st.subheader("Generated Tactical Dossier Preview")
        st.code(report_content, language="text")
        
        # Provide instant File Download capability
        st.write("")
        st.download_button(
            label="💾 Download Briefing Report (.TXT)",
            data=report_content,
            file_name=f"INTEL_REPORT_{target_country.upper()}.txt",
            mime="text/plain",
            type="primary"
        )
        
    else:
        st.error(f"No database entries available to generate a brief for {target_country}.")
else:
    st.error("Centralized data pipeline offline.")