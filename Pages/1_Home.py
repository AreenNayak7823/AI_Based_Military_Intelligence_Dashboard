import streamlit as st
from Utils.data_loader import load_gtd_data

st.title("🏠 Strategic Intelligence Command Center")

st.markdown("""
Welcome to the core operations page. This section initializes the underlying intelligence database 
and establishes system telemetry parameters.
""")

# Trigger our optimized data loader
with st.spinner("Initializing tactical database... Please wait..."):
    data = load_gtd_data()

if data is not None:
    st.success(f"✅ Data pipeline online! Successfully cached {len(data):,} operational records.")
    
    # Show a small preview of the data structure to the user
    st.subheader("Tactical Data Sample Summary")
    st.dataframe(data.head(5), use_container_width=True)
else:
    st.error("❌ Failed to initialize the data pipeline. Please check your file path or encoding attributes.")