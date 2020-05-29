#!/usr/bin/env python
# "shebang"

# If you call a script with:
#   python my_script.py
#       the shebang doesn't matter

#  ./my_script.py  (similar to executing a bash script)
#       therefore, always use one, it doesn't hurt anybody

from sklearn import preprocessing as pre
from argparse import ArgumentParser
from scipy import signal

import scipy.io as sio
import neurokit2 as nk
import pandas as pd
import numpy as np
import math



def driver():
    description = "Biosignal Emotions project BHS 2020."
    parser = ArgumentParser(__file__, description)


# main scripting details could go here
if __name__ == "__main__":
    driver()

