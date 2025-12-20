import streamlit as st
import re

st.set_page_config(layout="wide")
st.title("🚗 car body paint & damage inspection")

# -----------------------------
# Parts
# -----------------------------
parts = [
    "rear_left_fender",
    "rear_right_fender",
    "rear_left_door",
    "rear_right_door",
]

damage_options = ["none", "scratch", "dent", "scratch + dent"]

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("damage selection")
damage = {
    part: st.sidebar.selectbox(
        part.replace("_", " "),
        damage_options,
        index=0
    )
    for part in parts
}

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# 🔴 REMOVE XML HEADER (CRITICAL)
svg = re.sub(r"<\?xml.*?\?>", "", svg).strip()

# -----------------------------
# Marker visibility logic
# -----------------------------
show_scratch = any(v in ["scratch", "scratch + dent"] for v in damage.values())
show_dent = any(v in ["dent", "scratch + dent"] for v in damage.values())

# -----------------------------
# Inject CSS INSIDE SVG
# -----------------------------
style = f"""
<style>
#scratch_marker {{
    opacity: {1 if show_scratch else 0};
    fill: #ff9f43;
}}

#dent_marker {{
    opacity: {1 if show_dent else 0};
    fill: #e63946;
}}
</style>
"""

# Inject style right after <svg>
svg = svg.replace("<svg", f"<svg>{style}", 1)

# -----------------------------
# Display
# -----------------------------
st.markdown(svg, unsafe_allow_html=True)

# -----------------------------
# Legend
# -----------------------------
st.markdown("""
### 🔍 damage legend
- 🟠 **scratch** → surface mark (visual indicator)
- 🔴 **dent** → localized deformation
- 🟠🔴 **scratch + dent** → combined condition  

*(markers guide user to inspect real photos carefully)*
""")
