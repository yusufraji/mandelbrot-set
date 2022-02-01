import matplotlib.pyplot as plt
import numpy as np


def julia(progress_bar, frame_text, separation, iterations, st_fig):
    m, n, s = 960, 640, 400
    x = np.linspace(-m / s, m / s, num=m).reshape((1, m))  # real axis
    y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))  # imaginary axis

    for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))
        # Here were setting value for these two elements.
        progress_bar.progress(frame_num)
        frame_text.text("Frame %i/100" % (frame_num + 1))

        # Performing some fractal wizardry.
        c = separation * np.exp(1j * a)
        Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
        C = np.full((n, m), c)
        M: Any = np.full((n, m), True, dtype=bool)
        N = np.zeros((n, m))

        for i in range(iterations):
            Z[M] = Z[M] * Z[M] + C[M]
            M[np.abs(Z) > 2] = False
            N[M] = i

        # formatting options: remove ticks
        # ax = plt.axes()
        ax.set_xticks([], [])
        ax.set_yticks([], [])

        ax.imshow(1.0 - (N / N.max()), interpolation="hanning", cmap="magma_r")
        # Update the fig placeholder by calling the pyplot() function on it.
        st_fig.pyplot(fig, cmap="magma", clear_figure=True)


def animate_julia(a, ax, x, y, separation, iterations):
    a = a * (4 * np.pi) / 100
    ax.clear()
    ax.set_xticks([], [])
    ax.set_yticks([], [])
    m, n, s = 960, 640, 400
    # Performing some fractal wizardry.
    c = separation * np.exp(1j * a)
    Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
    C = np.full((n, m), c)
    M: Any = np.full((n, m), True, dtype=bool)
    N = np.zeros((n, m))

    for i in range(iterations):
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z) > 2] = False
        N[M] = i

    img = ax.imshow(1.0 - (N / N.max()), interpolation="hanning", cmap="magma_r")

    return [img]
