import streamlit as st

# Page setup
st.set_page_config(layout="wide")
st.title("🚗 Car Body Paint Thickness Inspection")

# Car body parts
parts = {
    "hood": "Hood",
    "roof": "Roof",
    "trunk": "Trunk",
    "fl_door": "Front Left Door",
    "fr_door": "Front Right Door",
    "rl_door": "Rear Left Door",
    "rr_door": "Rear Right Door"
}

# Color logic based on thickness
def get_color(value):
    if value <= 160:
        return "#8EE4A1"   # Original paint
    elif value <= 300:
        return "#3FAF6C"   # Repainted
    else:
        return "#0B3D1F"   # Heavy repair

# Sidebar input
st.sidebar.header("Paint Thickness Input (µm)")
values = {}

for key, name in parts.items():
    values[key] = st.sidebar.number_input(
        name,
        min_value=0,
        max_value=1000,
        value=120,
        step=1
    )

# SVG car diagram
svg = f"""
<svg width="900" height="400" viewBox="0 0 900 400">

  <!-- ===== LEFT SIDE VIEW ===== -->
  <path d="M50,80 C20,140 20,260 50,320 L120,340 L160,280 L160,120 L120,60 Z"
        fill="{get_color(values['fl_door'])}" stroke="#cfd8dc"/>

  <path d="M120,60 L200,50 L220,100 L220,300 L200,350 L120,340 Z"
        fill="{get_color(values['rl_door'])}" stroke="#cfd8dc"/>

  <!-- ===== TOP VIEW ===== -->
  <!-- Hood -->
  <path d="M350,40 C420,10 480,10 550,40 L530,120 L370,120 Z"
        fill="{get_color(values['hood'])}" stroke="#cfd8dc"/>

  <!-- Roof -->
  <path d="M370,120 C420,90 480,90 530,120 L530,260 L370,260 Z"
        fill="{get_color(values['roof'])}" stroke="#cfd8dc"/>

  <!-- Trunk -->
  <path d="M370,260 L530,260 L550,340 C480,370 420,370 350,340 Z"
        fill="{get_color(values['trunk'])}" stroke="#cfd8dc"/>

  <!-- ===== RIGHT SIDE VIEW ===== -->
  <path d="M740,60 L700,120 L700,280 L740,340 L820,320 C850,260 850,140 820,80 Z"
        fill="{get_color(values['fr_door'])}" stroke="#cfd8dc"/>

  <path d="M680,50 L740,60 L740,340 L680,350 L660,300 L660,100 Z"
        fill="{get_color(values['rr_door'])}" stroke="#cfd8dc"/>

</svg>
"""

# Display diagram
st.markdown(svg, unsafe_allow_html=True)

# Legend
st.markdown("""
### 🎨 Legend
- 🟢 **60–160 µm** → Original Paint  
- 🟩 **161–300 µm** → Repainted  
- ⬛ **301+ µm** → Heavy Repair / Filler
""")
