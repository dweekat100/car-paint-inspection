import streamlit as st
import re

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 car body inspection (paint / scratch / dent)")

# -----------------------------
# Parts (base names only)
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
# Sidebar input
# -----------------------------
st.sidebar.header("damage selection")

damage = {}
for part in parts:
    damage[part] = st.sidebar.selectbox(
        part.replace("_", " "),
        ["none", "scratch", "dent", "both"],
        index=0
    )

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# Extract anchor positions
# -----------------------------
anchor_pattern = re.compile(
    r'id="(?P<id>[\w_]+)_anchor".*?cx="(?P<cx>[\d.]+)".*?cy="(?P<cy>[\d.]+)"'
)

anchors = {}
for match in anchor_pattern.finditer(svg):
    anchors[match.group("id")] = (
        float(match.group("cx")),
        float(match.group("cy"))
    )

# -----------------------------
# Build markers SVG
# -----------------------------
OFFSET = 12  # visual offset
markers_svg = ""

for part, state in damage.items():
    if part not in anchors or state == "none":
        continue

    x, y = anchors[part]

    if state in ("scratch", "both"):
        markers_svg += f'''
        <use href="#scratch_marker"
             transform="translate({x} {y - OFFSET})"
             opacity="1"/>
        '''

    if state in ("dent", "both"):
        markers_svg += f'''
        <use href="#dent_marker"
             transform="translate({x} {y + OFFSET})"
             opacity="1"/>
        '''

# -----------------------------
# Inject markers before </svg>
# -----------------------------
final_svg = svg.replace("</svg>", markers_svg + "\n</svg>")

# -----------------------------
# Display SVG
# -----------------------------
st.markdown(final_svg, unsafe_allow_html=True)

# -----------------------------
# Legend
# -----------------------------
st.markdown("""
### 🛈 legend
- **scratch** → light surface mark (partial)
- **dent** → soft deformation (localized)
- **both** → combined condition  
*(visual markers indicate area to inspect photos more carefully)*
""")
