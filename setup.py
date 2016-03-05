################################################################################
# description: Initializes the SmartBet code base on your computer
# contributors: Connor Stone
# Date: 29-02-2016
################################################################################

import os

cwd = os.getcwd()

def install():

    # Write a file in each directory with the location of the head
    for root, dirs, files in os.walk(os.path.join(cwd,'scripts')):
        with open(os.path.join(root, '.head'), 'w') as f:
            f.write(cwd)
    
    return 0
