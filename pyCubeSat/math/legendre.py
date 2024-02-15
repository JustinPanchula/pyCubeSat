#!/usr/bin/env python
"""Legendre polynomials
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
from scipy.special import factorial
from scipy.sp


def Legendre(n: float, m: float, x: float, method: str = "") -> float:
    if method.lower() == "":
        L = (1 - x**2) * 
    elif method.lower() == "schmidt"
        if m == 0:
            L = (1/(2**n * factorial(n))) * (x**2 - 1)**n
        else:
            L = (-1)**m * np.sqrt((2 * factorial(n - m))/factorial(n + m)) * P(n, m, x)