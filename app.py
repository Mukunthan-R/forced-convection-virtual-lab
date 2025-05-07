# app.py
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from forced_convection_animation import generate_animation

st.set_page_config(page_title="Forced Convection Virtual Lab", layout="wide")

# Title
st.title("🔬 Forced Convection Heat Transfer Virtual Lab")
st.markdown("An interactive tool to explore heat transfer by forced convection in a horizontal pipe.")

# Aim
st.header("🎯 Aim")
st.markdown("""
To determine the **average surface heat transfer coefficient** for a pipe, 
transmitting heat by **forced convective flow of air through it**, both **experimentally** and **empirically**.
""")

# Specifications
st.header("📏 Specifications")
specs = {
    "Length of Test Section": "1.0 m",
    "Diameter of Test Section": "0.05 m (5 cm)",
    "Diameter of Orifice": "0.02 m (2 cm)",
    "Number of Thermocouples": "5",
    "Blower Power": "1 HP",
    "Measurement Devices": "Voltmeter (0–250 V), Ammeter (0–10 A)"
}
st.table(pd.DataFrame(specs.items(), columns=["Component", "Specification"]))

# Theory
st.header("📚 Theory")
st.markdown(r"""
In forced convection, heat is transferred from a heated surface to a moving fluid driven by external means.
The heat transfer coefficient \( h \) is calculated by:
$$
Q = h \cdot A \cdot (T_s - T_a) \quad \Rightarrow \quad h = \frac{Q}{A(T_s - T_a)}
$$
Where:
- \( Q = V \cdot I \) → Electrical heat input
- \( A = \pi D L \) → Surface area of pipe
- \( T_s \) = Average surface temperature from thermocouples
- \( T_a \) = Ambient air temperature
""", unsafe_allow_html=True)

# Description
st.header("📦 Description")
st.markdown("""
The setup consists of a heated aluminum pipe with forced air flow. 
Thermocouples measure temperature at 5 points. The power input is varied, and airflow is monitored via orifice.
""")

# Procedure
st.header("🧪 Procedure")
st.markdown("""
1. Start blower.
2. Turn on heater and set voltage & current.
3. Wait for steady-state.
4. Record **V, I, T1–T5, Ta**.
5. Calculate:
   - \( T_s = (T1 + T2 + T3 + T4 + T5)/5 \)
   - \( Q = V \cdot I \)
   - \( A = \pi D L \)
   - \( h = Q / (A \cdot (T_s - T_a)) \)
""", unsafe_allow_html=True)

# Experimental Rig
st.header("🛠️ Experimental Test Rig")
st.markdown("""
- Blower and Orifice meter
- Heated pipe (Aluminum)
- 5 Thermocouples
- Voltmeter & Ammeter
""")

# Schematic Image
st.header("📷 Schematic Diagram")
try:
    schematic = Image.open("forced_convection_schematic.png")
    st.image(schematic, caption="Forced Convection Experimental Setup", use_column_width=True)
except FileNotFoundError:
    st.warning("⚠️ Schematic image not found. Please place 'forced_convection_schematic.png' in the same folder.")

# Inputs
st.header("📥 Experimental Inputs")
col1, col2 = st.columns(2)
with col1:
    voltage = st.number_input("Voltage (V)", value=60.0)
    current = st.number_input("Current (A)", value=1.5)
    air_temp = st.number_input("Air Temperature (°C)", value=30.0)
with col2:
    temps = [
        st.number_input("Surface Temp T1 (°C)", value=85.0),
        st.number_input("Surface Temp T2 (°C)", value=87.0),
        st.number_input("Surface Temp T3 (°C)", value=88.0),
        st.number_input("Surface Temp T4 (°C)", value=86.5),
        st.number_input("Surface Temp T5 (°C)", value=89.0)
    ]

# Calculation
st.header("📊 Calculation & Results")
Q = voltage * current
Ts_avg = np.mean(temps)
D = 0.05
L = 1.0
A = np.pi * D * L
delta_T = Ts_avg - air_temp

if delta_T > 0:
    h = Q / (A * delta_T)
    st.success(f"✅ Heat Transfer Coefficient (h): {h:.2f} W/m²°C")
else:
    st.error("Temperature difference must be positive.")

# Summary Table
st.subheader("📑 Data Summary")
df = pd.DataFrame({
    "Parameter": ["Voltage (V)", "Current (A)", "Power Q (W)", "Area A (m²)", 
                  "Avg Surface Temp (Ts)", "Air Temp (Ta)", "ΔT", "h (W/m²°C)"],
    "Value": [voltage, current, Q, A, Ts_avg, air_temp, delta_T, h if delta_T > 0 else "Error"]
})
st.table(df)
