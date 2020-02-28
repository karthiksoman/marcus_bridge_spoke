import numpy as np
import sys
import os
# import matplotlib
# matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
# plt.switch_backend('TkAgg')

# SEP_variables from BRIDGE
# PSEV_matrix from SPOKE

# PSEV and SEP_map matrix version
dir_ = sys.argv[1]
os.chdir(dir_)

# Load PSEV matrix
PSEV_matrix = np.load(sys.argv[2])

# Load SEP_map array
SEP_map = np.load(sys.argv[3])

# SEP_variables
SEP_variables = sys.argv[4]
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

