import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 car body paint thickness inspection")

# -----------------------------
# Parts (SVG IDs)
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
    "roof_edg_Left",
    "roof_edg_right",
]

# -----------------------------
# Paint color logic
# -----------------------------
def paint_color(state):
    return {
        "original": "#8EE4A1",
        "repainted": "#3FAF6C",
        "heavy repair": "#0B3D1F"
    }[state]

# -----------------------------
# Sidebar input
# -----------------------------
st.sidebar.header("inspection input")

paint = {}
scratch = {}
dent = {}

for part in parts:
    st.sidebar.subheader(part.replace("_", " ").title())

    paint[part] = st.sidebar.selectbox(
        "paint condition",
        ["original", "repainted", "heavy repair"],
        key=f"paint_{part}"
    )

    scratch[part] = st.sidebar.checkbox("scratch", key=f"s_{part}")
    dent[part] = st.sidebar.checkbox("dent", key=f"d_{part}")

# -----------------------------
# Load SVG
# ----------------------
