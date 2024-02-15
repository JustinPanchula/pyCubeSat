#!/usr/bin/env python
"""Computes color gradients.
"""
__author__ = "Justin Panchula"
__copyright__ = "Copyright 2024 UC CubeCats"
__credits__ = ["Justin Panchula"]
__license__ = "MIT"
__version__ = "0.1.0"
__status__ = "Production"
__maintainer__ = None
__contact__ = None

# Imports
import numpy as np


def color_gradient(data: np.ndarray) -> np.ndarray:
    """Given an array, returns the appropriate color gradient

    Args:
        data (np.ndarray): the array of values.

    Returns:
        np.ndarray: the array of rgb color codes.
    """

    # Find min, max, and count of data
    min = np.min(data)
    max = np.max(data)
    num = len(data)

    # Mix between 0 and 1
    mix_lvl = (data - min)/(max - min)

    # Calculate RGB values
    r = 255 * np.array([i for i in reversed(mix_lvl)])
    g = np.zeros(num)
    b = 255 * mix_lvl

    # Create gradient
    gradient = np.empty((len(r), 1), dtype=object)
    for i in range(num):
        gradient[i] = (f"rgb({r[i]}, {g[i]}, {b[i]})")

    return gradient


# Test
if __name__ == '__main__':
    print(color_gradient(np.linspace(10, 90, 100)))
