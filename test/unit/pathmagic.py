import os
import sys
par_dir = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    )
sys.path.insert(0, par_dir)
