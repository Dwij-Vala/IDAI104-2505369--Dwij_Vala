# 🚀 Rocket Launch Command Center
## Mathematics for AI – Summative Assessment

---

## 👤 Student Information

**Name:** Dwij Vala  
**Candidate Registration Number:** 2505359
**CRS:** Artificial Intelligence  
**Course:** Mathematics for AI – I  
**School:** Udgam School for Children  

---

## 🌍 Live Application

🔗 **Streamlit Deployment Link:**  
👉 https://math-sa-dwij.streamlit.app

---

# 📌 Project Overview

The Rocket Launch Command Center is an interactive aerospace simulation and mission analytics dashboard built using Python and Streamlit.

This project integrates:

• Real-world mission dataset analysis  
• Mathematical modeling of rocket motion  
• Interactive physics-based simulation  
• 3D trajectory visualization  

The goal is to apply mathematical concepts from Mathematics for AI to simulate and analyze rocket launches under realistic physical constraints.

---

# 🎯 Problem Statement

This project addresses the following questions:

• How do thrust, mass, gravity, and drag affect rocket motion?  
• How does changing payload and fuel influence lift-off?  
• When does a rocket achieve orbit?  
• What insights can be extracted from historical mission datasets?  

The project combines data analysis with Newtonian physics to create a real-world simulation environment.

---

# 📊 Part 1: Data Analysis

## 🧹 Data Cleaning & Preprocessing

The dataset (`space_missions_dataset.csv`) was processed using:

• Removal of duplicate entries  
• Standardization of column names  
• Conversion of numeric columns  
• Handling of missing values  

Libraries used:

• Pandas  
• NumPy  

This ensures accurate and consistent visualization results.

---

## 📈 Visualizations Implemented

The dashboard includes:

• Scatter Plot – Relationship between mission variables  
• Line Plot – Trends in mission performance  
• Correlation Heatmap – Relationships between numeric features  
• Dynamic numeric comparisons  

These visualizations help identify:

• Cost patterns  
• Payload relationships  
• Fuel usage trends  
• Variable correlations  

---

# 🚀 Part 2: Rocket Launch Simulation

## 📐 Mathematical Model

The simulation applies Newton’s Second Law:

a = (T − mg − kv²) / m

Where:

T = Thrust (Newtons)  
m = Mass (kg)  
g = 9.81 m/s²  
k = Drag coefficient  
v = Velocity  

This equation determines acceleration at every time step.

---

## 🌫 Atmospheric Drag Model

Air density decreases exponentially with altitude:

ρ = e^(−h / 100000)

This reduces drag as altitude increases, making the simulation more realistic.

---

## ⛽ Variable Mass System

The rocket mass changes dynamically as fuel burns.

As fuel decreases:

• Total mass decreases  
• Acceleration increases  
• Rocket performance improves  

This models real-world rocket behavior.

---

## 🌌 Orbit Detection Logic

Orbital velocity threshold ≈ 7800 m/s.

If maximum velocity exceeds this value:

→ Orbit Achieved  

If thrust is insufficient:

→ Launch Failed  

Otherwise:

→ Successful Lift-Off  

---

# 📊 Simulation Outputs

The application displays:

• Altitude vs Time  
• Velocity vs Time  
• 3D Rocket Trajectory  
• Launch Status Indicator  
• Maximum Altitude  
• Maximum Velocity  
• Remaining Fuel  

These outputs provide both visual and quantitative analysis.

---

# ⚙️ Assumptions Made

• Constant gravitational acceleration  
• Constant drag coefficient  
• Exponential atmospheric density model  
• Single-stage rocket  
• No wind or lateral forces  

These assumptions simplify the model while preserving realistic dynamics.

---

# 🧠 Mathematical & Real-World Relevance

This project demonstrates:

• Application of Newtonian mechanics  
• Numerical modeling using discrete time simulation  
• Integration of mathematics with engineering systems  
• Data-driven analytical thinking  

It connects theoretical mathematics with practical aerospace simulation.

---

# 🛠 Technologies Used

• Python  
• Streamlit  
• Pandas  
• NumPy  
• Plotly  
• OpenPyXL  

---

# 💻 How to Run Locally

1. Clone repository:
   git clone [YOUR GITHUB REPO LINK]

2. Navigate to project folder:
   cd repository_name

3. Install dependencies:
   pip install -r requirements.txt

4. Run application:
   streamlit run app.py

---

# 📦 Repository Structure

app.py  
requirements.txt  
space_missions_dataset.csv  
rocket_header.jpg  
rocket_launch.jpg  
space_earth.jpg  
README.md  
.gitignore  

---

# 🎓 Learning Outcomes

Through this project, I developed:

• Understanding of applied Newtonian mechanics  
• Skills in numerical simulation  
• Experience in data cleaning and visualization  
• Deployment skills using GitHub and Streamlit Cloud  
• Ability to integrate mathematics with AI tools  

---

# 🏁 Conclusion

The Rocket Launch Command Center successfully integrates:

• Mathematical modeling  
• Aerospace physics simulation  
• Interactive visualization  
• Real-world dataset analysis  

This project demonstrates both conceptual understanding and technical implementation of Mathematics for AI principles.

---
