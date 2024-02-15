#!/usr/bin/env python
"""Functions related to quaternions
"""
__author__ = "Justin Panchula"
__copyright__ = "Copyright 2024 UC CubeCats"
__credits__ = ["Justin Panchula"]
__license__ = "MIT"
__version__ = "1.0.0"
__status__ = "Production"
__maintainer__ = None
__contact__ = None

# Imports
from typing import Tuple
import numpy as np
from scipy.spatial.transform import Rotation as R


class Rotation():
    """Converts between different coordinate frames"""
    def Earth_to_Stuff(x, y, z):
        return


class Quaternion():
    """Exchanges between quaternion and Euler angles.
    """
    def Quat_to_Euler(theta: float, alpha: float, psi: float, magnitude: float) -> Tuple[float, float, float]:
        """Given quaternions, returns Euler angles

        Args:
            theta (float): angle about the x-axis, in radians.
            alpha (float): angle about the y-axis, in radians.
            psi (float): angle about the z-axis, in radians.
            magnitude (float): the magnitude.

        Returns:
            Tuple[float, float, float]: the Euler angles
        """
        return R.from_quat(np.array([theta, alpha, psi, magnitude])).as_euler('xyz', False)

    def Euler_to_Quat(theta: float, alpha: float, psi: float) -> Tuple[float, float, float, float]:
        """Given Euler angles, returns quaternion angles.

        Args:
            theta (float): the angle about the x-axis, in radians.
            alpha (float): the angle about the y-axis, in radians.
            psi (float): the angle about the z-axis, in radians.

        Returns:
            Tuple[float, float, float, float]: the quaternions.
        """
        return R.from_euler('xyz', np.array(theta, alpha, psi), False).as_quat(True)


# Test
def _test():
    print(Quaternion.Euler_to_Quat(10, 10, 10))
    print(Quaternion.Quat_to_Euler(0, 0, 0, 0))