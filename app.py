import streamlit as st
import streamlit.components.v1 as components

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
<div style="display:flex; justify-content:center;">
<svg width="900" height="380" viewBox="0 0 900 380" xmlns="http://www.w3.org/2000/svg">

  <!-- LEFT SIDE -->
  <path d="M70,70 C30,150 30,230 70,310 L140,330 L180,260 L180,120 L140,50 Z"
        fill="{get_color(values['fl_door'])}" />

  <path d="M140,50 L220,40 L250,110 L250,270 L220,340 L140,330 Z"
        fill="{get_color(values['rl_door'])}" />

  <!-- TOP VIEW -->
  <path d="M380,30 C440,0 520,0 580,30 L560,110 L400,110 Z"
        fill="{get_color(values['hood'])}" />

  <path d="M400,110 C450,80 510,80 560,110 L560,250 L400,250 Z"
        fill="{get_color(values['roof'])}" />

  <path d="M400,250 L560,250 L580,330 C520,360 440,360 380,330 Z"
        fill="{get_color(values['trunk'])}" />

  <!-- RIGHT SIDE -->
  <path d="M720,40 L760,50 L760,330 L720,340 L690,270 L690,110 Z"
        fill="{get_color(values['rr_door'])}" />

  <path d="M760,50 L830,70 C870,150 870,230 830,310 L760,330 Z"
        fill="{get_color(values['fr_door'])}" />

</svg>
</div>
"""

# Display diagram
components.html(svg, height=420)

# Legend
st.markdown("""
### 🎨 Legend
- 🟢 **60–160 µm** → Original Paint  
- 🟩 **161–300 µm** → Repainted  
- ⬛ **301+ µm** → Heavy Repair / Filler
""")
