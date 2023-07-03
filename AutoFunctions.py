bl_info = {
    "name": "Auto Functions",
    "author": "flvffywvffy",
    "version": (0, 0, 1),
    "blender": (3, 5, 1),
    "location": "3D Viewport > Sidebar > AutoFunctions",
    "description": "Makes modeling quicker in blender.",
    "category": "Development",
}

import bpy

class OBJECT_OT_add_hd_cam(bpy.types.Operator):
    bl_idname = "object.add_hd_camera"
    bl_label = "Add HD camera"
    
    def execute(self, context):
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(1.5708, -0, -0), scale=(1, 1, 1))
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        bpy.context.scene.render.fps = 30
        return {"FINISHED"}

class OBJECT_OT_add_fourk_cam(bpy.types.Operator):
    bl_idname = "object.add_fourk_camera"
    bl_label = "Add 4k camera"
    
    def execute(self, context):
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(1.5708, -0, -0), scale=(1, 1, 1))
        bpy.context.scene.render.resolution_x = 3840
        bpy.context.scene.render.resolution_y = 2160
        bpy.context.scene.render.fps = 60
        return {"FINISHED"}

class apply_basic_render_props(bpy.types.Operator):
    bl_idname = "render.apply_basic_render_props"
    bl_label = "Apply Basic Render Properties"
    
    def execute(self, context):
        """Applies basic render properties such as ambient occlusion and bloom."""
        bpy.context.scene.eevee.use_gtao = True
        bpy.context.scene.eevee.use_bloom = True
        return {"FINISHED"}

class VIEW3D_PT_auto_functions_gen(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AutoFunctions"
    bl_label = "General"
    
    def draw(self, context):
        row = self.layout.row()
        row.label(text="Cameras:")
        row = self.layout.row()
        row.operator("object.add_hd_camera", text="1080p 30fps")
        row.operator("object.add_fourk_camera", text="4K 60fps")
        self.layout.separator()
        row = self.layout.row()
        row.label(text="Other:")
        row = self.layout.row()
        row.operator("render.apply_basic_render_props", text="Apply Basic Render Props")

class VIEW3D_PT_auto_functions_credits(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AutoFunctions"
    bl_label = "Credits"
    
    def draw(self, context):
        row = self.layout.row()
        row.label(text="Version: 0.0.1")
        row = self.layout.row()
        row.label(text="flvffywvffy © 2023")
        
def register():
    bpy.utils.register_class(VIEW3D_PT_auto_functions_gen)
    bpy.utils.register_class(VIEW3D_PT_auto_functions_credits)
    bpy.utils.register_class(OBJECT_OT_add_hd_cam)
    bpy.utils.register_class(OBJECT_OT_add_fourk_cam)
    bpy.utils.register_class(apply_basic_render_props)
    
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_auto_functions_gen)
    bpy.utils.unregister_class(VIEW3D_PT_auto_functions_credits)
    bpy.utils.unregister_class(OBJECT_OT_add_hd_cam)
    bpy.utils.unregister_class(OBJECT_OT_add_fourk_cam)
    bpy.utils.register_class(apply_basic_render_props)
    
if __name__ == "__main__":
    register()
