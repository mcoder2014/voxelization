# -*- coding: utf-8 -*-
"""batch_voxelization
"""

import argparse
import sys
import os

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
        help = 'the relative path to the *.ply model files floder')

    FLAGS, unparsed = parser.parse_known_args()
