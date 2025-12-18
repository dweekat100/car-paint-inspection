import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 car body paint thickness inspection")

# -----------------------------
# Parts (SVG IDs MUST MATCH)
# -----------------------------
parts = [
    "rear left fender",
    "rear right fender",
    "rear left door",
    "rear right door",
    "front left fender",
    "front right fender",
    "front left door",
    "front right door",
    "hood",
    "trunk",
    "roof",
    "roof edge left",
    "roof edge right",
]

# -----------------------------
# Color logic
# -----------------------------
def get_color(v):
    if v <= 160:
        return "#8EE4A1"
    elif v <= 300:
        return "#3FAF6C"
    else:
        return "#0B3D1F"

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("paint thickness input (µm)")
values = {}

for part in parts:
    values[part] = st.sidebar.number_input(
        part,
        min_value=0,
        max_value=2000,
        value=120,
        step=10
    )

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# CSS color injection
# -----------------------------
style = "<style>"
for part, val in values.items():
    style += (
        f"#{part} {{ "
        f"fill: {get_color(val)} !important; "
        f"}} "
    )
style += "</style>"

# -----------------------------
# Display SVG
# -----------------------------
st.markdown(style + svg, unsafe_allow_html=True)

# -----------------------------
# Legend (SAFE STRING)
# -----------------------------
st.markdown(
    "### legend\n"
    "- ≤160 µm → original paint\n"
    "- 161–300 µm → repainted\n"
    "- >300 µm → heavy repair / filler"
)
