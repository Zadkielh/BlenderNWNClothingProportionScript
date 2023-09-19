import bpy
import os
from neverblender import *

selectedObjects = bpy.context.selected_objects

for item in selectedObjects:
    print(item.nvb.supermodel)
    
    supermodel = "pmk0"
    item.nvb.supermodel = supermodel
    
   