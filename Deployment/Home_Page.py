import streamlit as st
import pandas as pd
from pathlib import Path

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="House Project", layout="wide")

#==========================
# Data path
#==========================
BASE_DIR = Path(__file__).resolve()
while not (BASE_DIR / "dataset").exists():
    BASE_DIR = BASE_DIR.parent
data_path = BASE_DIR / "dataset" / "clean_house_prices_df.csv"
# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data(path):
    return pd.read_csv(path)
df = load_data(data_path)

# =========================
# HOME PAGE
# =========================
st.title("🏠 House Price Prediction Project")

st.markdown("### 📌 Overview")
st.write("""
This project predicts house prices using Machine Learning.
It analyzes multiple features like location, area, number of rooms,
and amenities to estimate property value.
""")

st.markdown("---")

# =========================
# DATASET INFO
# =========================
st.markdown("### 📊 Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("📄 Total Rows", df.shape[0])
col2.metric("📊 Total Features", df.shape[1])
col3.metric("📍 Unique Locations", df["location"].nunique())

st.markdown("---")

st.markdown("### 🧠 Model Details")
st.write("""
- Model Used: **XGBoost Regressor**
- Task: Regression (Predicting Price)
- Input Features:
    - Location
    - Super Area
    - BHK
    - Bathrooms
    - Balcony
    - Floors
    - Furnishing, Facing, Ownership
    - View Features
""")

st.markdown("---")

st.markdown("### 🚀 Project Features")
st.write("""
- 📊 Interactive Dashboard  
- 🤖 Price Prediction System  
- 📈 Real-time Predictions  
""")



st.markdown("---")
st.info("👈 Use the sidebar to navigate between Dashboard and Prediction")
