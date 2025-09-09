import streamlit as st
import pandas as pd
import joblib

# Load model & scaler
model = joblib.load("energy_efficiency_model.pkl")
scaler = joblib.load("scaler.pkl")

# 🎨 Page setup
st.set_page_config(page_title="Smart Building Energy Predictor", page_icon="🏢", layout="wide")

# 🌈 Custom CSS for Attractive UI
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            text-align:center;
            color:black;
            font-size:45px;
            font-weight:bold;
            padding-top:1px;
        }
        .subtitle {
            text-align:center;
            color:black;
            font-size:20px;
            margin-bottom:30px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #16A085, #27AE60);
            color:white;
            border-radius:12px;
            height:3em;
            width:100%;
            font-size:18px;
            font-weight:bold;
            border:none;
            transition:0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #138D75, #1E8449);
            transform: scale(1.05);
        }
        .prediction-card {
            background: white;
            padding: 25px;
            border-radius: 20px;
            box-shadow: 2px 4px 15px rgba(0,0,0,0.3);
            text-align:center;
            margin-top:25px;
        }
        .footer {
            text-align:center;
            color:black;
            font-size:14px;
            margin-top:50px;
        }
    </style>
""", unsafe_allow_html=True)

# 🏠 Title & Subtitle
st.markdown("<div class='main-title'>🏢 Smart Building Energy Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Predictions for Heating 🔥  &  Cooling ❄️ loads</div>", unsafe_allow_html=True)

# 📊 Input Layout
col1, col2 = st.columns(2)

with col1:
    rc = st.slider("Relative Compactness", 0.6, 1.0, 0.8, 0.01)
    sa = st.number_input("Surface Area (m²)", 500, 800, 650, step=10)
    wa = st.number_input("Wall Area (m²)", 200, 400, 300, step=10)
    ra = st.number_input("Roof Area (m²)", 100, 220, 150, step=5)

with col2:
    oh = st.selectbox("Overall Height (m)", [3.5, 7.0 , 10.0, 14.0, 17.5, 21.0, 24.5, 28.0, 31.5, 35.0, 38.5, 42.0, 45.5, 49.0, 52.5, 56.0, 59.5, 63.0, 66.5, 70.0])
    ornt = st.selectbox("Orientation", [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])
    ga = st.slider("Glazing Area (ratio)", 0.0, 0.4, 0.25, 0.05)
    gad = st.selectbox("Glazing Area Distribution", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])

# 🚀 Prediction Button
if st.button("🔮 Predict Energy Load"):
    input_data = pd.DataFrame([[rc, sa, wa, ra, oh, ornt, ga, gad]],
                              columns=['Relative_Compactness','Surface_Area','Wall_Area','Roof_Area',
                                       'Overall_Height','Orientation','Glazing_Area','Glazing_Area_Distribution'])
    input_scaled = scaler.transform(input_data)
    pred = model.predict(input_scaled)[0]

    # 🎉 Results in Stylish Card
    st.markdown(
        f"""
        <div class="prediction-card">
            <h2 style="color:#E74C3C;">🔥 Heating Load: {pred[0]:.2f}</h2>
            <h2 style="color:#3498DB;">❄️ Cooling Load: {pred[1]:.2f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("👆 Adjust building parameters and click **Predict Energy Load**")

# ✍️ Footer
st.markdown("<div class='footer'><b>Developed By :- Pratik Ganesh Rajput </b> </div>", unsafe_allow_html=True)
