# Imports
from pyCubeSat.Orbit import EarthOrbit

# Test
if __name__ == '__main__':
    orbit = EarthOrbit()
    fig1 = orbit.plot_ground_track(0.1)
    fig1.show()