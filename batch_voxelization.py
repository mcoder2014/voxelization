# -*- coding: utf-8 -*-
"""batch_voxelization
"""

import argparse
import sys
import os
import voxelization
import thread
import time
import numpy as np
import operator

FLAGS = None

def main( ):
    """ the main program entrence
    """

    print(FLAGS)
    filenames = os.listdir(FLAGS.data_dir)  # get the filenames under data_dir
    print(filenames)

    #file_lists = div_list(filenames, FLAGS.threads)
    #print(file_lists)
#    locks = []

#    for index in range(FLAGS.threads):
        #produce(index, file_lists[index])
#        try:
#            lock = thread.allocate_lock()
#            lock.acquire()
#            locks.append(lock)
#            thread.start_new_thread( produce, (file_lists[index], id, lock, ) )
#        except:
#            print("Error! thread", index, "unable to start")
    produce(filenames, "0")
    print("All work has finished!")

def produce( filenames , id):
    """function produce
    Args:
        filenames: a list of filenames
        id: thread id
    """
    # print("threads", id, filenames, "length", len(filenames))
    print("threads:{0} ,file {1}, length: {2}".format(
        id, filenames, len(filenames)))
    length = len(filenames)
    for index in range(length):
        filename = filenames[index]
        if not operator.eq("ply", filename[filename.rfind(".")+1:len(filename)]):
            #print (filename, operator.eq("ply", filename[filename.rfind("."):len(filename)]))
            print (filename)
            continue
        #print("work in file", filename, "process bar", index,"/",length)
        print("work in file: {0}, Process bar: {1}/{2}".format(
            filename, index + 1, length ))
        voxelization.voxelization(
            FLAGS.data_dir + filename,
            outputJsonPath = FLAGS.json_dir,
            outputNumpyPath = FLAGS.numpy_dir,
            outputBinvoxPath = FLAGS.binvox_dir,
            coef = FLAGS.judge_coef,
            size = (FLAGS.size0, FLAGS.size1, FLAGS.size2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_dir',
        type = str,
        default='./',
        help = 'the relative path to the *.ply model files floder')

    parser.add_argument(
        '--json_dir',
        type = str,
        default="./voxel_json/",
        help = 'the path to save exported json files' )

    parser.add_argument(
        '--numpy_dir',
        type = str,
        default = './voxel_numpy/',
        help = 'the path to save exported numpy files' )

    parser.add_argument(
        '--binvox_dir',
        type = str,
        default = './voxel_binvox/',
        help = 'the path to save exported binvox files' )

    parser.add_argument(
        "--judge_coef",
        type = float,
        default = 1.0,
        help = "larger the finger is, thicker the voxel model is" )

    parser.add_argument(
        '--size0',
        type = int,
        default = 192,
        help = "the first num of size (192, 192, 200)" )

    parser.add_argument(
        '--size1',
        type = int,
        default = 192,
        help = "the second num of size (192, 192, 200)" )

    parser.add_argument(
        '--size2',
        type = int,
        default = 200,
        help = "the third num of size (192, 192, 200)" )

    FLAGS, unparsed = parser.parse_known_args()
    main()      # run main function
