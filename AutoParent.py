import bpy

selectedObjects = bpy.context.selected_objects

for item in selectedObjects:
    print(item.name[:-1])
    
    if (item.parent == None):
    
        o = bpy.data.objects.new( "empty", None )

        # due to the new mechanism of "collection"
        bpy.context.scene.collection.objects.link( o )

        # empty_draw was replaced by empty_display
        o.empty_display_size = 1
        o.empty_display_type = 'PLAIN_AXES'   
        o.name = item.name[:-1]
        item.parent = o
    
    elif (item.type == "MESH"):
        item.name = item.parent.name + "g"
    
    