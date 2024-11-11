import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3
from Scene import Scene
#from Scenario import Scenario
#from Rules import Rules

#Main
def cozmo_program():
    Scene.create_walls()
    Scene.plot_walls()


cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)