import streamlit as st

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("🚗 car body inspection (paint / scratch / dent)")

# -----------------------------
# Parts list (MUST match SVG IDs)
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
]

# -----------------------------
# Sidebar damage selection
# -----------------------------
st.sidebar.header("damage selection")

damage = {}
for part in parts:
    damage[part] = st.sidebar.selectbox(
        part.replace("_", " ").title(),
        ["none", "scratch", "dent", "both"],
        index=0
    )

# -----------------------------
# Load SVG
# -----------------------------
with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# -----------------------------
# CSS injection (THIS IS THE FIX)
# -----------------------------
style = "<style>"

for part, value in damage.items():

    scratch_id = f"#scratch_{part}"
    dent_id = f"#dent_{part}"

    if value == "scratch":
        style += f"""
        {scratch_id} {{
            opacity: 1 !important;
            stroke: #e67e22;
            stroke-width: 2.5;
        }}
        """

    elif value == "dent":
        style += f"""
        {dent_id} {{
            opacity: 1 !important;
            stroke: #c0392b;
            stroke-width: 2.5;
        }}
        """

    elif value == "both":
        style += f"""
        {scratch_id}, {dent_id} {{
            opacity: 1 !important;
            stroke-width: 2.5;
        }}
        {scratch_id} {{ stroke: #e67e22; }}
        {dent_id} {{ stroke: #c0392b; }}
        """

style += "</style>"

# -----------------------------
# Display SVG
# -----------------------------
st.markdown(style + svg, unsafe_allow_html=True)

# -----------------------------
# Legend
# -----------------------------
st.markdown("""
### ℹ️ legend
- **scratch** → light surface mark (partial)
- **dent** → soft deformation (localized)
- **both** → combined condition  
*(markers indicate area to inspect photos more carefully)*
""")
