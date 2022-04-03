bl_info = {
    "name": "Auto add vertex groups",
    "author": "aapeli",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "",
}

import bpy
from bpy.types import(Panel, Operator)

class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "vertex.1"
    bl_label = "Simple Vertex Operator"

    def execute(self, context):
        
        sel_objs = [obj for obj in bpy.context.selected_objects if obj.type == "MESH"]
        bpy.ops.object.select_all(action="DESELECT")
        for ob in sel_objs:
            bpy.context.view_layer.objects.active = ob
            group = bpy.context.object.vertex_groups.new(name=ob.name)
            verts = []
            for vert in ob.data.vertices:
                verts.append(vert.index)
            group.add(verts, 1.0, 'ADD')
        
        return {'FINISHED'}
    
class GustomPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Auto vertex group panel"
    bl_idname = "OBJECT_PT_vertex"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Auto vertex group"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Add Vertex groups", icon='GROUP_VERTEX')

from bpy.utils import register_class, unregister_class

_classes = [ButtonOperator, GustomPanel]    
    
def register():
    for cls in _classes:
        register_class(cls)

def unregister():
    for cls in _classes:
        unregister_class(cls)

if __name__ == "__main__":
    register()

