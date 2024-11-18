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
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3

ROOM_1_WAY = [Pose(0,-25), Pose(-300, -25), Pose(-300, 200)]
ROOM_2_WAY = [Pose(-300, -25), Pose(0, -25), Pose(0, 200)]
ROOM_3_WAY = [Pose(0, -25), Pose(250, -25), Pose(250, 200)]
ROOM_4_WAY = [Pose(250,-200)]
ROOM_5_WAY = [Pose(250, -25), Pose(0, -25), Pose(0, -200)]
ROOM_6_WAY = [Pose(0,-25), Pose(-300, -25), Pose(-300,-200)]
GO_FETCH_VILLAIN_WAY = [Pose(-300,-25), Pose(250, -25), Pose(250, -200)]
BRING_HIM_TO_PRISON_WAY = [Pose(250, -25), Pose(-300, -25), Pose(-300, -200)]


class Scenario:
    def init():
        pass

    def room1(self):
        self.justMoveToListOfPoseImSayingLittleDevil(ROOM_1_WAY)
        #Ask questions
        #Receive answers
    def room2(self):
        self.justMoveToListOfPoseImSayingLittleDevil(ROOM_2_WAY)
        #Ask questions
        #Receive answers
    def room3(self):
        self.justMoveToListOfPoseImSayingLittleDevil(ROOM_3_WAY)
        #Ask questions
        #Receive answers
    def room4(self):
        self.justMoveToListOfPoseImSayingLittleDevil(ROOM_4_WAY)
        #Ask questions
        #Receive answers
    def room5(self):
        self.justMoveToListOfPoseImSayingLittleDevil(ROOM_5_WAY)
        #Ask questions
        #Receive answers
    def room6(self):
        self.justMoveToListOfPoseImSayingLittleDevil(ROOM_6_WAY)
        #Ask questions
        #Receive answers
    def endGame(self):
        #I KNOW WHO IT IS
        self.justMoveToListOfPoseImSayingLittleDevil(GO_FETCH_VILLAIN_WAY)
        #Hit the cube, take the cube, shit yourself because you can't grab the cube
        self.justMoveToListOfPoseImSayingLittleDevil(BRING_HIM_TO_PRISON_WAY)

    def justMoveToListOfPoseImSayingLittleDevil(robot:cozmo.robot.Robot, listOfPose):
        for position in listOfPose:
            robot.go_to_pose(position).wait_for_completed()
