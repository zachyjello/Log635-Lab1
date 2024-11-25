import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3

# Constantes pour les dimensions des murs
HAUTEUR_MUR = 50
LARGEUR_MUR = 10

arret_depart = Pose(0, 400, 0, angle_z=degrees(0))

class Scene:
    def create_walls(robot: cozmo.robot.Robot):
        # --- MURS HORIZONTAUX ---
        # Define the wall's pose and dimensions
        wall_pose = Pose(0, 400, 100, angle_z=degrees(0))  # Position at x=-400, y=400, z=0, no rotation
        wall_length = 800  # x-dimension in millimeters
        wall_width = 1     # y-dimension in millimeters (very thin wall)
        wall_height = 200   # z-dimension in millimeters

        # Create the unmovable wall
        robot.world.create_custom_fixed_object(
            wall_pose,
            wall_length,
            wall_width,
            wall_height,
            relative_to_robot=True)  # Absolute coordinates
        
        # Define the wall's pose and dimensions
        wall_pose = Pose(0, -400, 100, angle_z=degrees(0))  # Position at x=-400, y=400, z=0, no rotation
        wall_length = 800  # x-dimension in millimeters
        wall_width = 1     # y-dimension in millimeters (very thin wall)
        wall_height = 200   # z-dimension in millimeters

        # Create the unmovable wall
        robot.world.create_custom_fixed_object(
            wall_pose,
            wall_length,
            wall_width,
            wall_height,
            relative_to_robot=True)  # Absolute coordinates

        # --- MURS VERTICAUX ---
        wall_pose = Pose(-400, 0, 100, angle_z=degrees(0))  # Position at x=-400, y=400, z=0, no rotation
        wall_length = 1  # x-dimension in millimeters
        wall_width = 800     # y-dimension in millimeters (very thin wall)
        wall_height = 200   # z-dimension in millimeters

        # Create the unmovable wall
        robot.world.create_custom_fixed_object(
            wall_pose,
            wall_length,
            wall_width,
            wall_height,
            relative_to_robot=True)  # Absolute coordinates
        
        wall_pose = Pose(400, 0, 100, angle_z=degrees(0))  # Position at x=-400, y=400, z=0, no rotation
        wall_length = 1  # x-dimension in millimeters
        wall_width = 800     # y-dimension in millimeters (very thin wall)
        wall_height = 200   # z-dimension in millimeters

        # Create the unmovable wall
        robot.world.create_custom_fixed_object(
            wall_pose,
            wall_length,
            wall_width,
            wall_height,
            relative_to_robot=True)  # Absolute coordinates
        
        wall_pose = Pose(-150, 250, 100, angle_z=degrees(0))  # Position at x=-400, y=400, z=0, no rotation
        wall_length = 1  # x-dimension in millimeters
        wall_width = 300     # y-dimension in millimeters (very thin wall)
        wall_height = 200   # z-dimension in millimeters

        # Create the unmovable wall
        robot.world.create_custom_fixed_object(
            wall_pose,
            wall_length,
            wall_width,
            wall_height,
            relative_to_robot=True)  # Absolute coordinates
        
        wall_pose = Pose(-150, -250, 100, angle_z=degrees(0))  # Position at x=-400, y=400, z=0, no rotation
        wall_length = 1  # x-dimension in millimeters
        wall_width = 300     # y-dimension in millimeters (very thin wall)
        wall_height = 200   # z-dimension in millimeters

        # Create the unmovable wall
        robot.world.create_custom_fixed_object(
            wall_pose,
            wall_length,
            wall_width,
            wall_height,
            relative_to_robot=True)  # Absolute coordinates
        
        wall_pose = Pose(150, 250, 100, angle_z=degrees(0))  # Position at x=-400, y=400, z=0, no rotation
        wall_length = 1  # x-dimension in millimeters
        wall_width = 300     # y-dimension in millimeters (very thin wall)
        wall_height = 200   # z-dimension in millimeters

        # Create the unmovable wall
        robot.world.create_custom_fixed_object(
            wall_pose,
            wall_length,
            wall_width,
            wall_height,
            relative_to_robot=True)  # Absolute coordinates
        
        wall_pose = Pose(150, -250, 100, angle_z=degrees(0))  # Position at x=-400, y=400, z=0, no rotation
        wall_length = 1  # x-dimension in millimeters
        wall_width = 300     # y-dimension in millimeters (very thin wall)
        wall_height = 200   # z-dimension in millimeters

        # Create the unmovable wall
        robot.world.create_custom_fixed_object(
            wall_pose,
            wall_length,
            wall_width,
            wall_height,
            relative_to_robot=True)  # Absolute coordinates

    def posDepart (robot: cozmo.robot.Robot) :
        print(robot.pose.position)
        # Positionner Cozmo au (0,400)
        robot.go_to_pose(arret_depart, relative_to_robot=False).wait_for_completed()
    