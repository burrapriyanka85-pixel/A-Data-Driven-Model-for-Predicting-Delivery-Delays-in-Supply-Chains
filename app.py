# app.py
import joblib

# Suppose you want to save the logistic regression pipeline as logistics.pkl
joblib.dump(lr_pipeline, "logistics.pkl")


import os
from pathlib import Path
import streamlit as st
import pandas as pd
import joblib

# =============================
# Page Config
# =============================
st.set_page_config(page_title="Parcel Delay Prediction", layout="centered")
st.title("📦 Parcel Delivery Delay Prediction")
st.markdown(
    "This app predicts whether a parcel will be **Late** or **On Time** using a trained ML model."
)

# =============================
# Model loader (robust pathing)
# =============================
@st.cache_resource(show_spinner=False)
def load_model():
    here = Path(__file__).resolve().parent

    # Allow override via environment variable if you ever need it
    env_path = os.getenv("MODEL_PATH")

    candidates = [
        Path(env_path) if env_path else None,
        here / "logistic_model.pkl",       # <-- file next to app.py (your case)
        here / "logistics.pkl",
        here.parent / "data" / "logistics.pkl",  # <-- original path from your code
    ]

    for p in candidates:
        if p and p.exists():
            try:
                model_obj = joblib.load(p)
                return model_obj, p
            except Exception as e:
                st.error(f"Failed to load model from {p}:\n{e}")
                return None, p

    return None, None


model, model_path = load_model()

if model is None:
    st.warning(
        "Model file not found.\n\n"
        "I looked for:\n"
        "• ./logistic_model.pkl (next to app.py)\n"
        "• ./logistics.pkl (next to app.py)\n"
        "• ../data/logistics.pkl\n\n"
        "Put your model file in one of those locations or set an env var MODEL_PATH to the exact file."
    )
else:
    st.caption(f"Model loaded from: `{model_path}`")

# =============================
# Input Fields
# =============================
st.header("Enter Parcel Details")
col1, col2 = st.columns(2)

with col1:
    freight_cost = st.number_input("Freight Cost", min_value=0.0, value=50.0, step=1.0)
    weight = st.number_input("Weight (kg)", min_value=0.0, value=10.0, step=0.5)
    customer_zip = st.text_input("Customer Zip Code", "12345")

with col2:
    distance = st.number_input("Distance (km)", min_value=0.0, value=200.0, step=10.0)
    shipping_mode = st.selectbox("Shipping Mode", ["Standard", "Express", "Same Day"])
    category = st.selectbox("Category", ["Office Supplies", "Electronics", "Apparel", "Other"])

# =============================
# Convert Input to DataFrame
# (names must match what the pipeline expects)
# =============================
input_data = pd.DataFrame(
    [{
        "Freight Cost": freight_cost,
        "Weight": weight,
        "Customer Zip": customer_zip,
        "Distance": distance,
        "Shipping Mode": shipping_mode,
        "Category": category,
    }]
)

# =============================
# Make Prediction
# =============================
if st.button("Predict"):
    if model is None:
        st.error("Cannot predict: Model is not loaded.")
    else:
        try:
            pred = model.predict(input_data)[0]  # pipeline handles preprocessing
            if int(pred) == 1:
                st.error("The parcel is **likely to be Late**.")
            else:
                st.success("The parcel is **likely to be On Time**.")
        except Exception as e:
            st.error(f"Error in prediction: {e}")
