import time
from time import strftime
import asyncio
import os
import cozmo
from PIL import Image
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject, LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import Pose, degrees, distance_mm, speed_mmps, Vector3

alreadyDoneImages = []
liveCamera = False
fullPath = "photos"
index = 0

def createAllDirectories():
    # Indiquer le dossier pour stocker les photos
    if not os.path.exists('photos'):
        os.makedirs('photos')
    if not os.path.exists('photos/Triangles'):
        os.makedirs('photos/Triangles')
    if not os.path.exists('photos/Triangles/Triangle2'):
        os.makedirs('photos/Triangles/Triangle2')
    if not os.path.exists('photos/Triangles/Triangle3'):
        os.makedirs('photos/Triangles/Triangle3')
    if not os.path.exists('photos/Triangles/Triangle4'):
        os.makedirs('photos/Triangles/Triangle4')
    if not os.path.exists('photos/Triangles/Triangle5'):
        os.makedirs('photos/Triangles/Triangle5')
    if not os.path.exists('photos/Hexagons'):
        os.makedirs('photos/Hexagons')
    if not os.path.exists('photos/Hexagons/Hexagon2'):
        os.makedirs('photos/Hexagons/Hexagon2')
    if not os.path.exists('photos/Hexagons/Hexagon3'):
        os.makedirs('photos/Hexagons/Hexagon3')
    if not os.path.exists('photos/Hexagons/Hexagon4'):
        os.makedirs('photos/Hexagons/Hexagon4')
    if not os.path.exists('photos/Hexagons/Hexagon5'):
        os.makedirs('photos/Hexagons/Hexagon5')
    if not os.path.exists('photos/Diamonds'):
        os.makedirs('photos/Diamonds')
    if not os.path.exists('photos/Diamonds/Diamond2'):
        os.makedirs('photos/Diamonds/Diamond2')
    if not os.path.exists('photos/Diamonds/Diamond3'):
        os.makedirs('photos/Diamonds/Diamond3')
    if not os.path.exists('photos/Diamonds/Diamond4'):
        os.makedirs('photos/Diamonds/Diamond4')
    if not os.path.exists('photos/Diamonds/Diamond5'):
        os.makedirs('photos/Diamonds/Diamond5')
    if not os.path.exists('photos/Circles'):
        os.makedirs('photos/Circles')
    if not os.path.exists('photos/Circles/Circle2'):
        os.makedirs('photos/Circles/Circle2')
    if not os.path.exists('photos/Circles/Circle3'):
        os.makedirs('photos/Circles/Circle3')
    if not os.path.exists('photos/Circles/Circle4'):
        os.makedirs('photos/Circles/Circle4')
    if not os.path.exists('photos/Circles/Circle5'):
        os.makedirs('photos/Circles/Circle5')

#TRY
def move_in_front_of_object(robot:cozmo.robot.Robot, obj, distance_from_object_mm=100):
    # Get object's pose
    object_pose = obj.pose

    # Calculate position in front of the object
    #distance = distance_mm(distance_from_object_mm)
    target_x = object_pose.position.x - distance_from_object_mm * object_pose.rotation.cos_z
    target_y = object_pose.position.y - distance_from_object_mm * object_pose.rotation.sin_z
    target_angle = object_pose.rotation.angle_z.degrees  # Same angle as the object

    # Move Cozmo to the target position and face the object
    target_pose = Pose(target_x, target_y, 0, angle_z=degrees(target_angle))
    robot.go_to_pose(target_pose).wait_for_completed()
#TRY

def on_new_camera_image(evt, **kwargs):    
    global liveCamera
    global fullPath
    if liveCamera:
        print("Cozmo is taking a photo")
        pilImage = kwargs['image'].raw_image
        existing_photos = [f for f in os.listdir(fullPath) if f.startswith("photo_") and f.endswith(".jpg")]
        photo_count = len(existing_photos)  # Count of existing photos

        # Increment the count for the new photo
        new_photo_index = photo_count + 1
        filename = f"photo_{new_photo_index:02d}.jpg"  # Format with leading zero
        fullPathModified = os.path.join(fullPath, filename)

        pilImage.save(fullPathModified, "JPEG")

def TakePhoto(robot: cozmo.robot.Robot, path):
    global liveCamera
    global fullPath
    fullPath=path
    # Assurez-vous que la tête et le bras de Cozmo sont à un niveau raisonnable
    robot.set_head_angle(degrees(10.0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()

    liveCamera = True
    time.sleep(0.1)    
    liveCamera = False


#TALK
def action_for_marker_0(robot: cozmo.robot.Robot):
    print("I do action 0")
    robot.say_text("My name is Sacha from Bourg Palette").wait_for_completed()

#EMOTION
def action_for_marker_1(robot: cozmo.robot.Robot):
    print("I do action 1")
    robot.play_anim_trigger(cozmo.anim.Triggers.Surprise).wait_for_completed()

#STACK CUBES
def action_for_marker_2(robot: cozmo.robot.Robot):
    print("I do action 2")
    robot.say_text("Pokemon, gotta catch em' all!").wait_for_completed()

def action_for_marker_3(robot: cozmo.robot.Robot):
    print("I do action 3")
    light_when_face(robot)

def action_for_marker_4(robot: cozmo.robot.Robot):
    print("I do action 4")
    cozmo_move_around(robot)

def action_for_marker_5(robot: cozmo.robot.Robot):
    print("I do action 5")
    robot.say_text("I will be the very best").wait_for_completed()

def action_for_marker_6(robot: cozmo.robot.Robot):
    print("I do action 6")
    robot.play_anim_trigger(robot.anim_triggers[3]).wait_for_completed()

def action_for_marker_7(robot: cozmo.robot.Robot):
    print("I do action 7")
    robot.say_text("Pikachu I choose you").wait_for_completed()

def action_for_marker_8(robot: cozmo.robot.Robot):
    print("I do action 8")
    robot.say_text("Pikachu I'm glad I choosed you").wait_for_completed()

def action_for_marker_9(robot: cozmo.robot.Robot):
    show_pokemon_pic(robot)

def action_for_marker_10(robot: cozmo.robot.Robot):
    print("I do action 10")
    robot.drive_straight(distance_mm(-75), speed_mmps(100)).wait_for_completed()
    robot.drive_straight(distance_mm(150), speed_mmps(100)).wait_for_completed()
    robot.drive_straight(distance_mm(-75), speed_mmps(100)).wait_for_completed()
    nothing = True

def action_for_marker_11(robot: cozmo.robot.Robot):
    print("I do action 11")
    robot.say_text("A legendary bird, launch the master ball").wait_for_completed()

def action_for_marker_12(robot: cozmo.robot.Robot):
    print("I do action 12")
    #This is mine Zach touch it and you died: no <3 Je t'aime Zach
    robot.turn_in_place(degrees(45)).wait_for_completed()
    robot.drive_straight(distance_mm(75), speed_mmps(100)).wait_for_completed()
    robot.turn_in_place(degrees(-45)).wait_for_completed()
    robot.drive_straight(distance_mm(75), speed_mmps(100)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(75), speed_mmps(100)).wait_for_completed()
    robot.turn_in_place(degrees(-45)).wait_for_completed()
    robot.drive_straight(distance_mm(75), speed_mmps(100)).wait_for_completed()

def action_for_marker_13(robot: cozmo.robot.Robot):
    print("I do action 13")
    robot.play_anim_trigger(robot.anim_triggers[5]).wait_for_completed()


def action_for_marker_14(robot: cozmo.robot.Robot):
    global index
    print("I do action 14")
    index += 1
    cozmo_cube_action(robot, index)

def action_for_marker_15(robot: cozmo.robot.Robot):
    global index
    print("I do action 15")
    index += 1
    cozmo_cube_action(robot, index)

def cozmo_program(robot: cozmo.robot.Robot):
    createAllDirectories()
    
    # Chaque fois que Cozmo voit une "nouvelle" image, prends une photo
    robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)

    #Création des objets customs
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

    time.sleep(1)

    while len(alreadyDoneImages) < 16:
        # Chercher les objets
        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60) #LOOK TIMEOUTS
        lookaround.stop()
        # visible_objects = robot.world.visible_objects
        #detected_objects = robot.world.visible_objects
        i = 0
        for obj in object_found:
            # Vérifiez si l'objet est un marqueur que vous surveillez
            try:
                reconized_thing = obj.object_type
                print(obj)
            except:
                reconized_thing = None
            if reconized_thing not in alreadyDoneImages:
                if reconized_thing == CustomObjectTypes.CustomType00:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(200), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType00:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Triangles/Triangle2/") #TODO: For each picture make sure you're in front, so hardcode some position
                    action_for_marker_0(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    
                    alreadyDoneImages.append(CustomObjectTypes.CustomType00)
                    break
                if reconized_thing == CustomObjectTypes.CustomType01:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType01:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Circles/Circle2/")
                    action_for_marker_1(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType01)
                    break
                if reconized_thing == CustomObjectTypes.CustomType02:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType02:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Diamonds/Diamond2/")
                    action_for_marker_2(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType02)
                    break
                if reconized_thing == CustomObjectTypes.CustomType03:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType03:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Hexagons/Hexagon2/")
                    action_for_marker_3(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType03)
                    break
                if reconized_thing == CustomObjectTypes.CustomType04:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType04:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Triangles/Triangle3/")
                    action_for_marker_4(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType04)
                    break
                if reconized_thing == CustomObjectTypes.CustomType05:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType05:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Circles/Circle3/")
                    action_for_marker_5(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType05)
                    break
                if reconized_thing == CustomObjectTypes.CustomType06:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType06:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Diamonds/Diamond3/")
                    action_for_marker_6(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType06)
                    break
                if reconized_thing == CustomObjectTypes.CustomType07:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType07:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Hexagons/Hexagon3/")
                    action_for_marker_7(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType07)
                    break
                if reconized_thing == CustomObjectTypes.CustomType08:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType08:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Triangles/Triangle4/")
                    action_for_marker_8(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType08)
                    break
                if reconized_thing == CustomObjectTypes.CustomType09:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType09:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Circles/Circle4/")
                    action_for_marker_9(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType09)
                    break
                if reconized_thing == CustomObjectTypes.CustomType10:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType10:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Diamonds/Diamond4/")
                    action_for_marker_10(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType10)
                    break
                if reconized_thing == CustomObjectTypes.CustomType11:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType11:
                            sawTheRightOne = True
                        time.sleep(0.1)
                    TakePhoto(robot, "photos/Hexagons/Hexagon4/")
                    action_for_marker_11(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType11)
                    break
                if reconized_thing == CustomObjectTypes.CustomType12:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType12:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Triangles/Triangle5/")
                    action_for_marker_12(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType12)
                    break
                if reconized_thing == CustomObjectTypes.CustomType13:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType13:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Circles/Circle5/")
                    action_for_marker_13(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType13)
                    break
                if reconized_thing == CustomObjectTypes.CustomType14:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType14:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Diamonds/Diamond5/")
                    action_for_marker_14(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType14)
                    break
                if reconized_thing == CustomObjectTypes.CustomType15:
                    initial_pose = robot.pose
                    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()
                    sawTheRightOne = False
                    while sawTheRightOne == False:
                        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
                        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60)
                        lookaround.stop()
                        try:
                            reconized_thing2 = obj.object_type
                        except:
                            reconized_thing2 = None
                        if reconized_thing2 == CustomObjectTypes.CustomType15:
                            sawTheRightOne = True
                            time.sleep(0.1)
                    TakePhoto(robot, "photos/Hexagons/Hexagon5/")
                    action_for_marker_15(robot)
                    robot.go_to_pose(initial_pose).wait_for_completed()
                    alreadyDoneImages.append(CustomObjectTypes.CustomType15)
                    break
    
    print("I'm done here, it's getting dark in here, goodbye")
    while True:
        time.sleep(0.1)

    
def light_when_face(robot: cozmo.robot.Robot):
    '''The core of the light_when_face program'''

    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    face = None
    
    hasNotSeenFace = True
    
    print("Press CTRL-C to quit")
    while hasNotSeenFace:
        if face and face.is_visible:
            robot.set_all_backpack_lights(cozmo.lights.blue_light)
            hasNotSeenFace = False
            robot.say_text("Soyboy Detected").wait_for_completed()
        else:
            robot.set_backpack_lights_off()

            # Wait until we we can see another face
            try:
                face = robot.world.wait_for_observed_face(timeout=30)
            except asyncio.TimeoutError:
                print("Didn't find a face.")
                return

        time.sleep(.1)

def cozmo_move_around (robot: cozmo.robot.Robot):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed()

    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
    robot.turn_in_place(degrees(180)).wait_for_completed()

    robot.drive_straight(distance_mm(100), speed_mmps(50)).wait_for_completed();

def show_pokemon_pic (robot: cozmo.robot.Robot):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    #Formule ETS is cool
    # resize to fit on Cozmo's face screen
    imagePokemon = os.path.join(current_directory, "Pokemon.png")
    #imagePokemon = os.path.join(current_directory, "cozmosdk.png")
    resized_image = Image.open(imagePokemon).resize(cozmo.oled_face.dimensions(), Image.BICUBIC)

    # convert the image to the format used by the oled screen
    face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,
                                                                invert_image=True)
    robot.display_oled_face_image(face_image, 10000).wait_for_completed()

def cozmo_jam_out (robot: cozmo.robot.Robot):
    notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Half)
        ]
    robot.play_song(notes, loop_count=1).wait_for_completed();
    
def cozmo_cube_action(robot: cozmo.robot.Robot, index: int):
    time.sleep(5)
    if(index == 1):
        robot.world.get_light_cube(cozmo.objects.LightCube1Id).set_lights(cozmo.lights.green_light.flash())
        robot.run_timed_behavior(cozmo.behavior.BehaviorTypes.StackBlocks, active_time=60)
    if(index == 2):
        robot.world.get_light_cube(cozmo.objects.LightCube1Id).set_lights(cozmo.lights.green_light.flash())
        robot.run_timed_behavior(cozmo.behavior.BehaviorTypes.KnockOverCubes, active_time=60)
    
def cozmo_pickup_nearby_cube(robot: cozmo.robot.Robot):
    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    # try to find a block
    cube = None

    try:
        cube = robot.world.wait_for_observed_light_cube(timeout=30)
        print("Found cube", cube)

    except asyncio.TimeoutError:
        print("Didn't find a cube :-(")

    finally:
        # whether we find it or not, we want to stop the behavior
        look_around.stop()

    if cube is None:
        robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail)
        return

    print("Yay, found cube")

    cube.set_lights(cozmo.lights.green_light.flash())

    anim = robot.play_anim_trigger(cozmo.anim.Triggers.BlockReact)
    anim.wait_for_completed()


    action = robot.pickup_object(cube)
    print("got action", action)
    result = action.wait_for_completed(timeout=30)
    print("got action result", result)

    robot.turn_in_place(degrees(90)).wait_for_completed()

    action = robot.place_object_on_ground_here(cube)
    print("got action", action)
    result = action.wait_for_completed(timeout=30)
    print("got action result", result)

    anim = robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin)
    cube.set_light_corners(None, None, None, None)
    anim.wait_for_completed()

def create_walls(robot: cozmo.robot.Robot):

    #Horizontal
    wall1 = Pose(-400,400,0, angle_z=degrees(0))
    wall1 = robot.world.create_custom_fixed_object(wall1, 10, 400, 50, relative_to_robot=False)
    wall2 = Pose(-200,400,0, angle_z=degrees(0))
    wall2 = robot.world.create_custom_fixed_object(wall2, 10, 400, 50, relative_to_robot=False)
    wall3 = Pose(100,400,0, angle_z=degrees(0))
    wall3 = robot.world.create_custom_fixed_object(wall3, 10, 400, 50, relative_to_robot=False)
    wall4 = Pose(400,400,0, angle_z=degrees(0))
    wall4 = robot.world.create_custom_fixed_object(wall4, 10, 400, 50, relative_to_robot=False)
    wall5 = Pose(-200,0,0, angle_z=degrees(0))
    wall5 = robot.world.create_custom_fixed_object(wall5, 10, 250, 50, relative_to_robot=False)
    wall6 = Pose(100,0,0, angle_z=degrees(0))
    wall6 = robot.world.create_custom_fixed_object(wall6, 10, 300, 50, relative_to_robot=False)
    
    #vertical
    wall7 = Pose(-400,800,0, angle_z=degrees(0))
    wall7 = robot.world.create_custom_fixed_object(wall7, 10, 800, 50, relative_to_robot=False)
    wall8 = Pose(-350,0,0, angle_z=degrees(0))
    wall8 = robot.world.create_custom_fixed_object(wall8, 10, 750, 50, relative_to_robot=False)
    

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)