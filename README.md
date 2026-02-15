# 🚀 Rocket Launch Command Center  
## Mathematics for AI – Summative Assessment

---

## 👤 Student Details

**Name:** Dwij Vala  
**Candidate Registration Number:** 2505369  
**CRS:** Artificial Intelligence  
**Course:** Mathematics for AI – I  
**School:** Udgam School for Children  

---

## 🌍 Live Application

🔗 **Streamlit Deployment Link:**  
👉 https://math-sa-dwij.streamlit.app/

---

# 📌 Project Overview

This project develops an interactive Rocket Launch Command Center that combines:

1. Mission data analysis  
2. Physics-based rocket launch simulation  

The system applies mathematical modeling to simulate rocket motion while analyzing real mission data using visualization techniques.

The objective is to connect mathematical principles with real-world aerospace engineering concepts.

---

# 🎯 Problem Statement

This project explores:

- How thrust, mass, and drag influence rocket motion  
- How mission variables relate to each other in real datasets  
- How mathematical equations can simulate real-world launch conditions  
- How to determine lift-off and orbit achievement  

The simulation integrates Newtonian mechanics with data-driven insights.

---

# 📊 Part 1: Data Analysis

## 🧹 Data Cleaning & Preprocessing

The dataset was processed using:

- Removal of duplicate entries  
- Conversion of numeric columns  
- Standardization of column names  
- Handling of missing values  

Libraries used:
- Pandas
- NumPy

---

## 📈 Visualizations Implemented

The dashboard includes:

- Scatter Plot → Relationship between mission variables  
- Line Plot → Trends in mission parameters  
- Correlation Heatmap → Relationship between numeric variables  
- Dynamic numeric visualizations  

These visualizations reveal patterns in:

- Cost trends  
- Payload relationships  
- Fuel consumption  
- Mission performance  

---

# 🚀 Part 2: Rocket Launch Simulation

## 📐 Mathematical Model

The simulation is based on Newton’s Second Law:

a = (T − mg − kv²) / m

Where:

- T = Thrust (Newtons)  
- m = Mass (kg)  
- g = 9.81 m/s²  
- k = Drag coefficient  
- v = Velocity  

---

## 🌫 Atmospheric Drag Model

Air density decreases exponentially with altitude:

ρ = e^(−h / 100000)

This reduces drag as altitude increases.

---

## ⛽ Variable Mass System

As fuel burns:

- Total mass decreases  
- Acceleration changes dynamically  
- Rocket performance improves during ascent  

---

## 🌌 Orbit Detection

Orbital velocity threshold ≈ 7800 m/s.

If maximum velocity exceeds this value:

→ Orbit Achieved  

Otherwise:

→ Successful Lift-Off or Launch Failure  

---

# 📊 Simulation Outputs

The system displays:

- Altitude vs Time  
- Velocity vs Time  
- 3D Rocket Trajectory  
- Launch Status Indicator  
- Maximum Altitude  
- Maximum Velocity  
- Fuel Remaining  

---

# ⚙️ Assumptions

- Constant gravitational acceleration  
- Constant drag coefficient  
- Exponential atmospheric model  
- Single-stage rocket  
- No wind or lateral forces  

These simplify the simulation while maintaining realism.

---

# 🧠 Mathematical & Real-World Relevance

This project demonstrates:

- Application of Newtonian mechanics  
- Numerical modeling using time-step simulation  
- Data analysis using statistical visualization  
- Real-world aerospace system modeling  

It integrates mathematics, physics, and artificial intelligence principles.

---

# 🛠 Technologies Used

- Python  
- Streamlit  
- Pandas  
- NumPy  
- Plotly  
- OpenPyXL  

---
