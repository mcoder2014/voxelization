# read me

This project's aim is to voxelize the `*.ply` 3D model.
But only for `ply` files, all [assimp support files ](
http://assimp.sourceforge.net/main_features_formats.html) can be voxelized.

# Import formats
Autodesk ( .fbx ), Collada ( .dae ), glTF ( .gltf, .glb ), Blender 3D ( .blend ),
 3ds Max 3DS ( .3ds ), 3ds Max ASE ( .ase ), Wavefront Object ( .obj ),
Industry Foundation Classes (IFC/Step) ( .ifc ), XGL ( .xgl,.zgl ),
Stanford Polygon Library ( .ply ), AutoCAD DXF ( .dxf ), LightWave ( .lwo ),
LightWave Scene ( .lws ), Modo ( .lxo ), Stereolithography ( .stl ),
DirectX X ( .x ), AC3D ( .ac ), Milkshape 3D ( .ms3d ), TrueSpace ( .cob,.scn )

# Export voxel formats
## numpy
A numpy array with shape of you appointed.Example: you give a vexel size of (100, 100, 100).
It will return a numpy array with shape (100, 100, 100).

## JSON
For more convenient usage, it export a json file. Just reshape the numpy array to
(-1, ) . As it shown below:

```JSON
{
    "array": [0,1,0,1]
}
```

## Requires

- [pyassimp 3](https://github.com/assimp/assimp/blob/master/port/PyAssimp/README.md)
- [numpy](http://www.numpy.org/)
- [python 2.7](https://www.python.org/downloads/)
- [pyflann](https://github.com/primetang/pyflann)
