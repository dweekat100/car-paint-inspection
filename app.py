import streamlit as st
import streamlit.components.v1 as components

with open("car top view svg.svg") as f:
    svg = f.read()

components.html(svg, height=500)
