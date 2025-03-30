import streamlit as st
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Define the target nutrient ranges (min, max) for crops after cultivating paddy
crop_nutrient_ranges = {
    "Wheat":  {"N": (200, 280), "P": (10, 25), "K": (110, 280), "Ca": (1000, 2000), "Mg": (100, 300), "S": (15, 30), "Zn": (0.6, 1.5), "B": (0.5, 1.5), "pH": (6.5, 7.5), "OC": (0.5, 0.8)},
    "Maize":  {"N": (220, 280), "P": (12, 22), "K": (150, 270), "Ca": (1000, 1800), "Mg": (100, 250), "S": (18, 28), "Zn": (0.8, 1.5), "B": (0.6, 1.4), "pH": (6.2, 7.5), "OC": (0.5, 0.8)},
    "Barley": {"N": (240, 280), "P": (15, 25), "K": (110, 200), "Ca": (1000, 1600), "Mg": (100, 220), "S": (15, 25), "Zn": (0.7, 1.3), "B": (0.5, 1.2), "pH": (6.5, 7.5), "OC": (0.5, 0.75)},
    "Soybean": {"N": (200, 250), "P": (10, 25), "K": (140, 250), "Ca": (1200, 2000), "Mg": (150, 300), "S": (15, 30), "Zn": (0.6, 1.2), "B": (0.5, 1.5), "pH": (5.8, 7.2), "OC": (0.5, 0.8)}
}

# Streamlit App Title
st.title("Crop Recommendation")
st.markdown("Enter soil nutrient levels to find the best crop to cultivate after rice")

# User Inputs for Soil Nutrients
nitrogen = st.number_input("Nitrogen (N) [kg/ha]", min_value=100, max_value=300, value=220)
phosphorus = st.number_input("Phosphorus (P) [kg/ha]", min_value=5, max_value=50, value=15)
potassium = st.number_input("Potassium (K) [kg/ha]", min_value=100, max_value=300, value=150)
calcium = st.number_input("Calcium (Ca) [mg/kg]", min_value=900, max_value=2100, value=1200)
magnesium = st.number_input("Magnesium (Mg) [mg/kg]", min_value=80, max_value=350, value=150)
sulfur = st.number_input("Sulfur (S) [mg/kg]", min_value=10, max_value=40, value=20)
zinc = st.number_input("Zinc (Zn) [mg/kg]", min_value=0.5, max_value=2.0, value=1.0)
boron = st.number_input("Boron (B) [mg/kg]", min_value=0.4, max_value=2.0, value=0.8)
ph = st.number_input("Soil pH", min_value=5.0, max_value=8.5, value=6.5, step=0.1)
organic_carbon = st.number_input("Organic Carbon (%)", min_value=0.4, max_value=1.0, value=0.6, step=0.1)

# Function to check crop suitability
def get_suitable_crops(n, p, k, ca, mg, s, zn, b, ph, oc):
    suitable_crops = []
    for crop, ranges in crop_nutrient_ranges.items():
        if (
            ranges["N"][0] <= n <= ranges["N"][1] and
            ranges["P"][0] <= p <= ranges["P"][1] and
            ranges["K"][0] <= k <= ranges["K"][1] and
            ranges["Ca"][0] <= ca <= ranges["Ca"][1] and
            ranges["Mg"][0] <= mg <= ranges["Mg"][1] and
            ranges["S"][0] <= s <= ranges["S"][1] and
            ranges["Zn"][0] <= zn <= ranges["Zn"][1] and
            ranges["B"][0] <= b <= ranges["B"][1] and
            ranges["pH"][0] <= ph <= ranges["pH"][1] and
            ranges["OC"][0] <= oc <= ranges["OC"][1]
        ):
            suitable_crops.append(crop)
    return suitable_crops

# Predict Button
if st.button("Predict Suitable Crops 🌾"):
    recommended_crops = get_suitable_crops(nitrogen, phosphorus, potassium, calcium, magnesium, sulfur, zinc, boron, ph, organic_carbon)
    if recommended_crops:
        st.success(f"✅ Suitable Crops for Cultivation After Rice: **{', '.join(recommended_crops)}**")
    else:
        st.warning("⚠️ No suitable crop found for the given soil conditions. Adjust the nutrient levels.")
