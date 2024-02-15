#!/usr/bin/env python
"""Computes orbital parameters about Earth.
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
import plotly.graph_objects as go

# Custom packages
from pyCubeSat.Orbit import Orbit

# Logging
import logging
log = logging.getLogger('pyCubeSat.Orbit')


class EarthOrbit(Orbit):
    # Set orbital constants
    MU = 398600  # km^3/m^2
    R = 6371  # Volumetric mean radius (km)
    J2 = 0.0010836  # Earth's dynamics oblateness
    W = (2 * np.pi)/((365.24/366.24) * 24 * 60 * 60)  # Angular rate of Earth (rad/s)

    def __init__(self,
                 Ap: float = 418,
                 e: float = 0.0000820,
                 i: float = 51.6432,
                 omega: float = 289.5972,
                 w: float = 300.5175,
                 res: int = 1000):
        """Propogates an orbit around Earth based on input parameters, or uses the default parameters for the ISS.

        Args:
            Ap (float): altitude of periapsis (km). Defaults to 418 km.
            e (float): orbital eccentricity, between 0 and 1. Defaults to 0.000820.
            i (float): orbital inclination (deg). Defaults to 51.6432°.
            Omega (float): right ascention of the ascending node (deg). Defaults to 289.5972°
            w (float): argument of periapsis (deg). Defaults to 300.5175°.
            res (int): resolution of the orbit. Defaults to 1000.
        """
        # Convert to radians
        self._e = np.radians(e)
        self._i = np.radians(i)
        self._omega = np.radians(omega)
        self._w = np.radians(w)

        # Calculate periapsis radius
        self._rp = Ap + EarthOrbit.R  # volumetric mean radius

        # Calculate specific angular momentum and semi-major axis
        self._h = np.sqrt(self._rp * EarthOrbit.MU * (1 + self._e))
        self._a = (self._h**2/EarthOrbit.MU) * (1/(1 - self._e**2))

        # Calculate period
        self._T = ((2 * np.pi)/np.sqrt(EarthOrbit.MU)) * self._a**(3/2)

        # Get theta
        theta = np.linspace(0, 2 * np.pi, res)

        # Calculate r
        self._r = (self._h**2/EarthOrbit.MU) * (1/(1 + self._e * np.cos(theta)))

    def plot_ground_track(self, days: float) -> go.Figure:
        """Plots the ground track of the satellite

        Args:
            days (float): the number of days to plot.

        Returns:
            go.Figure: the ground track.
        """
        # Log
        log.info("Plotting ground track")

        # Get ground track
        ground_track = self.getGroundTrack(days)

        # Create figure
        fig1 = go.Figure(
            data=[
                go.Scattergeo(  # Earth map
                    name="Ground Track",
                    lat=ground_track['lat'],
                    lon=ground_track['lon'],
                    mode="markers",
                    marker={
                        'cmax': np.max(self._r) - self.R,
                        'cmin': np.min(self._r) - self.R,
                        'colorscale': [[0, "rgb(255, 0, 0)"], [1, "rgb(0, 0, 255)"]],
                        'color': self._r - self.R,
                        'colorbar': {
                            'title': {
                                'text': "Altitude"
                            },
                            'tickvals': [np.min(self._r) - self.R, np.mean(self._r) - self.R, np.max(self._r) - self.R],
                        }
                    }
                )
            ],
            layout={
                'title': {
                    'text': "Ground Track of the Satellite"
                },
                'geo': {
                    'projection_type': "orthographic",
                }
            }
        )
        # Return
        return fig1

    # Properties
    @property
    def r(self) -> np.ndarray:
        return self._r

    @property
    def ra(self) -> float:
        return np.max(self._r)

    @property
    def rp(self) -> float:
        return np.min(self._r)

    @property
    def e(self) -> float:
        return self._e

    @property
    def i(self) -> float:
        return self._i

    @property
    def omega(self) -> float:
        return self._omega

    @property
    def w(self) -> float:
        return self._w

    @property
    def h(self) -> float:
        return self._h

    @property
    def a(self) -> float:
        return self._a

    @property
    def T(self) -> float:
        return self._T


class EarthTLE():
    def __init__(self):
        return

    # Properties
    @property
    def r(self) -> np.ndarray:
        return self._r

    @property
    def ra(self) -> float:
        return np.max(self._r)

    @property
    def rp(self) -> float:
        return np.min(self._r)

    @property
    def e(self) -> float:
        return self._e

    @property
    def i(self) -> float:
        return self._i

    @property
    def omega(self) -> float:
        return self._omega

    @property
    def w(self) -> float:
        return self._w

    @property
    def h(self) -> float:
        return self._h

    @property
    def a(self) -> float:
        return self._a

    @property
    def T(self) -> float:
        return self._T