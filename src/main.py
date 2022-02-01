from pathlib import Path

import streamlit as st

import utils

st.title("Mandelbrot Set")

set_type = st.sidebar.selectbox("Select set", ("Julia Set",))

if set_type == "Julia Set":
    st.subheader("Julia Set")

    iterations = st.slider("Level of detail", 2, 20, 10, 1)
    separation = st.slider("Separation", 0.7, 2.0, 0.7885)

    progress_bar = st.progress(0)

    # placeholders
    frame_text = st.empty()
    st_fig = st.empty()

    utils.julia(progress_bar, frame_text, separation, iterations, st_fig)

    # We clear elements by calling empty on them.
    progress_bar.empty()
    frame_text.empty()

    st.button("Re-run")
