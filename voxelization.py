# -*- coding: utf-8 -*-
"""
Functions that can voxelization the *.ply files
python 2.7
Author: Chaoqun Jiang
Home Page: http://mcoder.cc
"""

import pyassimp
import numpy as np
import operator

def voxelization(filename,
    outputJsonPath = '../voxel_json/',
    outputNumpyPath = '../voxel_numpy/',
    size = (192,192,200)):
    """ function voxelization
        This function load a *.ply model file, and convert it into a voxel.
        And export in two formats.

        numpy formats: just use numpy import, a array has shape (192, 192, 200)
        json format: a numpy format reshape to (1,) and attribute name is 'array'
    Args:
        filename:   a relative file path to the *.ply file
        outputJsonPath: a relative floder path to save voxel in json format
        outputNumpyPath: a relative floder path to save voxel in numpy format
        size: a tuple with 3 integer, default is (192, 192, 200)
    """
    if len(size) != 3:
        print("The argument \" size \" should has three integer")
        return

    scene = pyassimp.load(filename)     # import scene
    meshes_count = len(scene.meshes)    # the count of meshes
    if meshes_count < 1:
        print("Error! The model file has no meshes in it")
        return

    voxel_width = size[0]
    voxel_height = size[1]
    voxel_length = size[2]

    voxel = np.zeros( shape = (voxel_width, voxel_height, voxel_length),
        dtype = np.float32)         # Creat a zeros ndarray

    boundingbox = _getBoundingBox(scene)    # get the bounding box of scene

    def _getBoundingBox(scene):
        """give a assimp scene, get it bounding box
            It will bounding all meshes in the mesh.
        Args:
            scene: assimp scene
        Returns:
            bounding box
        """
        pass

    def _meshVoxel(boundingbox, mesh, voxel):
        """ mesh voxel function
        change numpy.ndarray's 0 to 1 acounding to mesh and scene'bounding box
        Args:
            boundingbox: bounding box
            mesh: pyassimp mesh
            voxel: numpy.ndarray
        """
        pass
