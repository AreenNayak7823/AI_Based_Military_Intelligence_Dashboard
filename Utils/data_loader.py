import streamlit as st
import pandas as pd

@st.cache_data
def load_gtd_data():
    """
    Loads and optimizes the Global Terrorism Database CSV.
    Uses st.cache_data so the file is only read once into memory,
    keeping your dashboard fast during page navigation.
    """
    # Exact name of your Kaggle dataset path
    file_path = "Data/globalterrorismdb_0718dist.csv"
    
    # We only select the critical columns needed for maps, graphs, and ML
    # to save memory and drastically speed up loading times.
    columns_to_keep = [
        'iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 
        'provstate', 'city', 'latitude', 'longitude', 
        'attacktype1_txt', 'targtype1_txt', 'gname', 
        'weaptype1_txt', 'nkill', 'nwound'
    ]
    
    try:
        # Load data with a fallback encoding common for Kaggle datasets
        df = pd.read_csv(file_path, usecols=columns_to_keep, encoding='ISO-8859-1')
        
        # Clean up missing geospatial or target points for safety
        df['latitude'] = df['latitude'].fillna(0.0)
        df['longitude'] = df['longitude'].fillna(0.0)
        df['nkill'] = df['nkill'].fillna(0).astype(int)
        df['nwound'] = df['nwound'].fillna(0).astype(int)
        df['casualties'] = df['nkill'] + df['nwound']
        
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None