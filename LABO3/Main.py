import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3
from Scene import Scene
#from Scenario import Scenario
#from Rules import Rules

#Main
def cozmo_program():
    Scene.create_walls(cozmo.robot.Robot)
    Scene.plot_walls()
<<<<<<< HEAD
    Scene.posDepart(cozmo.robot.Robot)
=======
    Scene.placeHint()
>>>>>>> 8edee3308bcd570d21c2d2d1b7df6f254e7dbcab


cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)