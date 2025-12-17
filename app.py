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
<svg width="500" height="800" viewBox="0 0 500 800">

  <!-- Hood -->
  <rect x="150" y="50" width="200" height="120" fill="{get_color(values['hood'])}" />

  <!-- Roof -->
  <rect x="150" y="200" width="200" height="150" fill="{get_color(values['roof'])}" />

  <!-- Trunk -->
  <rect x="150" y="380" width="200" height="120" fill="{get_color(values['trunk'])}" />

  <!-- Front Left Door -->
  <rect x="80" y="220" width="60" height="130" fill="{get_color(values['fl_door'])}" />

  <!-- Rear Left Door -->
  <rect x="80" y="360" width="60" height="130" fill="{get_color(values['rl_door'])}" />

  <!-- Front Right Door -->
  <rect x="360" y="220" width="60" height="130" fill="{get_color(values['fr_door'])}" />

  <!-- Rear Right Door -->
  <rect x="360" y="360" width="60" height="130" fill="{get_color(values['rr_door'])}" />

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
