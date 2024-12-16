import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3
from Scene import Scene
from CrimeInference import CrimeInference
from Scenario import Scenario
#from Rules import Rules
import time

counterTAP = 0

#ONLY FOR TESTING
def testLift(robot : cozmo.robot.Robot, scenario: Scenario):

    """lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()
    time.sleep(1)
    for cube in cubes:
        print(f"Cube id:{cube.cube_id}")
        print(f"Postion (x,y,z):{cube.pose.position.x, cube.pose.position.y, cube.pose.position.z}")
        print(f"Postion (x_y_z):{cube.pose.position.x_y_z}")
        robot.go_to_object(cube, distance_mm(20)).wait_for_completed()
        robot.set_lift_height(1).wait_for_completed()
        robot.set_lift_height(0).wait_for_completed()"""
    time.sleep(5)
    #robot.set_lift_height(0).wait_for_completed()  # Lever le lift à moitié
    scenario.tap_and_lift_cube(robot)
    #scenario.flip_cube(robot)
#Main
def cozmo_program(robot : cozmo.robot.Robot):
    #Create Crime Inference Motor
    motor = CrimeInference()
    
    robot.say_text("Pas de problème de cubes").wait_for_completed()
    # looks like a paperclip
    cube1 = robot.world.get_light_cube(LightCube1Id)
    # looks like a lamp / heart
    cube2 = robot.world.get_light_cube(LightCube2Id)
    # looks like the letters 'ab' over 'T'
    cube3 = robot.world.get_light_cube(LightCube3Id) 

    print(str(cube1) + "\n" + str(cube2) + "\n" + str(cube3))

    #TODO: ONLY WORK ON PAPERCLIP CUBE
    def on_cube_tapped(event, *, obj, tap_count, tap_duration, **kw): 
        global counterTAP
        #print("Received a tap event "+ str(event.obj.object_id))

        if obj.object_id == 2: 
            counterTAP += 1 
            if (counterTAP % 2) == 1:
                #print("Réponse : Oui")
                Scenario.set_cube_response(True)
            elif (counterTAP % 2) == 0:
                #print("Réponse : Non")
                Scenario.set_cube_response(False)
        else:
            print(f"Cube tapé: {obj.object_id} - Ce n'est pas le cube 2.")

    handler = robot.add_event_handler(cozmo.objects.EvtObjectTapped,on_cube_tapped)
    #pos = robot.pose
    Scene.create_walls(robot)
    #Scene.posDepart(robot)

    #Scene.initializeObjects()
    #Scene.initializeRulesInferenceAndShit()
    scenario = Scenario()
    #testLift(robot, scenario)
    Scenario.mapInit(scenario, robot)
    Scenario.room1(scenario, robot, motor)
    Scenario.room2(scenario, robot, motor)
    Scenario.room3(scenario, robot, motor)
    Scenario.room4(scenario, robot, motor)
    Scenario.room5(scenario, robot, motor)
    Scenario.room6(scenario, robot, motor)
    Scenario.endGame(scenario, robot, motor)
    
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