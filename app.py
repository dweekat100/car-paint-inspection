import streamlit as st

st.set_page_config(layout="wide")
st.title("🚗 car body paint inspection")

# -----------------------------
# Parts (SVG IDs must match)
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
]

# -----------------------------
# Color logic (paint only)
# -----------------------------
def paint_color(condition):
    return {
        "original": "#9BE7A4",
        "repainted": "#46B36B",
        "heavy repair": "#1F7A4A"
    }[condition]

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("Inspection input")

inspection = {}

for part in parts:
    st.sidebar.subheader(part.replace("_", " ").title())

    paint = st.sidebar.selectbox(
        "Paint condition",
        ["original", "repainted", "heavy repair"],
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
# CSS Injection (IMPORTANT)
# -----------------------------
style = "<style>"

for part, data in inspection.items():
    # Paint fill
    style += f"""
    #{part} {{
        fill: {paint_color(data['paint'])} !important;
    }}
    """

    # Scratch (soft dashed)
    if data["scratch"]:
        style += f"""
        #{part} {{
            stroke: #f59e0b !important;
            stroke-width: 3 !important;
            stroke-dasharray: 6,4;
        }}
        """

    # Dent (stronger dotted)
    if data["dent"]:
        style += f"""
        #{part} {{
            stroke: #ef4444 !important;
            stroke-width: 4 !important;
            stroke-dasharray: 2,6;
        }}
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
### Legend
- **Fill color** → paint condition  
- **Dashed border** → scratch (see photos)  
- **Dotted border** → dent (see photos)
""")
