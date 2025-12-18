import streamlit as st

st.set_page_config(layout="wide")
st.title("car body paint inspection")

# --------------------------------
# PART DEFINITIONS
# --------------------------------
PARTS = {
    "rear_left_fender": "rear left fender",
    "rear_right_fender": "rear right fender",
    "rear_left_door": "rear left door",
    "rear_right_door": "rear right door",
    "front_left_fender": "front left fender",
    "front_right_fender": "front right fender",
    "front_left_door": "front left door",
    "front_right_door": "front right door",
    "hood": "hood",
    "trunk": "trunk",
    "roof": "roof",
    "roof_edge_left": "roof edge left",
    "roof_edge_right": "roof edge right",
}

RESULT_COLORS = {
    "ok": "#4CAF50",
    "repainted": "#FFC107",
    "damaged": "#F44336"
}

# --------------------------------
# LOAD SVG
# --------------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg_template = f.read()

# --------------------------------
# USER INPUT
# --------------------------------
st.sidebar.header("inspection results")

results = {}
for part_id, display_name in PARTS.items():
    results[part_id] = st.sidebar.selectbox(
        display_name,
        ["ok", "repainted", "damaged"],
        index=0
    )

# --------------------------------
# APPLY COLORS
# --------------------------------
svg_colored = svg_template

for part_id, status in results.items():
    color = RESULT_COLORS[status]
    svg_colored = svg_colored.replace(
        f'id="{part_id}"',
        f'id="{part_id}" fill="{color}"'
    )

# --------------------------------
# DISPLAY SVG
# --------------------------------
st.subheader("inspection result (top view)")
st.components.v1.html(svg_colored, height=700)
