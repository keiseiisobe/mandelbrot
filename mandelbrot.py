"""
An implementation of Mandelbrot Set described in Chapter3 (Mathmetics and Reality)
in 'The Emperor's New Mind' written by Roger Penrose.
"""

import numpy as np
import matplotlib.pyplot as plt

def mapping(z, c):
    """
    Mapping z -> z^2 + c and iterate.
    This is described in p.121
    """
    while True:
        yield z
        z = z**2 + c

if "__main__" == __name__:
    # real axis
    re_start, re_stop = -3, 1
    # imaginary axis
    im_start, im_stop = -2, 2

    pixel_depth = 500

    row = np.linspace(re_start, re_stop, num=(re_stop - re_start) * pixel_depth)
    col = np.linspace(im_start, im_stop, num=(im_stop - im_start) * pixel_depth)
    M = row[np.newaxis, :] + col[:, np.newaxis] * 1j
    # mapping for Mandelbrot
    generator = mapping(0, M)
    # change parameters if you need Julia Set.
    # mapping for Julia
    # generator = mapping(M, 0.25)

    iteration = 20
    for i in range(iteration):
        res = next(generator)
    res = abs(res) <= 2

    plt.imshow(res)
    plt.show()
