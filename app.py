import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 car body paint thickness inspection")

# -----------------------------
# Parts (SVG IDs MUST MATCH)
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
def paint_color(state):
    if state == "original":
        return "#8EE4A1"
    elif state == "repainted":
        return "#3FAF6C"
    else:
        return "#0B3D1F"

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("inspection input")

paint_state = {}
scratch_state = {}
dent_state = {}

for part in parts:
    st.sidebar.subheader(part.replace("_", " ").title())

    paint_state[part] = st.sidebar.selectbox(
        "paint condition",
        ["original", "repainted", "heavy repair"],
        key=f"paint_{part}"
    )

    scratch_state[part] = st.sidebar.checkbox(
        "scratch",
        key=f"scratch_{part}"
    )

    dent_state[part] = st.sidebar.checkbox(
        "dent",
        key=f"dent_{part}"
    )

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# Paint coloring via CSS
# -----------------------------
style = "<style>"
for part in parts:
    style += (
        f"#{part} {{ "
        f"fill: {paint_color(paint_state[part])} !important; "
        f"}} "
    )
style += "</style>"

# -----------------------------
# Soft overlay markers (SVG)
# -----------------------------
overlays = ""

for part in parts:
    markers = ""
    if scratch_state[part]:
        markers += "／"
    if dent_state[part]:
        markers += " ●"

    if markers:
        overlays += f"""
        <text
            x="50%"
            y="50%"
            text-anchor="middle"
            dominant-baseline="middle"
            font-size="26"
            fill="#333"
            opacity="0.55"
            pointer-events="none"
        >
            {markers}
        </text>
        """

# -----------------------------
# Inject overlays before </svg>
# -----------------------------
svg = svg.replace("</svg>", overlays + "</svg>")

# -----------------------------
# Display SVG
# -----------------------------
st.markdown(style + svg, unsafe_allow_html=True)

# -----------------------------
# Legend
# -----------------------------
st.markdown(
    """
### 🎨 legend
- **green shades** → paint condition  
- **／** → minor scratch (localized)  
- **●** → localized dent  
*markers indicate attention only – refer to photos for detail*
"""
)
