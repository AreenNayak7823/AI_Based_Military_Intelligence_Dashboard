import streamlit as st

st.set_page_config(
    page_title="AI-Based Military Intelligence Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main Title Grid
st.title("🛡️ AI-Based Military Intelligence Dashboard")
st.write("---")

# Welcome Banner
st.markdown("""
### 🌐 Strategic Operations Command Gateway
This dashboard provides tactical, geospatial, and predictive military intelligence analysis utilizing the 
**Global Terrorism Database (GTD)**. By synthesizing global historical incident monitoring with optimized 
machine learning, the system provides real-time regional risk metrics, trend trajectories, and threat estimations.
""")

st.info("👈 **System Initialization Complete:** Select an active intelligence module from the left sidebar panel to begin analytics deployment.")

st.write("---")

# Visual Grid Layout for Sub-Modules
st.subheader("Available Tactical Systems")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### 📊 Strategic & Visual Analysis
    * **🏠 Home Node:** Verifies system diagnostics, directory telemetry, and data core loading sequences.
    * **🌏 Global Threat Map:** Renders high-speed geospatial mapping layers tracking regional distribution clusters.
    * **🗺️ Country Analysis:** Deep-dives into localized regional trends, casualties, and annual frequency volumes.
    """)

with col2:
    st.markdown("""
    #### 🤖 Predictive AI & Intelligence Operations
    * **🧠 Attack Prediction:** Utilizes a trained Random Forest classifier to identify anticipated tactical attack profiles.
    * **🚨 Threat Level Prediction:** Algorithmically computes localized hazard threat scoring indexing matrices.
    * **📈 Forward Forecasting:** Projects 5-year mathematical risk vector trajectories using linear regression parameters.
    * **📋 AI Intelligence Report:** Generates and exports dynamic plain-text briefings for command-level personnel.
    """)

st.write("---")
st.caption("AI-Based Military Intelligence Dashboard | Tactical Data Analysis Terminal Engine")