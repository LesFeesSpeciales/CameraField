bl_info = {
    "name": "Camera Field",
    "author": "Christophe SEUX",
    "version": (1, 0, 2),
    "blender": (2, 80, 0),
    "description": "View camera frustum",
    "warning": "",
    "wiki_url": "",
    "category": "Camera",
    }


if "bpy" in locals():
    import imp
    imp.reload(operators)
    imp.reload(panels)

else:
    from .operators import *
    from .panels import *


class CameraFrustumSettings(bpy.types.PropertyGroup):
    only_active: bpy.props.BoolProperty(default=True,
                                    name='Only Active',
                                    description='Project only from active camera')

    density: bpy.props.IntProperty(default=2000,
                                    name='Density',
                                    description='Camera frustum point density')

    distribution: bpy.props.EnumProperty(items=(('Random',)*3, ('Grid',)*3, ('Trail',)*3),
                                  default='Random',
                                  name='Distribution',
                                  description='How the points will be arranged')


class CameraFrustumCameraSettings(bpy.types.PropertyGroup):
    enable: bpy.props.BoolProperty(default=True,
                                   name="Enable",
                                   description="Show points for this camera")

    color: bpy.props.FloatVectorProperty(default=(1.0, 1.0, 0.0),
                                         min=0.0,
                                         max=1.0,
                                         name="Color",
                                         description="Camera frustum point color",
                                         subtype="COLOR")

classes = (CameraFrustumSettings, CameraFrustumCameraSettings,
           CAMERA_PT_FrustumCameraPanel, CAMERA_PT_FrustumPanel,
           CAMERA_OT_view_camera_field, CAMERA_OT_bake_field_to_object)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.camera_frustum_settings = bpy.props.PointerProperty(type=CameraFrustumSettings)
    bpy.types.Camera.camera_frustum_settings = bpy.props.PointerProperty(type=CameraFrustumCameraSettings)


def unregister():
    del bpy.types.Scene.camera_frustum_settings
    del bpy.types.Camera.camera_frustum_settings
    for cls in classes:
        bpy.utils.unregister_class(cls)
