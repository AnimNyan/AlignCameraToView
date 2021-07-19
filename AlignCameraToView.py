import bpy

def main(context):
    #set render resolution and lens data
    region=False
    for reg in context.area.regions:
        if(reg.type=='WINDOW'): 
            region = reg

    if(region):
        context.scene.render.resolution_x = region.width
        context.scene.render.resolution_y = region.height
        context.scene.camera.data.lens=context.space_data.lens

    #set camera position
    context.scene.camera.matrix_world=context.space_data.region_3d.view_matrix
    context.scene.camera.matrix_world.invert()

    #I don't know why sensor width must be 64, but it works:
    context.scene.camera.data.sensor_width = 64

    #set view from camera
    context.space_data.region_3d.view_perspective = 'CAMERA'

class ALIGNCAMERATOVIEW_PT_main_panel(bpy.types.Panel):
    bl_label = "Align Camera to View"
    bl_idname = "ALIGNCAMERATOVIEW_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Align"

    #if poll returns False
    #execute and draw functions will not run
    #In this case execute function will always run 
    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def draw(self, context):
        layout = self.layout
        layout.label(text ="This will set the active camera") 
        layout.label(text = "settings to the scene camera settings")
        layout.separator()

        layout.operator("aligncameratoview.set_render_size")


class ALIGNCAMERATOVIEW_OT_set_render_size(bpy.types.Operator):
    bl_idname = "aligncameratoview.set_render_size"
    bl_label = "Align Camera To View"

    #if poll returns False
    #execute and draw functions will not run
    #In this case execute function will always run 
    @classmethod
    def poll(cls, context):
        return context.area.type == 'VIEW_3D'

    def execute(self, context):
        main(context)
        return {'FINISHED'}

classes = [ALIGNCAMERATOVIEW_OT_set_render_size, ALIGNCAMERATOVIEW_PT_main_panel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    #unregister in reverse order to registered so classes relying on other classes
    #will not lead to an error
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()