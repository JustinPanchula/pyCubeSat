#!/usr/bin/env python
"""Base orbit class for pyCubeSat
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
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

# Logging
import logging
log = logging.getLogger('pyCubeSat.Orbit')


# Master orbit class
class Orbit(ABC):
    """Base orbit class"""
    # Set orbital constants
    MU: float
    R: float
    J2: float
    W: float

    @abstractmethod
    def __init__(self):
        pass

    def getGroundTrack(self, days: float) -> pd.DataFrame:
        """Computes the ground track for the orbit.

        Args:
            days (float): the number of days to compute.

        Returns:
            pd.DataFrame(index=[], columns=["sec", "r", "lat", and "lon"]): the dataframe containing ground track information.
        """
        # Log
        log.info("Computing ground track")

        # Get resolution from length of r
        res = len(self.r)

        # Calculate number of seconds in that many days
        sec = days * 24 * 60 * 60

        # Calculate number of orbits
        num_orbits = int(sec/self.T)

        # Get resolution
        res = int(res * num_orbits)

        # Find thetas
        theta_single = np.arccos((((self.h**2)/(self.r * self.MU)) - 1)/self.e)

        # Propogate radius and true anomoly for days of orbit
        theta = np.empty(0)
        r = np.empty(0)
        for _ in range(num_orbits):
            theta = np.append(theta, theta_single)
            r = np.append(r, self.r)

        # Make time array
        t = np.linspace(0, sec, res)

        # Calculate longitude and lattitude
        # lat = np.arcsin(np.sin(self.i) * np.sin(self.w + theta))
        # lon = np.arctan(np.cos(self.i) * np.tan(self.w + theta)) + self.omega - self.W * t
        lat = np.linspace(0, 2 * np.pi, len(t))
        lon = np.linspace(-np.pi, np.pi, len(t))

        # Convert to degrees
        lat = np.rad2deg(lat)
        lon = np.rad2deg(lon)

        # Create dataframe of orbital ground track
        columns = ['sec', 'r', 'lat', 'lon']
        index = []
        ground_track = pd.DataFrame(columns=columns, index=index)

        # Populate
        ground_track['sec'] = t
        ground_track['r'] = r
        ground_track['lat'] = lat
        ground_track['lon'] = lon

        return ground_track

    # Properties
    @property
    @abstractmethod
    def r(self) -> np.ndarray:
        """Orbital radii (km)"""
        pass

    @property
    @abstractmethod
    def ra(self) -> float:
        """Orbital apoapsis radius (km)"""
        pass

    @property
    @abstractmethod
    def rp(self) -> float:
        """Orbital periapsis radius (km)"""
        pass

    @property
    @abstractmethod
    def e(self) -> float:
        """Orbital eccentricity"""
        pass

    @property
    @abstractmethod
    def i(self) -> float:
        """Orbital inclination (rad)"""
        pass

    @property
    @abstractmethod
    def omega(self) -> float:
        """Orbital right ascension of the ascending node (rad)"""
        pass

    @property
    @abstractmethod
    def w(self) -> float:
        """Orbital argument of periapsis (rad)"""
        pass

    @property
    @abstractmethod
    def h(self) -> float:
        """Orbital specific angular momentum"""
        pass

    @property
    @abstractmethod
    def a(self) -> float:
        """Orbital semi-major axis (km)"""
        pass

    @property
    @abstractmethod
    def T(self) -> float:
        """Orbital period (sec)"""
        pass