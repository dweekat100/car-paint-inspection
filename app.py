import streamlit as st
import re

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 car body paint thickness inspection")

# -----------------------------
# Parts
# key   = SVG id (NO SPACES)
# value = display name (WITH SPACES)
# -----------------------------
parts = {
    "rear_left_fender": "rear left fender",
    "rear_right_fender": "rear right fender",
    "rear_left_door": "rear left door",
    "rear_right_door": "rear right door",
    "front_left_fender": "front left fender",
    "front_right_fender": "front right fender",
    "front_left_door": "front left door",
    "front_right_door": "front right door",
    "hood": "hood",
    "trunk": "trunk",
    "roof": "roof",
    "roof_edge_left": "roof edge left",
    "roof_edge_right": "roof edge right",
}

# -----------------------------
# Color logic
# -----------------------------
def get_color(value):
    if value <= 160:
        return "#8EE4A1"   # original paint
    elif value <= 300:
        return "#3FAF6C"   # repainted
    else:
        return "#0B3D1F"   # heavy repair

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("paint thickness input (µm)")
values = {}

for part_id, display_name in parts.items():
    values[part_id] = st.sidebar.number_input(
        display_name,
        min_value=0,
        max_value=1000,
        value=120,
        step=1
    )

# -----------------------------
# Load SVG file
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg_template = f.read()

# -----------------------------
# Apply colors to SVG (CORRECT WAY)
# -----------------------------

def set_svg_fill(svg, part_id, color):
    # remove fill from style attribute if it exists
    svg = re.sub(
        rf'(id="{part_id}"[^>]*style="[^"]*)fill:[^;"]*;?',
        rf'\1',
        svg
    )

    # replace existing fill attribute
    if re.search(rf'id="{part_id}"[^>]*fill=', svg):
        svg = re.sub(
            rf'(id="{part_id}"[^>]*fill=")[^"]*(")',
            rf'\1{color}\2',
            svg
        )
    else:
        # inject fill attribute if missing
        svg = re.sub(
            rf'(id="{part_id}")',
            rf'\1 fill="{color}"',
            svg
        )

    return svg


# -----------------------------
# Apply colors to SVG (FINAL)
# -----------------------------
svg_colored = svg_template

for part_id, thickness in values.items():
    color = get_color(thickness)
    svg_colored = set_svg_fill(svg_colored, part_id, color)

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
