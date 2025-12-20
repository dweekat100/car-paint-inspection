import streamlit as st

st.set_page_config(layout="wide")
st.title("🚗 car body paint & damage inspection")

# -----------------------------
# Parts (must match your logic)
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

damage = {}
for part in parts:
    damage[part] = st.sidebar.selectbox(
        part.replace("_", " "),
        damage_options,
        index=0
    )

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# CSS CONTROL (THE FIX)
# -----------------------------
style = """
<style>
#scratch_marker {
    opacity: 0;
    fill: #ff8c42;
}

#dent_marker {
    opacity: 0;
    fill: #e63946;
}
</style>
"""

# Enable markers if ANY part uses them
show_scratch = any(v in ["scratch", "scratch + dent"] for v in damage.values())
show_dent = any(v in ["dent", "scratch + dent"] for v in damage.values())

if show_scratch:
    style += """
    <style>
    #scratch_marker { opacity: 1; }
    </style>
    """

if show_dent:
    style += """
    <style>
    #dent_marker { opacity: 1; }
    </style>
    """

# -----------------------------
# Display
# -----------------------------
st.markdown(style + svg, unsafe_allow_html=True)

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
