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

    print("data_dir", FLAGS.data_dir)
    print("threads", FLAGS.threads)
    print("json_dir", FLAGS.json_dir)
    print("numpy_dir", FLAGS.numpy_dir)
    print("binvox_dir", FLAGS.binvox_dir)

    filenames = os.listdir(FLAGS.data_dir)  # get the filenames under data_dir
    #print(filenames)

    file_lists = div_list(filenames, FLAGS.threads)
    #print(file_lists)
    locks = []

    for index in range(FLAGS.threads):
        #produce(index, file_lists[index])
        try:
            lock = thread.allocate_lock()
            lock.acquire()
            locks.append(lock)
            thread.start_new_thread( produce, (file_lists[index], id, lock, ) )
        except:
            print("Error! thread", index, "unable to start")

    for lock in locks:
        while lock.locked():
            pass

    print("All work has finished!")

def produce( filenames , id, lock):
    """function produce
    Args:
        filenames: a list of filenames
        id: thread id
        lock: prevent main thread ends too early
    """
    print("threads", id, filenames, "length", len(filenames))
    length = len(filenames)
    for index in range(length):
        filename = filenames[index]
        if not operator.eq("ply", filename[filename.rfind(".")+1:len(filename)]):
            print (filename, operator.eq("ply", filename[filename.rfind("."):len(filename)]))
            continue
        print("work in file", filename, "process bar", index,"/",length)
        voxelization.voxelization(
            FLAGS.data_dir + filename,
            outputJsonPath = FLAGS.json_dir,
            outputNumpyPath = FLAGS.numpy_dir,
            outputBinvoxPath = FLAGS.binvox_dir,
            size = (192,192,200))
    lock.release()

def div_list(ls,n):
    """divide list into n parts
    """
    if not isinstance(ls,list) or not isinstance(n,int):
        return []
    ls_len = len(ls)
    if n<=0 or 0==ls_len:
        return []
    if n > ls_len:
        return []
    elif n == ls_len:
        return [[i] for i in ls]
    else:
        j = ls_len/n
        k = ls_len%n
        ### j,j,j,...(前面有n-1个j),j+k
        #步长j,次数n-1
        ls_return = []
        for i in xrange(0,(n-1)*j,j):
            ls_return.append(ls[i:i+j])
        #算上末尾的j+k
        ls_return.append(ls[(n-1)*j:])
        return ls_return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_dir',
        type = str,
        default='./',
        help = 'the relative path to the *.ply model files floder')

    parser.add_argument(
        '--threads',
        type = int,
        default = 4,
        help = 'set the max threads using' )

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

    FLAGS, unparsed = parser.parse_known_args()
    main()      # run main function
