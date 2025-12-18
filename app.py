import streamlit as st

st.set_page_config(layout="wide")
st.title("🚗 car body paint thickness inspection")

# -----------------------------
# Parts list (EXACT SVG IDs)
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
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# Inject colors (WORKING WAY)
# -----------------------------
for part, thickness in values.items():
    color = get_color(thickness)
    svg = svg.replace(
        f'id="{part}"',
        f'id="{part}" style="fill:{color};"'
    )

# -----------------------------
# Display SVG
# -----------------------------
st.markdown(svg, unsafe_allow_html=True)

# -----------------------------
# Legend
# -----------------------------
st.markdown("""
### 🎨 legend
- 🟢 ≤160 µm → original paint  
- 🟩 161–300 µm → repainted  
- ⬛ >300 µm → heavy repair / filler
""")
