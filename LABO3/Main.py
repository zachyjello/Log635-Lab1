import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3
from Scene import Scene
from CrimeInference import CrimeInference
from Scenario import Scenario
import time

#Compteur de tap sur le cube
counterTAP = 0

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

    #Reagit quand on tape sur le cube
    handler = robot.add_event_handler(cozmo.objects.EvtObjectTapped,on_cube_tapped)

    #Créer les murs dans l'environnement
    Scene.create_walls(robot)

    scenario = Scenario()
    #Ajoute les markeurs dans l'environnement de cozmo
    Scenario.mapInit(scenario, robot)

    #Actions pour les différentes salles
    Scenario.room1(scenario, robot, motor)
    Scenario.room2(scenario, robot, motor)
    Scenario.room3(scenario, robot, motor)
    Scenario.room4(scenario, robot, motor)
    Scenario.room5(scenario, robot, motor)
    Scenario.room6(scenario, robot, motor)
    Scenario.endGame(scenario, robot, motor)

    print("FINISH")

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)