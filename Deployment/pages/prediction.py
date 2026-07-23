import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# =========================
# Page Config
# =========================
st.set_page_config(page_title="House Price Predictor", layout="wide")

# =========================
# Background Style
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(255,255,255,0.92), rgba(255,255,255,0.92)),
                url("https://images.unsplash.com/photo-1560518883-ce09059eeffa");
    background-size: cover;
}

/* titles */
.big-title {
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#2c3e50;
}

/* labels */
label {
    color: #2c3e50 !important;
    font-weight: 600;
}

/* headings */
h1, h2, h3 {
    color: #2c3e50 !important;
}

/* section headers */
h2 {
    background: linear-gradient(90deg, #636EFA, #00C9A7);
    color: white !important;
    padding: 6px 14px;
    border-radius: 10px;
    display: inline-block;
}

/* =========================
   INPUTS CLEAN WHITE
========================= */

/* number input */
.stNumberInput > div {
    background-color: white !important;
    border-radius: 12px !important;
    border: 1px solid #ddd !important;
}

/* number text */
.stNumberInput input {
    background-color: white !important;
    color: #2c3e50 !important;
    border: none !important;
}

/* + - buttons */
.stNumberInput button {
    background-color: #f8f9fa !important;
    color: #2c3e50 !important;
    border: none !important;
}

/* select + multiselect container */
div[data-baseweb="select"] > div {
    background-color: white !important;
    color: #2c3e50 !important;
    border-radius: 12px !important;
    border: 1px solid #ddd !important;
}

/* text inside select */
div[data-baseweb="select"] span {
    color: #2c3e50 !important;
}

/* arrow */
div[data-baseweb="select"] svg {
    color: #2c3e50 !important;
}

/* dropdown list */
div[role="listbox"] {
    background-color: white !important;
    color: #2c3e50 !important;
}

/* hover option */
div[role="option"]:hover {
    background-color: #f1f3f5 !important;
}

/* =========================
   FIX TEXT VISIBILITY
========================= */

input {
    color: #2c3e50 !important;
}

input::placeholder {
    color: #999 !important;
}

/* =========================
   FOCUS EFFECT
========================= */

input:focus, div:focus {
    outline: none !important;
    box-shadow: 0 0 0 2px rgba(99,110,250,0.25) !important;
}

/* =========================
   BUTTON
========================= */

.stButton button {
    background: linear-gradient(90deg, #636EFA, #00C9A7);
    color: white;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

/* =========================
   CAPTION FIX
========================= */

[data-testid="stCaptionContainer"] {
    color: #2c3e50 !important;
    font-size: 15px !important;
    font-weight: 500 !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Title
# =========================
st.markdown('<div class="big-title">🏠 House Price Prediction</div>', unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center;'>
    <h3 style='
        background: linear-gradient(90deg, #27ae60, #00C9A7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    '>
        Predict Indian House Prices using Machine Learning 🤖🇮🇳
    </h3>
    <p style='color:#2c3e50; font-size:15px;'>
        Model trained on Indian real estate dataset
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# Paths
# =========================
BASE_DIR = Path(__file__).resolve()
while not (BASE_DIR / "dataset").exists():
    BASE_DIR = BASE_DIR.parent

# Load model + data
model_path = BASE_DIR / "models" / "house_price_model.pkl"
data_path = BASE_DIR / "dataset" / "clean_house_prices_df.csv"

@st.cache_resource
def load_model(path):
    return joblib.load(path)

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

model = load_model(model_path)
df = load_data(data_path)

locations = sorted(df["location"].unique())

# =========================
# Inputs
# =========================

st.markdown("### 📍 Location")

col1, col2 = st.columns(2)

with col1:
    location = st.selectbox("Location", ["Select Location"] + locations)

with col2:
    facing = st.selectbox("Facing", ["Select Facing"] + list(df["facing"].unique()))

# =========================
# House Details
# =========================
st.markdown("### 🏠 House Details")

col1, col2, col3 = st.columns(3)

with col1:
    bhk = st.number_input("BHK", min_value=1, max_value=10, value=None)

with col2:
    bathroom = st.number_input("Bathrooms", min_value=1, max_value=10, value=None)

with col3:
    balcony = st.number_input("Balcony", min_value=0, max_value=5, value=None)

# =========================
# Area
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    super_area = st.number_input("Super Area", min_value=1, value=None)

with col2:
    current_floor = st.number_input("Current Floor", min_value=0, value=None)

with col3:
    total_floors = st.number_input("Total Floors", min_value=1, value=None)

# =========================
# Additional Info
# =========================
st.markdown("### 🛋️ Additional Info")

col1, col2, col3 = st.columns(3)

with col1:
    furnishing = st.selectbox("Furnishing", ["Select Furnishing"] + list(df["Furnishing"].unique()))

with col2:
    transaction = st.selectbox("Transaction", ["Select Transaction"] + list(df["Transaction"].unique()))

with col3:
    ownership = st.selectbox("Ownership", ["Select Ownership"] + list(df["Ownership"].unique()))

# =========================
# Views
# =========================
st.markdown("### 🌴 Views")

view = st.multiselect(
    "Select Views",
    ["Garden_Park", "Main_Road", "Pool"]
)

# =========================
# Prediction
# =========================
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 Predict Price"):

    # =========================
    # Validation
    # =========================
    if (
        "Select" in location or
        "Select" in facing or
        "Select" in furnishing or
        "Select" in transaction or
        "Select" in ownership or
        bhk is None or
        bathroom is None or
        super_area is None or
        current_floor is None or
        total_floors is None
    ):
        st.error("⚠️ Please fill all required fields")

    elif current_floor > total_floors:
        st.error("⚠️ Current Floor cannot be greater than Total Floors")

    elif bhk < bathroom:
        st.warning("⚠️ Bathrooms are more than BHK (check if this is correct)")

    else:

        # =========================
        # Prepare Data
        # =========================
        data = pd.DataFrame([{
            "location": location,
            "Transaction": transaction,
            "Furnishing": furnishing,
            "facing": facing,
            "Ownership": ownership,
            "BHK": bhk,
            "Bathroom": bathroom,
            "Balcony": balcony if balcony is not None else 0,
            "Super Area": super_area,
            "Current_Floor": current_floor,
            "Total_Floors": total_floors,

            # Views
            "View_Garden_Park": 1 if "Garden_Park" in view else 0,
            "View_Main_Road": 1 if "Main_Road" in view else 0,
            "View_Pool": 1 if "Pool" in view else 0,
            "View_Unknown": 1 if len(view) == 0 else 0,
        }])

        # =========================
        # Prediction
        # =========================
        with st.spinner("Predicting..."):
            prediction = model.predict(data)[0]

        # =========================
        # Output
        # =========================
        st.markdown(f"""
        <div style="
            background-color:#d4edda;
            padding:25px;
            border-radius:12px;
            text-align:center;
            font-size:24px;
            font-weight:bold;
            color:#155724;
        ">
        💰 Estimated Price: {int(prediction):,} ₹
        </div>
        """, unsafe_allow_html=True)

# =========================
# Footer
# =========================
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#2c3e50; font-size:16px; font-weight:600;'>
    👨‍💻 Developed by Ahmed Samy Elzoghby | ML Project 🚀
</div>
""", unsafe_allow_html=True)