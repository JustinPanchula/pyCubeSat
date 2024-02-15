# Import
from pyCubeSat.PMACS.IGRF import igrf
from pyCubeSat.Orbit import EarthOrbit

# Test
if __name__ == '__main__':
    V = igrf(EarthOrbit(), 2023)