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
# Color logic
# -----------------------------
# 'def get_color(v):
#     'if v <= 160:
#        ' return "#8EE4A1"
#     'elif v <= 300:
#        ' return "#3FAF6C"
#     'else:
#         'return "#0B3D1F"

def get_color(condition):
    return {
        "Original paint": "#8EE4A1",
        "Repainted": "#3FAF6C",
        "Heavy repair / filler": "#0B3D1F",
    }[condition]

# -----------------------------
# Sidebar inputs
# -----------------------------
# 'st.sidebar.header("paint thickness input (µm)")
# 'values = {}

# 'for part in parts:
#     'values[part] = st.sidebar.number_input(
#        ' part,
#        ' min_value=0,
#        ' max_value=2000,
#         'value=120,
#        ' step=10
#    ' )
st.sidebar.header("paint condition")

values = {}

options = [
    "Original paint",
    "Repainted",
    "Heavy repair / filler",
]

for part in parts:
    values[part] = st.sidebar.selectbox(
        part.replace("_", " "),
        options,
        index=0
    )
# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# CSS color injection
# -----------------------------
# 'style = "<style>"
# 'for part, val in values.items():
#     'style += (
#       '  f"#{part} {{ "
#        ' f"fill: {get_color(val)} !important; "
#        ' f"}} "
#    ' )
# 'style += "</style>"
style = "<style>"
for part, condition in values.items():
    style += (
        f"#{part} {{ "
        f"fill: {get_color(condition)} !important; "
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
