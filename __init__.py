from . import AlignCameraToView

bl_info = {
    "name": "Align Camera To View",
    "author": "Crantisz, Jubi, Anime Nyan",
    "category": "3D View",
    "location": "3D View > Properties > Align Camera",
	"version": (1, 0, 1),
    "blender": (2, 93, 0),
    "category": "Camera",
	"description": "Assigns the active camera to the scene camera resolution and position",
}

def register():
    AlignCameraToView.register()

def unregister():
    AlignCameraToView.unregister()