import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3
from Scene import Scene
from CrimeInference import CrimeInference
from Scenario import Scenario
#from Rules import Rules
import time

#ONLY FOR TESTING
def testLift(robot : cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()
    time.sleep(1)
    for cube in cubes:
        print(f"Cube id:{cube.cube_id}")
        print(f"Postion (x,y,z):{cube.pose.position.x, cube.pose.position.y, cube.pose.position.z}")
        print(f"Postion (x_y_z):{cube.pose.position.x_y_z}")
        robot.go_to_object(cube, distance_mm(20)).wait_for_completed()
        robot.set_lift_height(1).wait_for_completed()
        robot.set_lift_height(0).wait_for_completed()
#Main
def cozmo_program(robot : cozmo.robot.Robot):

    #TODO: ONLY WORK ON PAPERCLIP CUBE
    def on_cube_tapped(event, *, obj, tap_count, tap_duration, **kw): 
        print("Received a tap event"+ str(event.obj.object_id))

    handler = robot.add_event_handler(cozmo.objects.EvtObjectTapped,on_cube_tapped)
    #pos = robot.pose
    Scene.create_walls(robot)
    #Scene.posDepart(robot)
    testLift(robot)

    #Scene.initializeObjects()
    #Scene.initializeRulesInferenceAndShit()
    scenario = Scenario()

    #Scenario.room1(scenario, robot)
    #Scenario.room2(scenario, robot)
    #Scenario.room3(scenario, robot)
    #Scenario.room4(scenario, robot)
    #Scenario.room5(scenario, robot)
    #Scenario.room6(scenario, robot)
    #Scenario.endGame(scenario, robot)
    
    '''agent = CrimeInference()
    
    # Conclusions
    print("Pièce du crime : ", agent.get_crime_room())
    print("Arme du crime : ", agent.get_crime_weapon())
    print("Personne victime : ", agent.get_victim())
    print("Heure du crime : ", agent.get_crime_hour())
    print("Meurtrier : ", agent.get_suspect())
    print("Personnes innocentes : ", agent.get_innocent())
    '''

    print("FINISH")
    while True:
        time.sleep(0.1)

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)