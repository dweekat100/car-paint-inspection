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
# Defect style logic
# -----------------------------
def get_defect_style(defect):
    if defect == "Scratch":
        return "stroke: #000; stroke-width: 2; stroke-dasharray: 6,4;"
    elif defect == "Denting":
        return "stroke: #000; stroke-width: 2; stroke-dasharray: 2,6;"
    else:
        return ""

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
    st.sidebar.markdown(f"**{part.replace('_',' ')}**")

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
# Apply CSS styling
# -----------------------------
style = "<style>"
for part in parts:
    style += (
        f"#{part} {{ "
        f"fill: {get_color(paint_values[part])} !important; "
        f"{get_defect_style(defect_values[part])} "
        f"}} "
    )
style += "</style>"

# -----------------------------
# Display SVG
# -----------------------------
st.markdown(style + svg, unsafe_allow_html=True)

# -----------------------------
# Legends
# -----------------------------
st.markdown(
    "### 🎨 paint condition legend\n"
    "- Original paint → light green\n"
    "- Repainted → medium green\n"
    "- Heavy repair / filler → dark green\n\n"
    "### 🛠 surface defect legend\n"
    "- Scratch → dashed outline\n"
    "- Denting → dotted outline"
)
