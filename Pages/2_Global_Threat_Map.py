import streamlit as st
import plotly.express as px
from Utils.data_loader import load_gtd_data

st.set_page_config(page_title="Global Threat Map", layout="wide")

st.title("🌏 Geospatial Tactical Intelligence Map")
st.markdown("Visualizing regional hot-zones, attack distributions, and historical conflict intensity markers.")

# Fetch our optimized, cached dataset from memory
data = load_gtd_data()

if data is not None:
    st.sidebar.subheader("Map Control Filters")
    
    # Timeline slider window
    min_year = int(data['iyear'].min())
    max_year = int(data['iyear'].max())
    year_range = st.sidebar.slider("Select Timeline Window", min_year, max_year, (2010, max_year))
    
    # Regional tracking multi-selector
    all_regions = sorted(data['region_txt'].unique())
    selected_regions = st.sidebar.multiselect("Select Target Regions", all_regions, default=all_regions[:3])

    # Filter operational data matrix
    filtered_data = data[
        (data['iyear'] >= year_range[0]) & 
        (data['iyear'] <= year_range[1]) & 
        (data['region_txt'].isin(selected_regions))
    ]

    # Constrain plotting layers to save browser memory overhead
    if len(filtered_data) > 10000:
        st.warning(f"⚠️ High density layout ({len(filtered_data):,} rows). Sampling latest 10,000 incidents for rendering speed.")
        filtered_data = filtered_data.sort_values(by='iyear', ascending=False).head(10000)

    # Generate dark-mode Plotly Mapbox scatter chart
    if not filtered_data.empty:
        st.subheader("Interactive Event Distribution Matrix")
        
        fig = px.scatter_mapbox(
            filtered_data,
            lat="latitude",
            lon="longitude",
            hover_name="city",
            hover_data=["country_txt", "attacktype1_txt", "gname", "casualties"],
            color="attacktype1_txt",
            size="casualties",
            size_max=30,
            zoom=1,
            mapbox_style="carto-darkmatter", # Dark tactical mapping grid
            title="Geospatial Threat Clustering Map",
            height=650
        )
        
        fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0}, template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.error("No intelligence incidents match the selected filter criteria.")
else:
    st.error("Unable to draw maps. Data pipeline offline.")