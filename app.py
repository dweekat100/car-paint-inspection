import streamlit as st

st.set_page_config(layout="wide")
st.title("🚗 Car Paint Thickness Inspection")

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
fl = st.sidebar.number_input("Front Left Door", 0, 1000, 220)
rl = st.sidebar.number_input("Rear Left Door", 0, 1000, 260)
fr = st.sidebar.number_input("Front Right Door", 0, 1000, 210)
rr = st.sidebar.number_input("Rear Right Door", 0, 1000, 310)

html = f"""
<div style="position:relative;width:800px;margin:auto;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/3e/Sedan_car_top_view.svg"
       style="width:800px;">

  <!-- Hood -->
  <div style="position:absolute;top:80px;left:260px;width:280px;height:80px;
              background:{color(hood)};opacity:0.7;"></div>

  <!-- Roof -->
  <div style="position:absolute;top:160px;left:300px;width:200px;height:100px;
              background:{color(roof)};opacity:0.7;"></div>

  <!-- Trunk -->
  <div style="position:absolute;top:270px;left:260px;width:280px;height:80px;
              background:{color(trunk)};opacity:0.7;"></div>

  <!-- Doors -->
  <div style="position:absolute;top:160px;left:200px;width:60px;height:140px;
              background:{color(fl)};opacity:0.7;"></div>

  <div style="position:absolute;top:160px;left:140px;width:60px;height:140px;
              background:{color(rl)};opacity:0.7;"></div>

  <div style="position:absolute;top:160px;left:540px;width:60px;height:140px;
              background:{color(fr)};opacity:0.7;"></div>

  <div style="position:absolute;top:160px;left:600px;width:60px;height:140px;
              background:{color(rr)};opacity:0.7;"></div>
</div>
"""

st.components.v1.html(html, height=420)
