from matplotlib import pyplot as plt
import numpy as np


def sigmoid_plot() -> None:
    """
    The sigmoid plot function approximates a step function when
    w -> infinity. The b parameter controls the horizontal
    displacement of the step function.
    """
    bs = [-10, 0, 10]
    ws = [-10, 0, 10]

    x = np.linspace(-10, 10, 100)

    i = 1
    plt.figure(figsize=(12, 12))
    for b in bs:
        for w in ws:
            y = 1 / (1 + np.exp(-w * x + b))
            plt.subplot(3, 3, i)
            plt.plot(x, y)
            plt.title(f"w={w}, b={b}")
            i += 1
    plt.show()
    return


def tower_plot() -> None:
    """
    The tower function is created by subtracting two step-functions
    with the same height, but are slightly displaced.
    """
    x = np.linspace(-10, 10, 100)

    b1, w1 = -10, 10
    y1 = 1 / (1 + np.exp(-w1 * x + b1))

    b2, w2 = 10, 10
    y2 = 1 / (1 + np.exp(-w2 * x + b2))

    plt.figure(figsize=(6, 8))
    plt.subplot(311)
    plt.plot(x, y1)
    plt.title('y1')
    plt.subplot(312)
    plt.plot(x, y2)
    plt.title('y2')
    plt.subplot(313)
    plt.plot(x, y1 - y2)
    plt.title('y1 - y2')
    plt.show()
    return


sigmoid_plot()
tower_plot()
