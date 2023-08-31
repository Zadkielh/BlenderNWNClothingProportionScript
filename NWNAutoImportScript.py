import bpy
import os
from neverblender import nvb_ops_io


path = 'C:/Users/olemagnus/Desktop/Neverwinter Modding/export/models/clothing unsorted/pmh0/'

files = os.listdir(path)


for f in files:
    print(f)
    
    bpy.ops.scene.nvb_mdlimport('EXEC_DEFAULT', filepath=path + str(f))
    