import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3
from Scene import Scene
from CrimeInference import CrimeInference
#from Scenario import Scenario
#from Rules import Rules

#Main
def cozmo_program():
    Scene.create_walls()
    Scene.plot_walls()
    Scene.placeHint()
    
    agent = CrimeInference()
    
    # Conclusions
    print("Pièce du crime : ", agent.get_crime_room())
    print("Arme du crime : ", agent.get_crime_weapon())
    print("Personne victime : ", agent.get_victim())
    print("Heure du crime : ", agent.get_crime_hour())
    print("Meurtrier : ", agent.get_suspect())
    print("Personnes innocentes : ", agent.get_innocent())


cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)