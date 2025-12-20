import streamlit as st
import re

st.set_page_config(layout="wide")
st.title("🚗 car body paint & damage inspection")

# -----------------------------
# Parts (must match anchor IDs)
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
    "left_step",
    "right_step",
]

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("damage selection")

damage = {}
for part in parts:
    damage[part] = st.sidebar.selectbox(
        part.replace("_", " "),
        ["none", "scratch", "dent", "scratch + dent"],
        0
    )

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# Build SVG-INTERNAL styles
# -----------------------------
svg_style = "<style>\n"

for part, value in damage.items():
    anchor = f"#anchor_{part}"

    if value == "scratch":
        svg_style += f"""
        {anchor} {{
            opacity: 1;
            fill: none;
            stroke: #ff9800;
            stroke-width: 2;
        }}
        """

    elif value == "dent":
        svg_style += f"""
        {anchor} {{
            opacity: 1;
            fill: #e53935;
            stroke: #b71c1c;
            stroke-width: 1;
        }}
        """

    elif value == "scratch + dent":
        svg_style += f"""
        {anchor} {{
            opacity: 1;
            fill: #e53935;
            stroke: #ff9800;
            stroke-width: 2;
            stroke-dasharray: 4 2;
        }}
        """

svg_style += "\n</style>"

# -----------------------------
# Inject style INSIDE SVG
# -----------------------------
svg = re.sub(
    r"(<svg[^>]*>)",
    r"\1\n" + svg_style,
    svg,
    count=1
)

# -----------------------------
# Render
# -----------------------------
st.markdown(svg, unsafe_allow_html=True)

# -----------------------------
# Legend
# -----------------------------
st.markdown("""
### 🔍 damage legend
- 🟠 **scratch** → surface damage (visual indicator)
- 🔴 **dent** → localized deformation
- 🔴🟠 **scratch + dent** → combined condition  
*(markers guide user to inspect real photos carefully)*
""")
