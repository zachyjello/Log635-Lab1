'''
Personnages:  
1-Pikachu                    USED  
2-Évoli                      USED  
3-Dracaufeu                  USED  
4-Ectoplasma                 USED  
5-Carapuce                   USED  
6-Herbizarre                 USED  

Pièces:  
1-BourgPalette                USED  
2-Azuria                      USED  
3-Jadielle                    USED  
4-Lavanville                  USED  
5-Celadopole                  USED  
6-CarminSurMer                USED  

Armes:  
1-BatteBaseballAvecClous      USED
2-PistoletAEau                USED  
3-LanceFlamme                 USED  
4-Tronçonneuse                USED  
5-Poison                      USED  
6-Grenade                     USED  



1-Dracaufeu est mort entre 17h et 20h  
2-Pikachu était à Lavanville entre 16h et 19h  
3-Dracaufeu a été trouvé à Lavanville  
4-Dracaufeu est mort explosé avec la grenade  
5-Une grenade était à Lavanville à 18h


6-Le poison était à CarminSurMer à 20h  
7-Évoli était à Celadopole entre 21h et 22h 
8-La Tronçonneuse était à Jadielle à 17h
9-Le PistoletAEau était à Azuria à 18h
10-Carapuce était au BourgPalette entre 16h et 18h
11-Ectoplasma était à Azuria entre 19h et 21h
12-Herbizarre était à CarminSurMer entre 18h et 19h
13-La BatteBaseballAvecClous était à CarminSurMer à 22h
14-Le LanceFlamme était à Celadopole à 14h

BREF: 
BourgPalette: Carapuce  
Azuria: PistoletAEau, Ectoplasma  
Jadielle: Tronçonneuse  
Lavanville: Dracaufeu(cube victime), Pikachu(cube villain), grenade  
Celadopole: Evoli, LanceFlamme  
CarminSurMer: Poison, Herbizarre, BatteBaseballAvecClous, PRISON  
'''
import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3, Angle

ROOM_1_WAY = [Pose(-300, 0, 0, angle_z=Angle(0)), Pose(-300, 175, 0, angle_z=Angle(0))]
ROOM_2_WAY = [Pose(-300, 0, 0, angle_z=Angle(0)), Pose(0, 0, 0, angle_z=Angle(0)), Pose(0, 175, 0, angle_z=Angle(0))]
ROOM_3_WAY = [Pose(0, 0, 0, angle_z=Angle(0)), Pose(300, 0, 0, angle_z=Angle(0)), Pose(300, 200, 0, angle_z=Angle(0))]
ROOM_4_WAY = [Pose(300,-175, 0, angle_z=Angle(0))]
ROOM_5_WAY = [Pose(300, 0, 0, angle_z=Angle(0)), Pose(0, 0, 0, angle_z=Angle(0)), Pose(0, -175, 0, angle_z=Angle(0))]
ROOM_6_WAY = [Pose(0,0, 0, angle_z=Angle(0)), Pose(-300, 0, 0, angle_z=Angle(0)), Pose(-300,-175, 0, angle_z=Angle(0))]
GO_FETCH_VILLAIN_WAY = [Pose(-300,0, 0, angle_z=Angle(0)), Pose(300, 0, 0, angle_z=Angle(0)), Pose(300, -175, 0, angle_z=Angle(0))]
BRING_HIM_TO_PRISON_WAY = [Pose(300, 0, 0, angle_z=Angle(0)), Pose(-300, 0, 0, angle_z=Angle(0)), Pose(-300, -175, 0, angle_z=Angle(0))]


class Scenario:
    def init():
        pass

    def room1(self, robot: cozmo.robot.Robot):
        print("Room1")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_1_WAY)
        #Ask questions
        #Receive answers
    def room2(self, robot: cozmo.robot.Robot):
        print("Room2")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_2_WAY)
        #Ask questions
        #Receive answers
        self.flip_cube(robot)
    def room3(self, robot: cozmo.robot.Robot):
        print("Room3")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_3_WAY)
        #Ask questions
        #Receive answers
        
    def room4(self, robot: cozmo.robot.Robot):
        print("Room4")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_4_WAY)
        #Ask questions
        #Receive answers
    def room5(self, robot: cozmo.robot.Robot):
        print("Room5")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_5_WAY)
        #Ask questions
        #Receive answers
    def room6(self, robot: cozmo.robot.Robot):
        print("Room6")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_6_WAY)
        #Ask questions
        #Receive answers
    def endGame(self, robot: cozmo.robot.Robot):
        #I KNOW WHO IT IS
        self.justMoveToListOfPoseImSayingLittleDevil(robot, GO_FETCH_VILLAIN_WAY)
        self.tap_and_lift_cube(robot)
        #Hit the cube, take the cube, shit yourself because you can't grab the cube
        self.justMoveToListOfPoseImSayingLittleDevil(robot, BRING_HIM_TO_PRISON_WAY)
        robot.set_lift_height(0).wait_for_completed()


    def justMoveToListOfPoseImSayingLittleDevil(self, robot:cozmo.robot.Robot, listOfPose):
        for position in listOfPose:
            robot.go_to_pose(position).wait_for_completed()

    #TODO: MAKE IT WORK (Async problem)
    def flip_cube(self, robot: cozmo.robot.Robot):
        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
        lookaround.stop()
        if cube is None:
            print("Cube not found!")
            return

        robot.set_lift_height(1).wait_for_completed()
        robot.go_to_object(cube, distance_mm(0.0)).wait_for_completed()  # Stop close to the cube
        robot.set_lift_height(0.4).wait_for_completed()
        robot.drive_straight(distance_mm(-60), speed_mmps(20)).wait_for_completed()  # Reculer légèrement


        #action = robot.roll_cube(cube, check_for_object_on_top=True, num_retries=2)
        #action.wait_for_completed()

    #TODO: MAKE IT WORK
    def tap_and_lift_cube(self, robot: cozmo.robot.Robot):
        # Étape 1 : Attendre que Cozmo détecte un cube
        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
        lookaround.stop()
        if cube is None:
            print("Aucun cube détecté !")
            return

        # Étape 2 : Se rapprocher du cube
        robot.go_to_object(cube, distance_mm(60)).wait_for_completed()

        # Étape 3 : Donner une tape avec le lift
        robot.set_lift_height(1).wait_for_completed()
        robot.drive_straight(distance_mm(20), speed_mmps(20)).wait_for_completed()
        robot.set_lift_height(0.5).wait_for_completed()  # Lever le lift à moitié
        robot.set_lift_height(1).wait_for_completed()  # Lever le lift à moitié
        robot.drive_straight(distance_mm(-40), speed_mmps(20)).wait_for_completed()  # Reculer légèrement
        robot.set_lift_height(0).wait_for_completed()
        robot.go_to_object(cube, distance_mm(0)).wait_for_completed()
        # Étape 4 : Soulever le cube
        robot.set_lift_height(1.0).wait_for_completed()  # Lever complètement le lift
        print("Cube tapé et soulevé avec succès !")