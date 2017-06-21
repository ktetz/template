import os
import sys

path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path2) if path2 not in sys.path else None

path = os.path.dirname(os.path.abspath(os.path.split(__file__)[0]))
sys.path.insert(0, path) if path not in sys.path else None

import template
 