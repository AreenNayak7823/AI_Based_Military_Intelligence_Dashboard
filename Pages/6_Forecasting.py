import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from Utils.data_loader import load_gtd_data

st.set_page_config(page_title="Threat Forecasting Engine", layout="wide")

st.title("📈 Forward-Looking Predictive Threat Forecasting")
st.markdown("Projects mathematical risk trajectories for the next 5 years using linear trendline regression vectors based on historical incident density.")

# Fetch our centralized data cache
data = load_gtd_data()

if data is not None:
    st.subheader("Select Area of Operations for Trend Forecasting")
    
    all_countries = sorted(data['country_txt'].unique())
    selected_country = st.selectbox("Select Target Nation for Projective Analytics", all_countries, index=all_countries.index("India") if "India" in all_countries else 0)
    
    st.write("---")
    
    # 1. Isolate historical timeline for the country
    country_data = data[data['country_txt'] == selected_country]
    
    # Group by year to get annual counts
    annual_counts = country_data.groupby('iyear').size().reset_index(name='Actual Incidents')
    
    # Filter to look at the last 10 historical baseline years available in data for training stability
    recent_history = annual_counts.tail(10)
    
    if len(recent_history) >= 3:
        # 2. Train a fast Linear Regression Model on historical timeline coordinates
        X_historical = recent_history['iyear'].values.reshape(-1, 1)
        y_historical = recent_history['Actual Incidents'].values
        
        reg_model = LinearRegression()
        reg_model.fit(X_historical, y_historical)
        
        # 3. Generate future 5-year timeline coordinates
        last_recorded_year = int(annual_counts['iyear'].max())
        future_years = np.array(range(last_recorded_year + 1, last_recorded_year + 6)).reshape(-1, 1)
        
        # Predict future counts (clip at 0 so predictions don't go negative)
        future_predictions = reg_model.predict(future_years)
        future_predictions = np.clip(future_predictions, 0, None)
        
        # Create a clean DataFrame for future projections
        forecast_df = pd.DataFrame({
            'Year': future_years.flatten(),
            'Projected Incidents': np.round(future_predictions).astype(int)
        })
        
        # 4. Construct a unified visualization using Plotly Graph Objects
        fig = go.Figure()
        
        # Plot full historical curve
        fig.add_trace(go.Scatter(
            x=annual_counts['iyear'], 
            y=annual_counts['Actual Incidents'],
            mode='lines+markers',
            name='Historical Incidents (Actual)',
            line=dict(color='#1f77b4', width=3)
        ))
        
        # Plot future predictive trajectory path
        # Connect the last historical point to the first forecast point for visual continuity
        connect_x = [annual_counts['iyear'].iloc[-1]] + list(forecast_df['Year'])
        connect_y = [annual_counts['Actual Incidents'].iloc[-1]] + list(forecast_df['Projected Incidents'])
        
        fig.add_trace(go.Scatter(
            x=connect_x, 
            y=connect_y,
            mode='lines+markers',
            name='Projected Risk Vector (Forecast)',
            line=dict(color='#ef553b', width=3, dash='dash')
        ))
        
        fig.update_layout(
            title=f"Strategic Threat Trajectory Projection: {selected_country}",
            xaxis_title="Timeline Coordinates (Years)",
            yaxis_title="Annual Documented Incidents",
            template="plotly_dark",
            height=600,
            legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
        )
        
        # Layout organization
        col_graph, col_metrics = st.columns([3, 1])
        
        with col_graph:
            st.plotly_chart(fig, use_container_width=True)
            
        with col_metrics:
            st.write("### 📊 Predictive Matrix")
            st.dataframe(forecast_df.set_index('Year'), use_container_width=True)
            
            # Calculate general momentum trajectory slope
            slope = reg_model.coef_[0]
            if slope > 0.5:
                st.error(f"⚠️ **Risk Vector Escalation:** Analytics show an increasing trend vector (+{slope:.2f}/yr) for {selected_country}.")
            elif slope < -0.5:
                st.success(f"📉 **Risk Vector De-escalation:** Analytics show a decreasing trend vector ({slope:.2f}/yr) for {selected_country}.")
            else:
                st.warning(f"🔄 **Risk Vector Stabilization:** Analytics show a flat or stagnant threat baseline trend for {selected_country}.")
                
    else:
        st.error(f"Insufficient baseline operational timeline history to generate stable forecasting vectors for {selected_country}.")
else:
    st.error("Centralized data intelligence repository offline.")