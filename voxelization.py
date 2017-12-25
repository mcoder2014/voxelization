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

    boundingbox = getBoundingBox(scene)    # get the bounding box of scene

def _getBoundingBox(scene):
    """give a assimp scene, get it bounding box
            It will bounding all meshes in the mesh.
        Args:
            scene: assimp scene
        Returns:
            bounding box ( xmax, ymax, zmax, xmin, ymin, zmin )
            6 num represent 6 faces.
    """
    if len(scene.meshes) == 0:
        print("scene's meshes attribute has no mesh")
        return (0,0,0,0,0,0)

    mesh_1 = scene.meshes[0]
    xmax, ymax, zmax = np.amax( mesh_1.vertices, axis = 0 )
    xmin, ymin, zmin = np.amin( mesh_1.vertices, axis = 0 )

    for index in range(1,len(scene.meshes)):
        mesh_t = scene.meshes[index]
        xmax_t, ymax_t, zmax_t = np.amax( mesh_t.vertices, axis = 0)
        xmin_t, ymin_t, zmin_t = np.amin( mesh_t.vertices, axis = 0)

        if xmax_t > xmax:   xmax = xmax_t
        if ymax_t > ymax:   ymax = ymax_t
        if zmax_t > zmax:   zmax = zmax_t
        if xmin_t < xmin:   xmin = xmin_t
        if ymin_t < ymin:   ymin = ymin_t
        if zmin_t < zmin:   zmin = zmin_t

    return (xmax, ymax, zmax, xmin, ymin, zmin)

def _meshVoxel(boundingbox, mesh, voxel):
    """ mesh voxel function
    change numpy.ndarray's 0 to 1 acounding to mesh and scene'bounding box
    Args:
        boundingbox: bounding box
        mesh: pyassimp mesh
        voxel: numpy.ndarray
    """
    pass
