"""Pure Python CubeSat Simulation
"""

# __all__
from . import Orbit
from . import PMACS
__all__ = [Orbit, PMACS]


# Configure logging
import logging
import logging.config
import yaml
logging.config.dictConfig(yaml.safe_load(open("pyCubeSat/logging.yaml", 'r').read()))