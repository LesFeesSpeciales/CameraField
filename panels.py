import bpy


class CAMERA_PT_FrustumPanel(bpy.types.Panel):
    bl_label = "Camera Frustum"
    bl_category = "CAMMAP"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        row = layout.row(align=True)
        row.prop(bpy.context.scene.camera_frustum_settings, "only_active")
        row.prop(bpy.context.scene.camera_frustum_settings, "density")

        layout.prop(bpy.context.scene.camera_frustum_settings, "distribution", expand=True)

        layout.separator()
        layout.operator("camerafield.view_field", icon='RENDER_ANIMATION')
        layout.operator("camerafield.bake_to_object", icon='POINTCLOUD_DATA')


class CAMERA_PT_FrustumCameraPanel(bpy.types.Panel):
    bl_label = "Camera Frustum"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        engine = context.scene.render.engine
        return context.camera

    def draw(self, context):
        layout = self.layout

        ob = context.object
        cam = ob.data

        layout.prop(cam.camera_frustum_settings, "enable")
        layout.prop(cam.camera_frustum_settings, "color")
