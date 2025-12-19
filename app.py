import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 car body paint & surface inspection")

# -----------------------------
# Parts (SVG IDs MUST MATCH EXACTLY)
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
# Paint color logic
# -----------------------------
def get_color(condition):
    if condition == "Original paint":
        return "#8EE4A1"
    elif condition == "Repainted":
        return "#3FAF6C"
    else:
        return "#0B3D1F"

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("inspection input")

paint_options = [
    "Original paint",
    "Repainted",
    "Heavy repair / filler",
]

defect_options = [
    "None",
    "Scratch",
    "Denting",
]

paint_values = {}
defect_values = {}

for part in parts:
    st.sidebar.markdown(f"**{part.replace('_', ' ')}**")

    paint_values[part] = st.sidebar.selectbox(
        "Paint condition",
        paint_options,
        key=f"paint_{part}"
    )

    defect_values[part] = st.sidebar.selectbox(
        "Surface defect",
        defect_options,
        key=f"defect_{part}"
    )

    st.sidebar.markdown("---")

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# SVG pattern definitions (SCRATCH & DENTING)
# -----------------------------
pattern_defs = """
<svg width="0" height="0" style="position:absolute">
  <defs>
    <!-- Scratch pattern -->
    <pattern id="scratch" patternUnits="userSpaceOnUse" width="8" height="8">
      <line x1="0" y1="8" x2="8" y2="0" stroke="black" stroke-width="1"/>
    </pattern>

    <!-- Denting pattern -->
    <pattern id="dent" patternUnits="userSpaceOnUse" width="6" height="6">
      <circle cx="3" cy="3" r="1.2" fill="black"/>
    </pattern>
  </defs>
</svg>
"""

# -----------------------------
# Apply CSS styling
# -----------------------------
style = "<style>"

for part in parts:
    paint_color = get_color(paint_values[part])
    defect = defect_values[part]

    if defect == "Scratch":
        fill_value = "url(#scratch)"
    elif defect == "Denting":
        fill_value = "url(#dent)"
    else:
        fill_value = paint_color

    style += f"""
    #{part} {{
        fill: {fill_value} !important;
    }}
    """

style += "</style>"

# -----------------------------
# Display SVG
# -----------------------------
st.markdown(style + pattern_defs + svg, unsafe_allow_html=True)

# -----------------------------
# Legends
# -----------------------------
st.markdown(
    "### 🎨 paint condition legend\n"
    "- Original paint → light green\n"
    "- Repainted → medium green\n"
    "- Heavy repair / filler → dark green\n\n"
    "### 🛠 surface defect legend\n"
    "- Scratch → diagonal lines\n"
    "- Denting → dotted pattern"
)
