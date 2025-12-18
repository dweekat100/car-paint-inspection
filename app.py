import streamlit as st

st.set_page_config(layout="wide")
st.title("🚗 car body paint thickness inspection")

parts = [
    "rear left fender",
    "rear right fender",
    "rear left door",
    "rear right door",
    "front left fender",
    "front right fender",
    "front left door",
    "front right door",
    "hood",
    "trunk",
    "roof",
    "roof edge left",
    "roof edge right",
]

def get_color(v):
    if v <= 160:
        return "#8EE4A1"
    elif v <= 300:
        return "#3FAF6C"
    else:
        return "#0B3D1F"

st.sidebar.header("paint thickness input (µm)")
values = {
    part: st.sidebar.number_input(
        part, 0, 2000, 120, 10
    )
    for part in parts
}

with open("car top view svg.svg", "r", encoding="utf-8") as f:
    svg = f.read()

css = "<style>"
for part, value in values.items():
    css += f"""
    #{part} {{
        fill: {get_color(value)} !important;
    }}
    """
css += "</style>"

st.markdown(css + svg, unsafe_allow_html=True)

st.markdown("""
### 🎨 legend
- 🟢 ≤160 µm → original paint  
- 🟩 161–300 µm → repainted  
- ⬛ >300 µm → heavy repair / filler
""")

- ⬛ >300 µm → heavy repair / filler
""")
