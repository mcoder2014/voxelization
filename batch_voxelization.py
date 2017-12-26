# -*- coding: utf-8 -*-
"""batch_voxelization
"""

import argparse
import sys
import os
import voxelization
import thread
import time

FLAGS = None

def main( ):
    """ the main program entrence
    """
    pass    # the progress need to be executed at first.

if __name__ = '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--datadir',
        type = str,
        default='./',
        help = 'the relative path to the *.ply model files floder')

    parser.add_argument(
        '--threads',
        type = int,
        default = 4,
        help = 'set the max threads using'
    )

    FLAGS, unparsed = parser.parse_known_args()
