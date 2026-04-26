import streamlit as st
import numpy as np
import pickle

# ── Page config ────────────────────────────────────────────
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾",
    layout="centered"
)

# ── Load saved model & preprocessing ──────────────────────
@st.cache_resource
def load_artifacts():
    with open("model.pkl",   "rb") as f: model   = pickle.load(f)
    with open("scaler.pkl",  "rb") as f: scaler  = pickle.load(f)
    with open("encoder.pkl", "rb") as f: encoder = pickle.load(f)
    return model, scaler, encoder

model, scaler, encoder = load_artifacts()

# ── Crop emoji map ─────────────────────────────────────────
crop_emoji = {
    "rice": "🌾", "maize": "🌽", "chickpea": "🫘", "kidneybeans": "🫘",
    "pigeonpeas": "🫛", "mothbeans": "🫘", "mungbean": "🫘", "blackgram": "🫘",
    "lentil": "🫛", "pomegranate": "🍎", "banana": "🍌", "mango": "🥭",
    "grapes": "🍇", "watermelon": "🍉", "muskmelon": "🍈", "apple": "🍎",
    "orange": "🍊", "papaya": "🍑", "coconut": "🥥", "cotton": "🌿",
    "jute": "🌿", "coffee": "☕",
}

# ── UI ─────────────────────────────────────────────────────
st.title("🌾 Crop Recommendation System")
st.markdown("Enter your soil and weather conditions to get the best crop recommendation.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧪 Soil Nutrients")
    N  = st.slider("Nitrogen (N)",   0, 140, 50,
                   help="Ratio of Nitrogen content in soil")
    P  = st.slider("Phosphorus (P)", 5, 145, 50,
                   help="Ratio of Phosphorus content in soil")
    K  = st.slider("Potassium (K)",  5, 205, 50,
                   help="Ratio of Potassium content in soil")
    ph = st.slider("Soil pH",        3.5, 9.9, 6.5, step=0.1,
                   help="pH value of the soil (0–14)")

with col2:
    st.subheader("🌦️ Climate Conditions")
    temperature = st.slider("Temperature (°C)", 8.0,  44.0, 25.0, step=0.1)
    humidity    = st.slider("Humidity (%)",      14.0, 100.0, 70.0, step=0.1)
    rainfall    = st.slider("Rainfall (mm)",     20.0, 300.0, 100.0, step=0.5)

st.markdown("---")

# ── Predict ────────────────────────────────────────────────
if st.button("🌱 Recommend Crop", use_container_width=True):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    crop_name = encoder.inverse_transform(prediction)[0]
    emoji = crop_emoji.get(crop_name, "🌱")

    st.success(f"### {emoji} Recommended Crop: **{crop_name.upper()}**")

    # Show input summary
    with st.expander("📋 Input Summary"):
        st.write(f"**N:** {N} | **P:** {P} | **K:** {K} | **pH:** {ph}")
        st.write(f"**Temperature:** {temperature}°C | **Humidity:** {humidity}% | **Rainfall:** {rainfall}mm")

    # Probabilities (if model supports it)
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(input_scaled)[0]
        top5_idx = probs.argsort()[-5:][::-1]
        st.markdown("#### Top 5 Possible Crops:")
        for idx in top5_idx:
            c = encoder.classes_[idx]
            e = crop_emoji.get(c, "🌱")
            st.progress(float(probs[idx]), text=f"{e} {c} — {probs[idx]*100:.1f}%")

# ── Footer ─────────────────────────────────────────────────
st.markdown("---")
st.caption("Built with Scikit-learn + Streamlit | NPK Crop Recommendation Dataset")