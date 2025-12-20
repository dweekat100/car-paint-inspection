import streamlit as st

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
# Load SVG (UNCHANGED)
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# Build INTERNAL SVG styles
# -----------------------------
style_lines = ["<style>"]

for part, value in damage.items():
    anchor = f"#anchor_{part}"

    if value == "scratch":
        style_lines.append(f"""
        {anchor} {{
            opacity: 1;
            fill: none;
            stroke: #ff9800;
            stroke-width: 2;
        }}
        """)

    elif value == "dent":
        style_lines.append(f"""
        {anchor} {{
            opacity: 1;
            fill: #e53935;
            stroke: #b71c1c;
            stroke-width: 1;
        }}
        """)

    elif value == "scratch + dent":
        style_lines.append(f"""
        {anchor} {{
            opacity: 1;
            fill: #e53935;
            stroke: #ff9800;
            stroke-width: 2;
            stroke-dasharray: 4 2;
        }}
        """)

style_lines.append("</style>")
style_block = "\n".join(style_lines)

# -----------------------------
# SAFE INSERT (NO REGEX)
# -----------------------------
svg = svg.replace("<svg", "<svg\n" + style_block, 1)

# -----------------------------
# Render SVG
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
