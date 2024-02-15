#!/usr/bin/env python
"""Custom exceptions for Passive Magnetic Attitude Control Simulation.
"""
__author__ = "Justin Panchula"
__copyright__ = "Copyright 2024 UC CubeCats"
__credits__ = ["Justin Panchula"]
__license__ = "MIT"
__version__ = "1.0.0"
__status__ = "Production"
__maintainer__ = None
__contact__ = None


class pyCubeSatBaseException(Exception):
    def __init__(self, msg):
        """Base exception for pyCubeSat"""
        super().__init__(msg)


class PMACSBaseException(pyCubeSatBaseException):
    def __init__(self, msg):
        """Base exception for the PMACS module"""
        super().__init__(msg)