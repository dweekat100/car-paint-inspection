import streamlit.components.v1 as components

import streamlit as st

st.set_page_config(page_title="Car Paint Inspection", layout="wide")

st.title("🚗 Car Paint Thickness Inspection")

# --- Color logic ---
def thickness_to_color(value):
    if value <= 160:
        return "#7EE3A1"   # light green
    elif value <= 300:
        return "#3BAE6A"   # medium green
    else:
        return "#0B5D2A"   # dark green

# --- User input ---
st.sidebar.header("Paint Thickness (µm)")

panels = {
    "hood": st.sidebar.number_input("Hood", 0, 1000, 120),
    "roof": st.sidebar.number_input("Roof", 0, 1000, 180),
    "trunk": st.sidebar.number_input("Trunk", 0, 1000, 140),
    "front_left": st.sidebar.number_input("Front Left Door", 0, 1000, 220),
    "rear_left": st.sidebar.number_input("Rear Left Door", 0, 1000, 260),
    "front_right": st.sidebar.number_input("Front Right Door", 0, 1000, 210),
    "rear_right": st.sidebar.number_input("Rear Right Door", 0, 1000, 310),
}

colors = {k: thickness_to_color(v) for k, v in panels.items()}

# --- SVG ---
svg = f"""
<svg viewBox="0 0 800 400" width="100%" xmlns="http://www.w3.org/2000/svg">

  <!-- Car body outline -->
  <rect x="150" y="60" rx="80" ry="80" width="500" height="280" fill="#f4f6f8"/>

  <!-- Hood -->
  <path id="hood"
        d="M300 70 H500 V130 H300 Z"
        fill="{colors['hood']}" stroke="#999"/>

  <!-- Roof -->
  <path id="roof"
        d="M330 130 H470 V210 H330 Z"
        fill="{colors['roof']}" stroke="#999"/>

  <!-- Trunk -->
  <path id="trunk"
        d="M300 210 H500 V270 H300 Z"
        fill="{colors['trunk']}" stroke="#999"/>

  <!-- Left doors -->
  <path id="front_left"
        d="M220 130 H300 V210 H220 Z"
        fill="{colors['front_left']}" stroke="#999"/>

  <path id="rear_left"
        d="M180 150 H220 V230 H180 Z"
        fill="{colors['rear_left']}" stroke="#999"/>

  <!-- Right doors -->
  <path id="front_right"
        d="M500 130 H580 V210 H500 Z"
        fill="{colors['front_right']}" stroke="#999"/>

  <path id="rear_right"
        d="M580 150 H620 V230 H580 Z"
        fill="{colors['rear_right']}" stroke="#999"/>

  <!-- Wheels -->
  <circle cx="260" cy="330" r="28" fill="#ccc"/>
  <circle cx="540" cy="330" r="28" fill="#ccc"/>

</svg>
"""

components.html(svg, height=450)


# --- Legend ---
st.markdown("""
### 🎨 Thickness Legend
- 🟩 **60–160 µm** (Original paint)
- 🟢 **161–300 µm** (Repaint)
- 🟢⬛ **301+ µm** (Heavy repaint / filler)
""")
