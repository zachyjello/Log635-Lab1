import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3

# Constantes pour les dimensions des murs
HAUTEUR_MUR = 50
LARGEUR_MUR = 10

arret_depart = Pose(0, 400, 0, angle_z=degrees(0))


def create_walls(robot: cozmo.robot.Robot):
     # --- MURS HORIZONTAUX ---
    mur1 = Pose(0, 800, 0, angle_z=degrees(0))  
    robot.world.create_custom_fixed_object(mur1, 800, LARGEUR_MUR, HAUTEUR_MUR, relative_to_robot=False)
    
    mur2 = Pose(0, 400, 0, angle_z=degrees(0))  
    robot.world.create_custom_fixed_object(mur2, 800, LARGEUR_MUR, HAUTEUR_MUR, relative_to_robot=False)

    mur7 = Pose(25, -400, 0, angle_z=degrees(0))  
    robot.world.create_custom_fixed_object(mur7, 800, LARGEUR_MUR, HAUTEUR_MUR, relative_to_robot=False)

    # --- MURS VERTICAUX ---
    mur3 = Pose(-400, 400, 0, angle_z=degrees(90))  
    robot.world.create_custom_fixed_object(mur3, HAUTEUR_MUR, 400, LARGEUR_MUR, relative_to_robot=False)
    
    mur4 = Pose(-200, 0, 0, angle_z=degrees(90))  
    robot.world.create_custom_fixed_object(mur4, HAUTEUR_MUR, 400, LARGEUR_MUR, relative_to_robot=False)

    mur5 = Pose(100, 0, 0, angle_z=degrees(90))  
    robot.world.create_custom_fixed_object(mur5, HAUTEUR_MUR, 400, LARGEUR_MUR, relative_to_robot=False)

    mur6 = Pose(400, 200, 0, angle_z=degrees(90))  
    robot.world.create_custom_fixed_object(mur6, HAUTEUR_MUR, 400, LARGEUR_MUR, relative_to_robot=False)

def posDepart (robot: cozmo.robot.Robot) :
    print(robot.pose.position)
    # Positionner Cozmo au (0,400)
    robot.go_to_pose(arret_depart, relative_to_robot=False).wait_for_completed()
    