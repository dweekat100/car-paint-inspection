import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 car body paint & damage inspection")

# -----------------------------
# Parts (MUST MATCH SVG anchor IDs)
# -----------------------------
parts = [
    "rear_left_fender",
    "rear_right_fender",
    "rear_left_door",
    "rear_right_door",
    "front_left_fender",
    "front_right_fender",
    "front_left_door",
    "front_right_door",
    "hood",
    "trunk",
    "roof",
    "roof_edge_left",
    "roof_edge_right",
    "right_step",
    "left_step",
]

# -----------------------------
# Sidebar – Damage selection
# -----------------------------
st.sidebar.header("damage selection")

damage_values = {}
for part in parts:
    damage_values[part] = st.sidebar.selectbox(
        part.replace("_", " "),
        ["none", "scratch", "dent", "scratch + dent"],
        index=0
    )

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# Build CSS to activate markers
# -----------------------------
style = "<style>"

for part, damage in damage_values.items():
    anchor = f"#anchor_{part}"

    if damage == "scratch":
        style += f"""
        {anchor} {{
            opacity: 1 !important;
            fill: none !important;
            stroke: #ff9800 !important;
            stroke-width: 2 !important;
        }}
        """

    elif damage == "dent":
        style += f"""
        {anchor} {{
            opacity: 1 !important;
            fill: #e53935 !important;
            stroke: #b71c1c !important;
            stroke-width: 1 !important;
        }}
        """

    elif damage == "scratch + dent":
        style += f"""
        {anchor} {{
            opacity: 1 !important;
            fill: #e53935 !important;
            stroke: #ff9800 !important;
            stroke-width: 2 !important;
            stroke-dasharray: 4 2 !important;
        }}
        """

# Default = none → stays invisible
style += "</style>"

# -----------------------------
# Display SVG
# -----------------------------
st.markdown(style + svg, unsafe_allow_html=True)

# -----------------------------
# Legend
# -----------------------------
st.markdown("""
### 🔍 damage legend
- 🟠 **scratch** → surface damage (visual indicator only)
- 🔴 **dent** → body deformation
- 🔴🟠 **scratch + dent** → combined damage  
*(hover markers later can open real photos)*
""")
