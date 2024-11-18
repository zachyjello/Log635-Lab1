import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3
from Scene import Scene
from Scenario import Scenario
#from Rules import Rules

#Main
def cozmo_program(robot: cozmo.robot.Robot):
    #Scene.create_walls()
    #Scene.plot_walls()
    #Scene.initializeObjects()
    #Scene.initializeRulesInferenceAndShit()

    Scenario.room1()
    Scenario.room2()
    Scenario.room3()
    Scenario.room4()
    Scenario.room5()
    Scenario.room6()
    Scenario.endGame()

    


cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)