"""
Usage:
    PSEV_from_BRIDGE_SEP_id_docopt.py [-d=NAME] [-p=NAME] [-s=NAME] [-l=NAME]

Options:
    -h --help   Show this screen
    -d=NAME     Filepath of the directory where PSEV matrix lives
    -p=NAME     Name of PSEV matrix file
    -s=NAME     Name of SEP_map array
    -l=NAME     List of SEP identifiers
"""

## Import python packages

import numpy as np
import os
from docopt import docopt
import matplotlib.pyplot as plt

## Get the arguments

arguments = docopt(__doc__)
# SEP_variables from BRIDGE
# PSEV_matrix from SPOKE

# PSEV and SEP_map matrix version
dir_ = arguments['-d']
os.chdir(dir_)

# Load PSEV matrix
PSEV_matrix = np.load(arguments['-p'])

# Load SEP_map array
SEP_map = np.load(arguments['-s'])

# SEP_variables
SEP_variables = arguments['-l']
SEP_variables = SEP_variables.strip('[]').split(',')

def PSEV_to_BRIDGE():

    # Convert SEP_variables from BRIDGE to byte strings
    SEP_variables_bytes = [x.encode('UTF-8') for x in SEP_variables]

    # Initialize an empty list for the index (this carries the PSEV row index for each SEP variable)
    index = []

    # Loop on each BRIDGE SEP variable to get its index in the PSEV matrix
    for x in SEP_variables_bytes:
        index.append(np.where(SEP_map == x)[0][0])

    # Final PSEV to return to BRIDGE
    PSEV = PSEV_matrix[index, :]
    return PSEV

if __name__ == '__main__':
    PSEV = PSEV_to_BRIDGE()
    print(PSEV)
    plt.plot(PSEV[0,:])
    plt.show()


