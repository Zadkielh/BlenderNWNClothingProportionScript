import bpy
from neverblender import nvb_ops_io
from neverblender import nvb_utils


selectedObjects = bpy.context.selected_objects
allObjects = bpy.data.objects

path = ''
i = 200
for object in selectedObjects:
    i = i + 1
    
    children = []
    nvb_utils.get_children_recursive(object, children)
    for child in children:
        if '.' in child.name:
            print(child.name)
            try:
                allObjects[child.name.split('.')[0]].name = allObjects[child.name.split('.')[0]].name + ".00" + str(i)
            except:
                pass
            child.name = child.name.split('.')[0]
            
    bpy.context.view_layer.objects.active = object
    bpy.ops.scene.nvb_mdlexport('EXEC_DEFAULT', filepath=path + object.name + ".mdl")
    

