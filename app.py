import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("🚗 Car Paint Thickness – Sedan (Full Panels)")

def color(v):
    if v <= 160:
        return "#7EE3A1"
    elif v <= 300:
        return "#3BAE6A"
    else:
        return "#0B5D2A"

st.sidebar.header("Paint Thickness (µm)")

hood = st.sidebar.number_input("Hood", 0, 1000, 120)
roof = st.sidebar.number_input("Roof", 0, 1000, 180)
trunk = st.sidebar.number_input("Trunk", 0, 1000, 140)

fl_fender = st.sidebar.number_input("Front Left Fender", 0, 1000, 150)
fr_fender = st.sidebar.number_input("Front Right Fender", 0, 1000, 150)
rl_fender = st.sidebar.number_input("Rear Left Fender", 0, 1000, 170)
rr_fender = st.sidebar.number_input("Rear Right Fender", 0, 1000, 170)

fl = st.sidebar.number_input("Front Left Door", 0, 1000, 220)
rl = st.sidebar.number_input("Rear Left Door", 0, 1000, 260)
fr = st.sidebar.number_input("Front Right Door", 0, 1000, 210)
rr = st.sidebar.number_input("Rear Right Door", 0, 1000, 310)

svg = f"""
<svg viewBox="0 0 800 400" width="800" style="display:block;margin:auto">

  <!-- Hood -->
  <polygon points="300,40 500,40 550,100 250,100"
           fill="{color(hood)}" stroke="#333"/>

  <!-- Front Left Fender -->
  <polygon points="250,100 300,100 300,200 240,180"
           fill="{color(fl_fender)}" stroke="#333"/>

  <!-- Front Right Fender -->
  <polygon points="500,100 550,100 560,180 500,200"
           fill="{color(fr_fender)}" stroke="#333"/>

  <!-- Roof -->
  <polygon points="320,100 480,100 520,200 280,200"
           fill="{color(roof)}" stroke="#333"/>

  <!-- Rear Left Fender -->
  <polygon points="240,200 300,200 300,270 260,260"
           fill="{color(rl_fender)}" stroke="#333"/>

  <!-- Rear Right Fender -->
  <polygon points="500,200 560,180 540,260 500,270"
           fill="{color(rr_fender)}" stroke="#333"/>

  <!-- Trunk -->
  <polygon points="250,200 550,200 500,270 300,270"
           fill="{color(trunk)}" stroke="#333"/>

  <!-- Front Left Door -->
  <polygon points="220,110 280,110 280,200 220,200"
           fill="{color(fl)}" stroke="#333"/>

  <!-- Rear Left Door -->
  <polygon points="160,110 220,110 220,200 160,200"
           fill="{color(rl)}" stroke="#333"/>

  <!-- Front Right Door -->
  <polygon points="520,110 580,110 580,200 520,200"
           fill="{color(fr)}" stroke="#333"/>

  <!-- Rear Right Door -->
  <polygon points="580,110 640,110 640,200 580,200"
           fill="{color(rr)}" stroke="#333"/>

  <!-- Car Outline -->
  <path d="M200 40 H600 L680 120 V260 L600 320 H200 L120 260 V120 Z"
        fill="none" stroke="#000" stroke-width="4"/>

</svg>
"""

components.html(svg, height=460)
