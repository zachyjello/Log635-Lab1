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
FloraVille: Carapuce, BatteBaseballAvecClous
Azuria: PistoletAEau, Ectoplasma  
Jadielle: Tronçonneuse, Pikachu(cube villain)
Lavanville: Dracaufeu(cube victime), grenade  
Celadopole: Evoli, LanceFlamme  
Rotombourg: Poison, Herbizarre, PRISON  
'''
import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3, Angle
import time
import nltk
from nltk import load_parser
from grammars import *
import os


ROOM_1_WAY = [Pose(-300, 0, 0, angle_z=Angle(0)), Pose(-300, 150, 0, angle_z=Angle(0))]
ROOM_2_WAY = [Pose(-300, 0, 0, angle_z=Angle(0)), Pose(0, 0, 0, angle_z=Angle(0)), Pose(0, 150, 0, angle_z=Angle(0))]
ROOM_3_WAY = [Pose(0, 0, 0, angle_z=Angle(0)), Pose(300, 0, 0, angle_z=Angle(0)), Pose(300, 200, 0, angle_z=Angle(0))]
ROOM_4_WAY = [Pose(300,-150, 0, angle_z=Angle(0))]
ROOM_5_WAY = [Pose(300, 0, 0, angle_z=Angle(0)), Pose(0, 0, 0, angle_z=Angle(0)), Pose(0, -150, 0, angle_z=Angle(0))]
ROOM_6_WAY = [Pose(0,0, 0, angle_z=Angle(0)), Pose(-300, 0, 0, angle_z=Angle(0)), Pose(-300,-150, 0, angle_z=Angle(0))]
GO_FETCH_VILLAIN_WAY = [Pose(-300,0, 0, angle_z=Angle(0)), Pose(0, 0, 0, angle_z=Angle(0)), Pose(0, 150, 0, angle_z=Angle(0))]
BRING_HIM_TO_PRISON_WAY = [Pose(0, 0, 0, angle_z=Angle(0)), Pose(-300, 0, 0, angle_z=Angle(0)), Pose(-300, -150, 0, angle_z=Angle(0))]

'''
ROOM_1_WAY = [Pose(-300, 0, 0, angle_z=Angle(0))]
ROOM_2_WAY = [Pose(0, 0, 0, angle_z=Angle(0))]
ROOM_3_WAY = [Pose(300, 0, 0, angle_z=Angle(0))]
ROOM_4_WAY = [Pose(300, 0, 0, angle_z=Angle(0))]
ROOM_5_WAY = [Pose(0, 0, 0, angle_z=Angle(0))]
ROOM_6_WAY = [Pose(-300, 0, 0, angle_z=Angle(0))]
GO_FETCH_VILLAIN_WAY = [Pose(0, 0, 0, angle_z=Angle(0))]
BRING_HIM_TO_PRISON_WAY = [Pose(-300, 0, 0, angle_z=Angle(0))]
'''

class Scenario:

    cube_response=None

    def init():
        print("A quelle heure est morte la victime?")
        
    @classmethod
    def set_cube_response(cls, response):
        cls.cube_response = response

    @classmethod
    def attendre_reponse_cube(cls, timeout=5):
        start_time = time.time()
        print("En attente de la réponse...")

        # Boucle jusqu'à ce qu'une réponse soit reçue ou que le timeout soit atteint
        while (time.time() - start_time) < timeout:
            time.sleep(0.1)  # Attendre un petit moment pour ne pas bloquer totalement

        if cls.cube_response is not None:
            print(f"Réponse reçue : {cls.cube_response}")
        else:
            print("Timeout atteint, aucune réponse reçue.")

        # Réinitialiser la réponse pour la prochaine utilisation
        response = cls.cube_response
        cls.cube_response = None
        return response



    def room1(self, robot: cozmo.robot.Robot, motor):
        print("Room1")
        # self.arme_piece_clause(motor, "BatteBaseball", "Floraville") 
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_1_WAY)
        
        #Ask questions
        #room = self.FindRoom(robot)
        #print("Je suis présentement dans" + room)
        #weapon = self.FindWeapon(robot)
        #print("Je vois l'arme: " + weapon)

        room,weapon,pokemon = self.FindInfos(robot)
        pokemon = 'Dracaufeu'
        print("Je vois " + pokemon)

        print("Est il vivant")
        self.attendre_reponse_cube()
        
        
        #Dire dans quelle piece se trouve l'arme
        # motor.add_clause(weapon + " est dans la " + room)      
        self.arme_piece_clause(motor, weapon, room)  
        #Dire que le pokemon est dans la piece
        # motor.add_clause(pokemon + " est dans la " + room)
        self.personne_piece_clause(motor, pokemon, room)
        #Dire que le pokemon est vivant
        # motor.add_clause(pokemon + " est mort.")
        self.personne_morte_clause(motor, pokemon)

        # motor.add_clause(pokemon + " est tranché.")
        self.personne_marque_clause(motor, pokemon)

        #Receive answers
        print('A quelle heure est mort ' + pokemon)
        hour = input()
        # motor.add_clause(pokemon + 'était dans la '+ room + ' à ' + hour)
        self.personne_morte_heure_clause(motor, pokemon, hour)

        self.personne_piece_heure_clause(motor, pokemon, room, hour)

        # self.flip_cube(robot)
        
        #Receive answers
    def room2(self, robot: cozmo.robot.Robot, motor):
        print("Room2")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_2_WAY)
        #Ask questions
        #room = self.FindRoom(robot)
        #print("Je suis présentement dans" + room)
        #weapon = self.FindWeapon(robot)
        #print("Je vois l'arme: " + weapon)

        room,weapon,pokemon = self.FindInfos(robot)
        pokemon = 'Pikachu'
        print("Je vois " + pokemon)
        
        #Dire dans quelle piece se trouve l'arme
        # motor.add_clause(weapon + " est dans la " + room)      
        self.arme_piece_clause(motor, weapon, room)  
        #Dire que le pokemon est dans la piece
        # motor.add_clause(pokemon + " est dans la " + room)
        self.personne_piece_clause(motor, pokemon, room)
        #Dire que le pokemon est vivant
        # motor.add_clause(pokemon + " est mort.")
        self.personne_vivant_clause(motor, pokemon)
        #Receive answers
        print('où était le pokemon une heure après le crime ')
        room = input()
        self.personne_piece_heure_clause(motor, pokemon, room, "9h")

    def room3(self, robot: cozmo.robot.Robot, motor):
        print("Room3")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_3_WAY)
        
        #Ask questions
        #room = self.FindRoom(robot)
        #print("Je suis présentement dans" + room)
        #weapon = self.FindWeapon(robot)
        #print("Je vois l'arme: " + weapon)
        #pokemon = self.FindPokemon(robot)
        #print("Je vois " + pokemon)

        room,weapon,pokemon = self.FindInfos(robot)
        
        
       #Dire dans quelle piece se trouve l'arme
        # motor.add_clause(weapon + " est dans la " + room)      
        self.arme_piece_clause(motor, weapon, room)  
        #Dire que le pokemon est dans la piece
        # motor.add_clause(pokemon + " est dans la " + room)
        self.personne_piece_clause(motor, pokemon, room)
        #Dire que le pokemon est vivant
        # motor.add_clause(pokemon + " est mort.")
        self.personne_vivant_clause(motor, pokemon)
        #Receive answers
        print('où était le pokemon une heure après le crime ')
        room = input()
        self.personne_piece_heure_clause(motor, pokemon, room, "9h")
        
    def room4(self, robot: cozmo.robot.Robot, motor):
        print("Room4")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_4_WAY)

        #Ask questions
        #room = self.FindRoom(robot)
        #print("Je suis présentement dans" + room)
        #weapon = self.FindWeapon(robot)
        #print("Je vois l'arme: " + weapon)
        #pokemon = self.FindPokemon(robot)
        #print("Je vois " + pokemon)

        room,weapon,pokemon = self.FindInfos(robot)
        
        #Dire dans quelle piece se trouve l'arme
        # motor.add_clause(weapon + " est dans la " + room)      
        self.arme_piece_clause(motor, weapon, room)  
        #Dire que le pokemon est dans la piece
        # motor.add_clause(pokemon + " est dans la " + room)
        self.personne_piece_clause(motor, pokemon, room)
        #Dire que le pokemon est vivant
        # motor.add_clause(pokemon + " est mort.")
        self.personne_vivant_clause(motor, pokemon)
        #Receive answers
        print('où était le pokemon une heure après le crime ')
        room = input()
        self.personne_piece_heure_clause(motor, pokemon, room, "9h")
        
    def room5(self, robot: cozmo.robot.Robot, motor):
        print("Room5")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_5_WAY)
        
        #Ask questions
        #room = self.FindRoom(robot)
        #print("Je suis présentement dans" + room)
        #weapon = self.FindWeapon(robot)
        #print("Je vois l'arme: " + weapon)
        #pokemon = self.FindPokemon(robot)
        #print("Je vois " + pokemon)
        
        room,weapon,pokemon = self.FindInfos(robot)
        
        #Dire dans quelle piece se trouve l'arme
        # motor.add_clause(weapon + " est dans la " + room)      
        self.arme_piece_clause(motor, weapon, room)  
        #Dire que le pokemon est dans la piece
        # motor.add_clause(pokemon + " est dans la " + room)
        self.personne_piece_clause(motor, pokemon, room)
        #Dire que le pokemon est vivant
        # motor.add_clause(pokemon + " est mort.")
        self.personne_vivant_clause(motor, pokemon)
        #Receive answers
        print('où était le pokemon une heure après le crime ')
        room = input()
        self.personne_piece_heure_clause(motor, pokemon, room, "9h")

    def room6(self, robot: cozmo.robot.Robot, motor):
        print("Room6")
        self.justMoveToListOfPoseImSayingLittleDevil(robot, ROOM_6_WAY)
        
        #Ask questions
        #room = self.FindRoom(robot)
        #print("Je suis présentement dans" + room)
        #weapon = self.FindWeapon(robot)
        #print("Je vois l'arme: " + weapon)
        #pokemon = self.FindPokemon(robot)
        #print("Je vois " + pokemon)

        room,weapon,pokemon = self.FindInfos(robot)
        
        #Dire dans quelle piece se trouve l'arme
        # motor.add_clause(weapon + " est dans la " + room)      
        self.arme_piece_clause(motor, weapon, room)  
        #Dire que le pokemon est dans la piece
        # motor.add_clause(pokemon + " est dans la " + room)
        self.personne_piece_clause(motor, pokemon, room)
        #Dire que le pokemon est vivant
        # motor.add_clause(pokemon + " est mort.")
        self.personne_vivant_clause(motor, pokemon)
        #Receive answers
        print('où était le pokemon une heure après le crime ')
        room = input()
        self.personne_piece_heure_clause(motor, pokemon, room, "9h")
        
    def endGame(self, robot: cozmo.robot.Robot, motor):

        print(motor.get_suspect())
        
        #I KNOW WHO IT IS
        self.justMoveToListOfPoseImSayingLittleDevil(robot, GO_FETCH_VILLAIN_WAY)
        #self.tap_and_lift_cube(robot)
        time.sleep(10)
        robot.set_lift_height(1).wait_for_completed()
        #Hit the cube, take the cube, shit yourself because you can't grab the cube
        self.justMoveToListOfPoseImSayingLittleDevil(robot, BRING_HIM_TO_PRISON_WAY)
        robot.set_lift_height(0).wait_for_completed()


    def justMoveToListOfPoseImSayingLittleDevil(self, robot:cozmo.robot.Robot, listOfPose):
        for position in listOfPose:
            print("move")
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

    def FindInfos(self, robot:cozmo.robot.Robot):
        qui = None
        ou = None
        quoi = None

        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        object_found = robot.world.wait_until_observe_num_objects(num=3, timeout=60) #LOOK TIMEOUTS
        lookaround.stop()
        for obj in object_found:
            try:
                recognized_thing = obj.object_type
                # print(obj)
            except:
                recognized_thing = None
            if recognized_thing == CustomObjectTypes.CustomType00:
                print("Je suis présentement dans" + "Floraville")
                ou = "Floraville"
            elif recognized_thing == CustomObjectTypes.CustomType03:
                print("Je suis présentement dans" + "Azuria")
                ou = "Azuria"
            elif recognized_thing == CustomObjectTypes.CustomType06:
                print("Je suis présentement dans" + "Jadielle")
                ou = "Jadielle"
            elif recognized_thing == CustomObjectTypes.CustomType08:
                print("Je suis présentement dans" + "Lavanville")
                ou = "Lavanville"
            elif recognized_thing == CustomObjectTypes.CustomType10:
                print("Je suis présentement dans" + "Celadopole")
                ou = "Celadopole"
            elif recognized_thing == CustomObjectTypes.CustomType13:
                print("Je suis présentement dans" + "Rotombourg")
                ou = "Rotombourg"
            elif recognized_thing == CustomObjectTypes.CustomType02:
                print("Je vois " + "Carapuce")
                qui = "Carapuce"
            elif recognized_thing == CustomObjectTypes.CustomType05:
                print("Je vois " + "Ectoplasma")
                qui = "Ectoplasma"
            elif recognized_thing == CustomObjectTypes.CustomType12:
                print("Je vois " + "Evoli")
                qui = "Evoli"
            elif recognized_thing == CustomObjectTypes.CustomType15:
                print("Je vois " + "Herbizarre")
                qui = "Herbizarre"
            elif recognized_thing == CustomObjectTypes.CustomType01:
                print("Je vois l'arme: " + "Poison")
                quoi = "Poison"
            elif recognized_thing == CustomObjectTypes.CustomType04:
                print("Je vois l'arme: " + "PistoletEau")
                quoi = "PistoletEau"
            elif recognized_thing == CustomObjectTypes.CustomType07:
                print("Je vois l'arme: " + "Tronconneuse")
                quoi = "Tronconneuse"
            elif recognized_thing == CustomObjectTypes.CustomType09:
                print("Je vois l'arme: " + "Grenade")
                quoi = "Grenade"
            elif recognized_thing == CustomObjectTypes.CustomType11:
                print("Je vois l'arme: " + "LanceFlamme")
                quoi = "LanceFlamme"
            elif recognized_thing == CustomObjectTypes.CustomType14:
                print("Je vois l'arme: " + "BatteBaseball")
                quoi = "BatteBaseball"
            else:
                pass
        #robot.start_behavior(cozmo.behavior.Behavior.stop)
        #robot.drive_straight(distance_mm(0), speed_mmps(0)).wait_for_completed()  # Stop movement
        lookaround.stop()
        lookaround.stop()
        lookaround.stop()
        return (ou,quoi,qui)
        
    def FindRoom(self, robot:cozmo.robot.Robot):
        notFound = True
        while notFound:
            lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
            object_found = robot.world.wait_until_observe_num_objects(num=3, timeout=60) #LOOK TIMEOUTS
            for obj in object_found:
                try:
                    recognized_thing = obj.object_type
                    # print(obj)
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
            object_found = robot.world.wait_until_observe_num_objects(num=3, timeout=60) #LOOK TIMEOUTS
            for obj in object_found:
                try:
                    recognized_thing = obj.object_type
                    # print(obj)
                except:
                    recognized_thing = None
                if recognized_thing == CustomObjectTypes.CustomType01:
                    notFound = False
                    return "Poison"
                elif recognized_thing == CustomObjectTypes.CustomType04:
                    notFound = False
                    return "PistoletEau"
                elif recognized_thing == CustomObjectTypes.CustomType07:
                    notFound = False
                    return "Tronconneuse"
                elif recognized_thing == CustomObjectTypes.CustomType09:
                    notFound = False
                    return "Grenade"
                elif recognized_thing == CustomObjectTypes.CustomType11:
                    notFound = False
                    return "LanceFlamme"
                elif recognized_thing == CustomObjectTypes.CustomType14:
                    notFound = False
                    return "BatteBaseball"
    
    def FindPokemon(self, robot:cozmo.robot.Robot):
        notFound = True
        while notFound:
            lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
            object_found = robot.world.wait_until_observe_num_objects(num=3, timeout=60) #LOOK TIMEOUTS
            for obj in object_found:
                try:
                    recognized_thing = obj.object_type
                    # print(obj)
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
                    return "Evoli"
                elif recognized_thing == CustomObjectTypes.CustomType15:
                    notFound = False
                    return "Herbizarre"
                elif recognized_thing == LightCube1Id:
                    notFound = False
                    return "Pikachu"
                elif recognized_thing == LightCube3Id:
                    notFound = False
                    return "Dracaufeu"

    def mapInit(self, robot: cozmo.robot.Robot):
        robot.world.define_custom_wall(CustomObjectTypes.CustomType00,
                                   CustomObjectMarkers.Triangles2,
                                   60, 60, 50, 50, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType01,
                                    CustomObjectMarkers.Circles2,
                                    60, 60, 50, 50, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType02,
                                    CustomObjectMarkers.Diamonds2,
                                    60, 60, 50, 50, True)
        
        robot.world.define_custom_wall(CustomObjectTypes.CustomType03,
                                    CustomObjectMarkers.Hexagons2,
                                    60, 60, 50, 50, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType04,
                                    CustomObjectMarkers.Triangles3,
                                    60, 60, 50, 50, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType05,
                                    CustomObjectMarkers.Circles3,
                                    60, 60, 50, 50, True)
        
        robot.world.define_custom_wall(CustomObjectTypes.CustomType06,
                                    CustomObjectMarkers.Diamonds3,
                                    60, 60, 50, 50, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType07,
                                    CustomObjectMarkers.Hexagons3,
                                    60, 60, 50, 50, True)
    
        robot.world.define_custom_wall(CustomObjectTypes.CustomType08,
                                    CustomObjectMarkers.Triangles4,
                                    60, 60, 50, 50, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType09,
                                    CustomObjectMarkers.Circles4,
                                    60, 60, 50, 50, True)
        
        robot.world.define_custom_wall(CustomObjectTypes.CustomType10,
                                    CustomObjectMarkers.Diamonds4,
                                    60, 60, 50, 50, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType11,
                                    CustomObjectMarkers.Hexagons4,
                                    60, 60, 50, 50, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType12,
                                    CustomObjectMarkers.Triangles5,
                                    60, 60, 50, 50, True)
        
        robot.world.define_custom_wall(CustomObjectTypes.CustomType13,
                                    CustomObjectMarkers.Circles5,
                                    60, 60, 50, 50, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType14,
                                    CustomObjectMarkers.Diamonds5,
                                    60, 60, 50, 50, True)
        robot.world.define_custom_wall(CustomObjectTypes.CustomType15,
                                    CustomObjectMarkers.Hexagons5,
                                    60, 60, 50, 50, True)
    
    def arme_piece_clause(self, motor, arme, piece):
        grammar_path = ".\\LABO3\\grammars\\arme_piece.fcfg"  
        parser = load_parser(grammar_path, trace=0)

        # Example sentence
        sentence = f"Le {arme} est dans la {piece}".split()

        for tree in parser.parse(sentence):
            semantic_representation = tree.label()['SEM']
            # Add the semantic representation to the knowledge base
            motor.add_clause(str(semantic_representation))
    
    def personne_marque_clause(self, motor, pokemon):
        grammar_path = '.\\LABO3\\grammars\\personne_marque.fcfg'  
        parser = load_parser(grammar_path, trace=0)

        # Example sentence
        sentence = f"{pokemon} est tranché".split()

        for tree in parser.parse(sentence):
            semantic_representation = tree.label()['SEM']
            # Add the semantic representation to the knowledge base
            motor.add_clause(str(semantic_representation))

    def personne_morte_heure_clause(self, motor, pokemon, heure):
        grammar_path = '.\\LABO3\\grammars\\personne_morte_heure.fcfg'  
        parser = load_parser(grammar_path, trace=0)

        # Example sentence
        sentence = f"{pokemon} est mort à {heure}".split()

        for tree in parser.parse(sentence):
            semantic_representation = tree.label()['SEM']
            # Add the semantic representation to the knowledge base
            motor.add_clause(str(semantic_representation))
    
    def personne_morte_clause(self, motor, pokemon):
        grammar_path = '.\\LABO3\\grammars\\personne_morte.fcfg'  
        parser = load_parser(grammar_path, trace=0)

        # Example sentence
        sentence = f"{pokemon} est mort".split()

        for tree in parser.parse(sentence):
            semantic_representation = tree.label()['SEM']
            # Add the semantic representation to the knowledge base
            motor.add_clause(str(semantic_representation))
    
    def personne_piece_heure_clause(self, motor, pokemon, piece, heure):
        grammar_path = '.\\LABO3\\grammars\\personne_piece_heure.fcfg'  
        parser = load_parser(grammar_path, trace=0)

        # Example sentence
        sentence = f"{pokemon} était dans la {piece} à {heure}".split()

        for tree in parser.parse(sentence):
            semantic_representation = tree.label()['SEM']
            # Add the semantic representation to the knowledge base
            motor.add_clause(str(semantic_representation))

    def personne_piece_clause(self, motor, pokemon, piece):
        grammar_path = '.\\LABO3\\grammars\\personne_piece.fcfg'  
        parser = load_parser(grammar_path, trace=0)

        # Example sentence
        sentence = f"{pokemon} est dans la {piece}".split()

        for tree in parser.parse(sentence):
            semantic_representation = tree.label()['SEM']
            # Add the semantic representation to the knowledge base
            motor.add_clause(str(semantic_representation))

    def personne_vivant_clause(self, motor, pokemon):
        grammar_path = '.\\LABO3\\grammars\\personne_vivant.fcfg'  
        parser = load_parser(grammar_path, trace=0)

        # Example sentence
        sentence = f"{pokemon} est vivant".split()

        for tree in parser.parse(sentence):
            semantic_representation = tree.label()['SEM']
            # Add the semantic representation to the knowledge base
            motor.add_clause(str(semantic_representation))
