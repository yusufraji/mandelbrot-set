from importlib.metadata import metadata
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
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

    _ = utils.julia(progress_bar, frame_text, separation, iterations, st_fig)

    # We clear elements by calling empty on them.
    progress_bar.empty()
    frame_text.empty()

    frames = 100  # number of animation frames
    m, n, s = 960, 640, 400
    x = np.linspace(-m / s, m / s, num=m).reshape((1, m))  # real axis
    y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))  # imaginary axis
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes()
    anim = animation.FuncAnimation(
        fig,
        utils.animate_julia,
        fargs=(
            ax,
            x,
            y,
            separation,
            iterations,
        ),
        frames=100,
        interval=50,
        blit=True,
    )

    video_writer = animation.FFMpegWriter(fps=5)
    gif_writer = animation.PillowWriter(fps=5)
    anim.save(str(Path.cwd() / "graphics" / "julia_set.mp4"), writer=video_writer)
    anim.save(str(Path.cwd() / "graphics" / "julia_set.gif"), writer=gif_writer)

    st.write(
        "This render might be slow, when it's done, consider downloading the gif or mp4 to view locally."
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Re-run")
    with col2:
        with open(Path.cwd() / "graphics" / "julia_set.gif", "rb") as f:
            st.download_button(
                "Download as gif", data=f, file_name="julia_set.gif", mime="image/gif"
            )
    with col3:
        with open(Path.cwd() / "graphics" / "julia_set.mp4", "rb") as f:
            st.download_button(
                "Download as mp4", data=f, file_name="julia_set.mp4", mime="image/mp4"
            )
