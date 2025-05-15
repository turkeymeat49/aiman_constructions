import streamlit as st
from PIL import Image, ImageDraw
import io

st.title("Home Wall Front Design")

st.sidebar.header("Design Options")

# Wall background selection
wall_color = st.sidebar.color_picker("Pick Wall Color", "#f5f5dc")

# Option to upload a background image
uploaded_bg = st.sidebar.file_uploader("Upload Wall Background (optional)", type=["jpg", "jpeg", "png"])

# Canvas size
canvas_width = st.sidebar.slider("Wall Width (px)", 400, 1200, 600)
canvas_height = st.sidebar.slider("Wall Height (px)", 300, 900, 400)

# Add windows/doors
add_window = st.sidebar.checkbox("Add Window")
add_door = st.sidebar.checkbox("Add Door")

# Create base image
if uploaded_bg:
    wall_img = Image.open(uploaded_bg).resize((canvas_width, canvas_height))
else:
    wall_img = Image.new("RGB", (canvas_width, canvas_height), wall_color)

draw = ImageDraw.Draw(wall_img)

# Draw window
if add_window:
    wx = st.sidebar.slider("Window X", 0, canvas_width-100, 100)
    wy = st.sidebar.slider("Window Y", 0, canvas_height-100, 100)
    ww = st.sidebar.slider("Window Width", 50, 200, 100)
    wh = st.sidebar.slider("Window Height", 50, 200, 100)
    draw.rectangle([wx, wy, wx+ww, wy+wh], fill="#87ceeb", outline="black", width=3)

# Draw door
if add_door:
    dx = st.sidebar.slider("Door X", 0, canvas_width-80, 250)
    dy = st.sidebar.slider("Door Y", 0, canvas_height-150, canvas_height-150)
    dw = st.sidebar.slider("Door Width", 50, 120, 80)
    dh = st.sidebar.slider("Door Height", 100, 250, 150)
    draw.rectangle([dx, dy, dx+dw, dy+dh], fill="#deb887", outline="black", width=3)

st.image(wall_img, caption="Wall Design Preview", use_column_width=True)

st.info("You can further enhance this app by adding more shapes, textures, or saving designs.")
