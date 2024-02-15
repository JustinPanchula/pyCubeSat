#!/usr/bin/env python
"""Computes the International Geomagnetic Reference Field 13, valid between 1900-01-01 and 2025-12-31.
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
from pathlib import Path
import pandas as pd
import numpy as np
from scipy.special import lpmv

# Custom packages
from pyCubeSat.Orbit import Orbit

# Logging
import logging
log = logging.getLogger('pyCubeSat.PMACS.IGRF')


def igrf(orbit: Orbit, t: float, days: float = 14):
    # Load IGRF coefficients
    log.info("Loading IGRF-13 coefficients")
    igrf_data = pd.read_csv(Path("./pyCubeSat/PMACS/IGRF/IGRF13.csv"), header=3)

    # Get year bracket
    T = t - t % 5

    # Cap at epoch 2020
    if T > 2020:
        log.info("Input \"year\" was greater than 2024, using epoch 2020")
        T = 2020

    # Get IGRF coefficientts
    coeffs = igrf_data.iloc[:, 0:3]
    coeffs.loc[:, str(T)] = igrf_data.loc[:, str(T)]
    if T == 2020:
        coeffs.loc[:, "SV"] = igrf_data.iloc[:, -1]
    else:
        coeffs.loc[:, "SV"] = (1/5) * (igrf_data.iloc[:, str(T + 5)] - igrf_data.iloc[:, str(T)])

    # Set Earth radius
    a = 6371.2  # km

    # Set N based on epoch
    if T <= 1995:
        N = 10
    else:
        N = 13

    # Get radius, co-latitude, and longitutde
    groundTrack = orbit.getGroundTrack(days)
    r = groundTrack['r']
    lat = groundTrack['lat']
    lon = groundTrack['lon']

    # Compute co-latitude
    colat = (np.pi/2) - lat

    def g(n: int, m: int, T: int, t: int) -> float:
        """The value of the "g" coefficient from the IGRF-13 model.

        Args:
            n (int): the degree of the coefficient.
            m (int): the order of the coefficient.
            T (int): the epoch.
            t (int): the year.

        Returns:
            float: the coefficient value of g.
        """
        # Find correct values
        i = 0
        while i < len(coeffs):
            gh, en, em = coeffs.iloc[i, 0:3]
            if gh == 'g' and en == n and em == m:
                break
            else:
                i += 1

        # Load coefficients
        c = coeffs.loc[i, str(T)]
        sv = coeffs.loc[i, 'SV']

        # Return correct values
        return c + (t - T) * sv

    def h(n: int, m: int, T: int, t: int) -> float:
        """The value of the "h" coefficient from the IGRF-13 model.

        Args:
            n (int): the degree of the coefficient.
            m (int): the order of the coefficient.
            T (int): the epoch.
            t (int): the year.

        Returns:
            float: the coefficient value of h.
        """
        # Find correct values
        i = 0
        while i < len(coeffs):
            gh, en, em = coeffs.iloc[i, 0:3]
            if gh == 'h' and en == n and em == m:
                break
            else:
                i += 1

        # Check that "h" value in valid
        if i == len(coeffs):
            return 0.0
        else:  # Load coefficients
            c = coeffs.loc[i, str(T)]
            sv = coeffs.loc[i, 'SV']

            # Return correct values
            return c + (t - T) * sv

    # Compute field
    log.info("Computing IGRF-13 model")
    sum = np.zeros(len(r))
    # for i in range(len(r)):
    for i in range(1):
        log.debug(f"Computing IGRF-13 for point {i}: r = {r[i]:0.4f} | colat = {colat[i]} | lon = {lon[i]}")
        for n in range(N):
            for m in range(n):
                sum[i] += (a/r[i])**(n + 1) * (g(n, m, T, t) * np.cos(m * colat[i]) + h(n, m, T, t) * np.sin(m * colat[i])) * lpmv(m, n, np.cos(colat[i]))
    V = a * sum