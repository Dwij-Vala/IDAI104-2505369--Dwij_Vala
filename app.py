# ============================================================
# ROCKET LAUNCH COMMAND CENTER
# FINAL STABLE VERSION – Loophole Free
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="Rocket Launch Command Center", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# SAFE IMAGE LOADER
# ============================================================

def load_image_safe(name):
    extensions = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]
    for ext in extensions:
        path = os.path.join(BASE_DIR, name + ext)
        if os.path.exists(path):
            st.image(path, width="stretch")
            return
    st.info(f"{name} image not found (optional).")

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #05070f 0%, #000000 100%);
}
h1 {
    font-size: 42px;
    font-weight: 900;
    color: white;
}
h2, h3 {
    color: #00BFFF;
}
.section-divider {
    height: 2px;
    background: linear-gradient(90deg, #00BFFF, transparent);
    margin: 25px 0px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.title("🚀 ROCKET LAUNCH COMMAND CENTER")
load_image_safe("rocket_header")
st.markdown("Mission Analytics • Mathematical Simulation • 3D Trajectory")
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ============================================================
# LOAD DATA (STRICT + SAFE)
# ============================================================

@st.cache_data
def load_data():
    csv_path = os.path.join(BASE_DIR, "space_missions_dataset.csv")
    if not os.path.exists(csv_path):
        st.error("Dataset file not found.")
        return pd.DataFrame()

    df = pd.read_csv(csv_path)

    # Clean columns
    df.columns = df.columns.str.strip().str.replace("_", " ").str.title()

    # Convert numeric columns safely
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    df = df.drop_duplicates()

    return df

df = load_data()

if df.empty:
    st.stop()

# ============================================================
# SHOW DATA STRUCTURE (DEBUG SAFE)
# ============================================================

# st.write("Columns:", df.columns)

# ============================================================
# KPI SECTION
# ============================================================

st.header("Mission Overview")

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

col1, col2, col3, col4 = st.columns(4)

if len(numeric_cols) >= 1:
    col1.metric("Average " + numeric_cols[0], f"{df[numeric_cols[0]].mean():.2f}")

if len(numeric_cols) >= 2:
    col2.metric("Average " + numeric_cols[1], f"{df[numeric_cols[1]].mean():.2f}")

if len(numeric_cols) >= 3:
    col3.metric("Average " + numeric_cols[2], f"{df[numeric_cols[2]].mean():.2f}")

if len(numeric_cols) >= 4:
    col4.metric("Average " + numeric_cols[3], f"{df[numeric_cols[3]].mean():.2f}")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ============================================================
# DATA VISUALS (DYNAMIC – NEVER FAILS)
# ============================================================

st.header("Mission Data Analysis")

numeric_df = df.select_dtypes(include=np.number)

if numeric_df.shape[1] >= 2:

    cols = numeric_df.columns.tolist()

    colA, colB = st.columns(2)

    with colA:
        fig1 = px.scatter(
            df,
            x=cols[0],
            y=cols[1],
            template="plotly_dark",
            title=f"{cols[0]} vs {cols[1]}"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with colB:
        fig2 = px.line(
            df,
            x=cols[0],
            y=cols[-1],
            template="plotly_dark",
            title=f"{cols[-1]} over {cols[0]}"
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Correlation Heatmap")
    heatmap = px.imshow(
        numeric_df.corr(),
        text_auto=True,
        template="plotly_dark"
    )
    st.plotly_chart(heatmap, use_container_width=True)

else:
    st.warning("Not enough numeric data to generate graphs.")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ============================================================
# SIMULATION SECTION
# ============================================================

st.header("Launch Simulation")
load_image_safe("rocket_launch")

colL, colR = st.columns([1,2])

with colL:
    thrust = st.slider("Thrust (kN)", 500, 3000, 2200)
    payload = st.slider("Payload (tons)", 1, 150, 25)
    fuel_mass = st.slider("Fuel (tons)", 20, 800, 250)
    drag_coeff = st.slider("Drag Coefficient", 0.01, 0.4, 0.07)
    burn_rate = st.slider("Burn Rate (tons/sec)", 0.5, 10.0, 3.0)
    duration = st.slider("Duration (sec)", 60, 400, 200)

# Physics
g = 9.81
dt = 0.05

thrust_N = thrust * 1000
payload_kg = payload * 1000
fuel_kg = fuel_mass * 1000
burn_rate_kg = burn_rate * 1000

velocity = 0
altitude = 0
time = 0
fuel = fuel_kg

dry_mass = payload_kg + 50000
mass = dry_mass + fuel

time_list, alt_list, vel_list = [], [], []
x_traj, y_traj, z_traj = [], [], []

can_lift = thrust_N > mass * g

if not can_lift:
    st.warning("⚠️ Thrust too low to lift off.")

while time < duration and fuel > 0 and can_lift:

    air_density = np.exp(-altitude / 100000)
    drag = drag_coeff * air_density * velocity**2

    acceleration = (thrust_N - mass*g - drag) / mass

    velocity += acceleration * dt
    velocity = max(0, velocity)

    altitude += velocity * dt

    fuel -= burn_rate_kg * dt
    fuel = max(0, fuel)

    mass = dry_mass + fuel

    time_list.append(time)
    alt_list.append(altitude)
    vel_list.append(velocity)

    x_traj.append(altitude * 0.02)
    y_traj.append(altitude * 0.01)
    z_traj.append(altitude)

    time += dt

sim_df = pd.DataFrame({
    "Time": time_list,
    "Altitude": alt_list,
    "Velocity": vel_list
})

with colR:
    if not sim_df.empty:
        st.plotly_chart(px.line(sim_df, x="Time", y="Altitude", template="plotly_dark"),
                        use_container_width=True)
        st.plotly_chart(px.line(sim_df, x="Time", y="Velocity", template="plotly_dark"),
                        use_container_width=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ============================================================
# 3D TRAJECTORY
# ============================================================

st.header("🌌 3D Trajectory")
load_image_safe("space_earth")

if sim_df["Altitude"].max() > 0:

    fig3d = go.Figure(data=[
        go.Scatter3d(
            x=x_traj,
            y=y_traj,
            z=z_traj,
            mode='lines',
            line=dict(color=z_traj, colorscale='Plasma', width=6)
        )
    ])

    fig3d.update_layout(template="plotly_dark", height=700)
    st.plotly_chart(fig3d, use_container_width=True)

else:
    st.info("Increase thrust to visualize trajectory.")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown("Professional Aerospace Simulation Dashboard – Final Stable Build")
