import streamlit as st
import plotly.express as px
from Utils.data_loader import load_gtd_data

st.set_page_config(page_title="Country Analysis", layout="wide")

st.title("🗺️ Strategic Country Metrics & Trend Analysis")
st.markdown("Deep-dive analytics into country-specific incident rates, casualty frequencies, and historical vectors.")

# Load cached data core
data = load_gtd_data()

if data is not None:
    all_countries = sorted(data['country_txt'].unique())
    selected_country = st.selectbox("Select Target Country for Assessment", all_countries, index=all_countries.index("India") if "India" in all_countries else 0)
    
    country_data = data[data['country_txt'] == selected_country]
    
    if not country_data.empty:
        st.write("### Tactical Summary Indicators")
        col1, col2, col3 = st.columns(3)
        
        total_incidents = len(country_data)
        total_fatalities = country_data['nkill'].sum()
        total_wounded = country_data['nwound'].sum()
        
        col1.metric("Total Documented Incidents", f"{total_incidents:,}")
        col2.metric("Total Critical Fatalities", f"{total_fatalities:,}")
        col3.metric("Total Wounded Personnel", f"{total_wounded:,}")
        
        st.write("---")
        
        st.subheader("Historical Timeline Vector (Incidents per Year)")
        timeline = country_data.groupby('iyear').size().reset_index(name='Incident Count')
        
        fig_trend = px.line(
            timeline,
            x='iyear',
            y='Incident Count',
            labels={'iyear': 'Year', 'Incident Count': 'Recorded Attacks'},
            title=f"Evolution of Risk Vector: {selected_country}",
            markers=True
        )
        fig_trend.update_layout(template="plotly_dark")
        st.plotly_chart(fig_trend, use_container_width=True)
        
    else:
        st.error(f"No operational data available for {selected_country}.")
else:
    st.error("Data pipeline offline.")