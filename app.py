import streamlit as st
import base64
import os

st.set_page_config(layout="wide")
st.title("🚗 car body paint inspection")

# -----------------------------
# Parts
# -----------------------------
parts = [
    "rear_left_fender",
    "rear_right_fender",
    "rear_left_door",
    "rear_right_door",
]

# -----------------------------
# Label positions (SVG coords)
# -----------------------------
LABEL_POSITIONS = {
    "rear_left_fender": (140, 220),
    "rear_right_fender": (360, 220),
    "rear_left_door": (150, 300),
    "rear_right_door": (350, 300),
}

# -----------------------------
# Paint colors
# -----------------------------
PAINT_COLORS = {
    "original": "#9BE7A4",
    "repainted": "#46B36B",
    "heavy repair": "#1F7A4A",
}

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Inspection input")
inspection = {}

for part in parts:
    st.sidebar.subheader(part.replace("_", " ").title())

    paint = st.sidebar.selectbox(
        "Paint condition",
        list(PAINT_COLORS.keys()),
        key=f"{part}_paint"
    )

    scratch = st.sidebar.checkbox("Scratch", key=f"{part}_scratch")
    dent = st.sidebar.checkbox("Dent", key=f"{part}_dent")

    inspection[part] = {
        "paint": paint,
        "scratch": scratch,
        "dent": dent
    }

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# Helper: image to base64
# -----------------------------
def img_to_base64(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

# -----------------------------
# CSS
# -----------------------------
style = "<style>"

# paint
for part, data in inspection.items():
    style += f"""
    #{part} {{
        fill: {PAINT_COLORS[data['paint']]} !important;
    }}
    """

# tooltip
style += """
.damage-label {
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
}

.tooltip {
    position: absolute;
    background: white;
    border: 1px solid #ccc;
    padding: 6px;
    display: none;
    z-index: 1000;
}

.label-wrapper:hover .tooltip {
    display: block;
}
</style>
"""

# -----------------------------
# Inject labels into SVG
# -----------------------------
labels_svg = ""

for part, data in inspection.items():
    if part not in LABEL_POSITIONS:
        continue

    x, y = LABEL_POSITIONS[part]

    for damage in ["scratch", "dent"]:
        if not data[damage]:
            continue

        img_path = f"damage_images/{part}_{damage}.jpg"
        img64 = img_to_base64(img_path)

        if not img64:
            continue

        labels_svg += f"""
        <foreignObject x="{x}" y="{y}" width="120" height="40">
            <div xmlns="http://www.w3.org/1999/xhtml" class="label-wrapper">
                <span class="damage-label">{damage.title()}</span>
                <div class="tooltip">
                    <img src="data:image/jpeg;base64,{img64}" width="200"/>
                </div>
            </div>
        </foreignObject>
        """

# insert labels before closing svg
svg = svg.replace("</svg>", labels_svg + "</svg>")

# -----------------------------
# Display
# -----------------------------
st.markdown(style + svg, unsafe_allow_html=True)

# -----------------------------
# Legend
# -----------------------------
st.markdown("""
### Legend
- **Color** → paint condition  
- **Text label** → localized issue  
- **Hover label** → view real photo
""")
