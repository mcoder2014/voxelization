# -*- coding: utf-8 -*-
"""
split files under one floder into your determined parts.
And copy them to your determined floders.
"""
import argparse
import os
import time
import operator
import math
import shutil

FLAGS = None

def main( ):
    """ main function
    """
    filenames = os.listdir( FLAGS.in_dir )
    file_lists = div_list(filenames, FLAGS.split)

    start_time = time.time()
    file_list_length = len(file_lists)

    for part in range(file_list_length):

        part_list = file_lists[part]     # part lists
        print(part_list)
        floder_path = os.path.join(FLAGS.out_dir, FLAGS.prefix + str(part))
        os.makedirs(floder_path)        #create_

        part_time = time.time()
        part_list_length = len(part_list)

        for index in range(part_list_length):

            single_time = time.time()
            file_old = os.path.join(FLAGS.in_dir, part_list[index])
            file_new = os.path.join(floder_path, part_list[index])

            shutil.copy(file_old, file_new)
            print("File {0} -> {1} finished in {2} Sec. Total:{3}/{4} Part:{5}/{6}".format(
                file_old, file_new, time.time() - part_time,
                part+1, file_list_length,
                index+1, part_list_length ))

        print("Total: {0}/{1} finished, cost {2} Sec.".format(
            part + 1, file_list_length, time.time() - part_time ))

    print("All work finished, cost {0} Sec.".format(
        time.time() - start_time ))

#split the arr into N chunks
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
        '-i',
        '--in_dir',
        dest = 'in_dir',
        type = str,
        default='./',
        help = 'the input dir')

    parser.add_argument(
        '-o',
        '--out_dir',
        dest = 'out_dir',
        type = str,
        default='./',
        help = 'the output dir')

    parser.add_argument(
        '-s',
        '--split',
        type = int,
        dest = "split",
        default = 1,
        help = 'Split files into xx parts')

    parser.add_argument(
        '-p',
        '--prefix',
        dest = 'prefix',
        type = str,
        default = '',
        help = "the prefix add before each subdirs!" )

    FLAGS, unparsed = parser.parse_known_args()
    print(FLAGS)
    main()      # run main function
