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
        print("A quelle heure est morte la victime?")
        

    def room1(self, robot: cozmo.robot.Robot, motor):
        print("Room1")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_1_WAY)
        
        #Ask questions
        room = self.FindRoom(self, robot)
        print("Je suis présentement dans" + room)
        weapon = self.FindWeapon(self, robot)
        print("Je vois l'arme: " + weapon)
        pokemon = self.FindPokemon(self, robot)
        print("Je vois " + pokemon)
        
        
        #Dire dans quelle piece se trouve l'arme
        motor.add_clause(weapon + " est dans la " + room)        
        #Dire que le pokemon est dans la piece
        motor.add_clause(pokemon + " est dans la " + room)
        #Dire que le pokemon est vivant
        motor.add_clause(pokemon + " est vivant.")
        
        #Receive answers
    def room2(self, robot: cozmo.robot.Robot, motor):
        print("Room2")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_2_WAY)
        #Ask questions
        room = self.FindRoom(self, robot)
        print("Je suis présentement dans" + room)
        weapon = self.FindWeapon(self, robot)
        print("Je vois l'arme: " + weapon)
        pokemon = self.FindPokemon(self, robot)
        print("Je vois " + pokemon)
        
        
        #Dire dans quelle piece se trouve l'arme
        motor.add_clause(weapon + " est dans la " + room)        
        #Dire que le pokemon est dans la piece
        motor.add_clause(pokemon + " est dans la " + room)
        #Dire que le pokemon est vivant
        motor.add_clause(pokemon + " est vivant.")
        #Receive answers
    def room3(self, robot: cozmo.robot.Robot, motor):
        print("Room3")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_3_WAY)
        
        #Ask questions
        room = self.FindRoom(self, robot)
        print("Je suis présentement dans" + room)
        weapon = self.FindWeapon(self, robot)
        print("Je vois l'arme: " + weapon)
        pokemon = self.FindPokemon(self, robot)
        print("Je vois " + pokemon)
        
        
        #Dire dans quelle piece se trouve l'arme
        motor.add_clause(weapon + " est dans la " + room)        
        #Dire que le pokemon est dans la piece
        motor.add_clause(pokemon + " est dans la " + room)
        #Dire que le pokemon est vivant
        motor.add_clause(pokemon + " est vivant.")
        #Receive answers
        self.flip_cube(robot)
        
    def room4(self, robot: cozmo.robot.Robot, motor):
        print("Room4")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_4_WAY)
        #Ask questions
        room = self.FindRoom(self, robot)
        print("Je suis présentement dans" + room)
        weapon = self.FindWeapon(self, robot)
        print("Je vois l'arme: " + weapon)
        pokemon = "Dracaufeu"
        print("Je vois " + pokemon)
        
        #Dire dans quelle piece se trouve l'arme
        motor.add_clause(weapon + " est dans la " + room)        
        #Dire que le pokemon est dans la piece
        motor.add_clause(pokemon + " est dans la " + room)
        #Dire que le pokemon est vivant
        motor.add_clause(pokemon + " est mort.")
        #Dire que le pokemon est tranché
        motor.add_clause(pokemon + " est tranché.")
        #Receive answers
    def room5(self, robot: cozmo.robot.Robot, motor):
        print("Room5")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_5_WAY)
        
        #Ask questions
        room = self.FindRoom(self, robot)
        print("Je suis présentement dans" + room)
        weapon = self.FindWeapon(self, robot)
        print("Je vois l'arme: " + weapon)
        pokemon = self.FindPokemon(self, robot)
        print("Je vois " + pokemon)
        
        
        #Dire dans quelle piece se trouve l'arme
        motor.add_clause(weapon + " est dans la " + room)        
        #Dire que le pokemon est dans la piece
        motor.add_clause(pokemon + " est dans la " + room)
        #Dire que le pokemon est vivant
        motor.add_clause(pokemon + " est vivant.")
        #Receive answers
    def room6(self, robot: cozmo.robot.Robot, motor):
        print("Room6")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_6_WAY)
        
        #Ask questions
        room = self.FindRoom(self, robot)
        print("Je suis présentement dans" + room)
        weapon = self.FindWeapon(self, robot)
        print("Je vois l'arme: " + weapon)
        pokemon = self.FindPokemon(self, robot)
        print("Je vois " + pokemon)
        
        
        #Dire dans quelle piece se trouve l'arme
        motor.add_clause(weapon + " est dans la " + room)        
        #Dire que le pokemon est dans la piece
        motor.add_clause(pokemon + " est dans la " + room)
        #Dire que le pokemon est vivant
        motor.add_clause(pokemon + " est vivant.")
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

        robot.go_to_object(cube, distance_mm(50.0)).wait_for_completed()  # Stop close to the cube
        action = robot.roll_cube(cube, check_for_object_on_top=True, num_retries=2)
        action.wait_for_completed()

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
        robot.go_to_object(cube, distance_mm(20)).wait_for_completed()

        # Étape 3 : Donner une tape avec le lift
        robot.set_lift_height(1).wait_for_completed()
        robot.drive_straight(distance_mm(15), speed_mmps(20)).wait_for_completed()
        robot.set_lift_height(0.5).wait_for_completed()  # Lever le lift à moitié
        robot.drive_straight(distance_mm(-10), speed_mmps(20)).wait_for_completed()  # Reculer légèrement
        robot.set_lift_height(0).wait_for_completed()
        robot.go_to_object(cube, distance_mm(20)).wait_for_completed()
        # Étape 4 : Soulever le cube
        robot.set_lift_height(1.0).wait_for_completed()  # Lever complètement le lift
        print("Cube tapé et soulevé avec succès !")
        
    def FindRoom(self, robot:cozmo.robot.Robot):
        notFound = True
        while notFound:
            lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
            object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60) #LOOK TIMEOUTS
            for obj in object_found:
                try:
                    recognized_thing = obj.object_type
                    print(obj)
                except:
                    recognized_thing = None
                if recognized_thing == CustomObjectTypes.CustomType00:
                    notFound = False
                    return "Floraville"
                elif recognized_thing == CustomObjectTypes.CustomType03:
                    notFound = False
                    return "Azuria"
                elif recognized_thing == CustomObjectTypes.CustomType06:
                    notFound = False
                    return "Jadielle"
                elif recognized_thing == CustomObjectTypes.CustomType08:
                    notFound = False
                    return "Lavanville"
                elif recognized_thing == CustomObjectTypes.CustomType10:
                    notFound = False
                    return "Celadopole"
                elif recognized_thing == CustomObjectTypes.CustomType13:
                    notFound = False
                    return "Rotombourg"
                
    def FindWeapon(self, robot:cozmo.robot.Robot):
        notFound = True
        while notFound:
            lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
            object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60) #LOOK TIMEOUTS
            for obj in object_found:
                try:
                    recognized_thing = obj.object_type
                    print(obj)
                except:
                    recognized_thing = None
                if recognized_thing == CustomObjectTypes.CustomType01:
                    notFound = False
                    return "Poison"
                elif recognized_thing == CustomObjectTypes.CustomType04:
                    notFound = False
                    return "WaterGun"
                elif recognized_thing == CustomObjectTypes.CustomType07:
                    notFound = False
                    return "Tronçonneuse"
                elif recognized_thing == CustomObjectTypes.CustomType09:
                    notFound = False
                    return "Grenade"
                elif recognized_thing == CustomObjectTypes.CustomType11:
                    notFound = False
                    return "LanceFlamme"
                elif recognized_thing == CustomObjectTypes.CustomType14:
                    notFound = False
                    return "BatteBaseballAvecClous"
    
    def FindPokemon(self, robot:cozmo.robot.Robot):
        notFound = True
        while notFound:
            lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
            object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60) #LOOK TIMEOUTS
            for obj in object_found:
                try:
                    recognized_thing = obj.object_type
                    print(obj)
                except:
                    recognized_thing = None
                if recognized_thing == CustomObjectTypes.CustomType02:
                    notFound = False
                    return "Carapuce"
                elif recognized_thing == CustomObjectTypes.CustomType05:
                    notFound = False
                    return "Ectoplasma"
                elif recognized_thing == CustomObjectTypes.CustomType12:
                    notFound = False
                    return "Evioli"
                elif recognized_thing == CustomObjectTypes.CustomType15:
                    notFound = False
                    return "Herbizarre"

    def mapInit(self, robot: cozmo.robot.Robot):
        robot.world.define_custom_wall(CustomObjectTypes.CustomType00,
                                   CustomObjectMarkers.Triangles2,
                                   50, 58, 26, 26, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType01,
                                    CustomObjectMarkers.Circles2,
                                    50, 58, 26, 26, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType02,
                                    CustomObjectMarkers.Diamonds2,
                                    50, 58, 26, 26, True)
        
        robot.world.define_custom_wall(CustomObjectTypes.CustomType03,
                                    CustomObjectMarkers.Hexagons2,
                                    50, 58, 26, 26, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType04,
                                    CustomObjectMarkers.Triangles3,
                                    50, 58, 26, 26, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType05,
                                    CustomObjectMarkers.Circles3,
                                    50, 58, 26, 26, True)
        
        robot.world.define_custom_wall(CustomObjectTypes.CustomType06,
                                    CustomObjectMarkers.Diamonds3,
                                    50, 58, 26, 26, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType07,
                                    CustomObjectMarkers.Hexagons3,
                                    50, 58, 26, 26, True)
    
        robot.world.define_custom_wall(CustomObjectTypes.CustomType08,
                                    CustomObjectMarkers.Triangles4,
                                    50, 58, 26, 26, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType09,
                                    CustomObjectMarkers.Circles4,
                                    50, 58, 26, 26, True)
        
        robot.world.define_custom_wall(CustomObjectTypes.CustomType10,
                                    CustomObjectMarkers.Diamonds4,
                                    50, 58, 26, 26, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType11,
                                    CustomObjectMarkers.Hexagons4,
                                    50, 58, 26, 26, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType12,
                                    CustomObjectMarkers.Triangles5,
                                    50, 58, 26, 26, True)
        
        robot.world.define_custom_wall(CustomObjectTypes.CustomType13,
                                    CustomObjectMarkers.Circles5,
                                    50, 58, 26, 26, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType14,
                                    CustomObjectMarkers.Diamonds5,
                                    50, 58, 26, 26, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType15,
                                    CustomObjectMarkers.Hexagons5,
                                    50, 58, 26, 26, True)