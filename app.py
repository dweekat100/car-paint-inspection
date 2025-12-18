import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 car body paint thickness inspection")

# -----------------------------
# Parts (MUST MATCH SVG IDs EXACTLY)
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
        return "#8EE4A1"
    elif value <= 300:
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
# Load SVG file
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg_content = f.read()

# -----------------------------
# Build FORCE CSS (IMPORTANT)
# -----------------------------
css = "<style>\n"

for part, thickness in values.items():
    css += f'''
    #{part} {{
        fill: {get_color(thickness)} !important;
        stroke: #ffffff;
        stroke-width: 1;
    }}
    '''

css += "</style>\n"

# -----------------------------
# Render SVG with CSS injected
# -----------------------------
st.markdown(css + svg_content, unsafe_allow_html=True)

# -----------------------------
# Legend
# -----------------------------
st.markdown("""
### 🎨 legend
- 🟢 ≤160 µm → original paint  
- 🟩 161–300 µm → repainted  
- ⬛ >300 µm → heavy repair / filler
""")
