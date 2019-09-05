"""Path hack to make tests work."""

import os
import sys

bp = os.path.realpath('.').split(os.sep)

modpath = os.sep.join(bp + ['src'])

sys.path.insert(0, modpath)

