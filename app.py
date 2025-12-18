import streamlit as st
import xml.etree.ElementTree as ET
from io import StringIO

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 car body paint thickness inspection")

# -----------------------------
# Parts (SVG IDs)
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
def get_color(value):
    if value <= 160:
        return "#8EE4A1"   # original
    elif value <= 300:
        return "#3FAF6C"   # repainted
    else:
        return "#0B3D1F"   # heavy repair

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("paint thickness input (µm)")
values = {}

for part in parts:
    values[part] = st.sidebar.number_input(
        part,
        min_value=0,
        max_value=1000,
        value=120,
        step=1
    )

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg_data = f.read()

# -----------------------------
# Parse SVG properly (THIS IS THE FIX)
# -----------------------------
ET.register_namespace("", "http://www.w3.org/2000/svg")
tree = ET.ElementTree(ET.fromstring(svg_data))
root = tree.getroot()

# -----------------------------
# Apply colors by ID
# -----------------------------
for element in root.iter():
    part_id = element.attrib.get("id")
    if part_id in values:
        color = get_color(values[part_id])

        # remove style fill if exists
        style = element.attrib.get("style", "")
        style = ";".join(
            s for s in style.split(";") if not s.strip().startswith("fill:")
        )

        # apply new fill
        element.set("style", f"{style};fill:{color}")
        element.set("fill", color)

# -----------------------------
# Convert SVG back to string
# -----------------------------
output = StringIO()
tree.write(output, encoding="unicode")
svg_colored = output.getvalue()

# -----------------------------
# Display SVG
# -----------------------------
st.markdown(svg_colored, unsafe_allow_html=True)

# -----------------------------
# Legend
# -----------------------------
st.markdown("""
### 🎨 legend
- 🟢 **≤160 µm** → original paint  
- 🟩 **161–300 µm** → repainted  
- ⬛ **>300 µm** → heavy repair / filler
""")
