import streamlit as st
from pathlib import Path

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 Car body paint inspection")

# -----------------------------
# Parts (MUST MATCH SVG IDs)
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
]

# -----------------------------
# Color logic
# -----------------------------
def paint_color(condition):
    return {
        "original": "#9BE7A2",
        "repainted": "#3FAF6C",
        "heavy_repair": "#1F6F43",
    }[condition]

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("Inspection input")

paint = {}
scratch = {}
dent = {}

for part in parts:
    st.sidebar.subheader(part.replace("_", " ").title())

    paint[part] = st.sidebar.selectbox(
        "Paint condition",
        ["original", "repainted", "heavy_repair"],
        key=f"paint_{part}",
    )

    scratch[part] = st.sidebar.checkbox(
        "Scratch",
        key=f"scratch_{part}",
    )

    dent[part] = st.sidebar.checkbox(
        "Dent",
        key=f"dent_{part}",
    )

# -----------------------------
# Load SVG (ABSOLUTE SAFE LOAD)
# -----------------------------
svg_path = Path("car top view svg.svg")
svg = svg_path.read_text(encoding="utf-8")

# -----------------------------
# Build CSS
# -----------------------------
css = "<style>"

for part in parts:
    css += f"""
    #{part} {{
        fill: {paint_color(paint[part])} !important;
        stroke: #444;
        stroke-width: 1;
    }}
    """

    if scratch[part]:
        css += f"""
        #{part} {{
            stroke-dasharray: 5 4;
        }}
        """

    if dent[part]:
        css += f"""
        #{part} {{
            stroke-width: 2.5;
            stroke-dasharray: 2 6;
        }}
        """

css += "</style>"

# -----------------------------
# FINAL RENDER (THIS IS THE KEY)
# -----------------------------
st.components.v1.html(
    css + svg,
    height=700,
    scrolling=False,
)

# -----------------------------
# Legend
# -----------------------------
st.markdown(
    """
### Legend
- 🟢 Original paint
- 🟢🟩 Repainted
- 🟢⬛ Heavy repair
- ┄ Scratch (dashed border)
- ·· Dent (thicker dotted border)
"""
)
