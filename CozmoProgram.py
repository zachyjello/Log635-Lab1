import time
from time import strftime
import os
import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject
from cozmo.util import Pose, degrees

current_step = 0
liveCamera = False
fullPath = "photos"

def on_new_camera_image(evt, **kwargs):    
    global liveCamera
    global fullPath
    if liveCamera:
        print("Cozmo is taking a photo")
        pilImage = kwargs['image'].raw_image
        global directory
        pilImage.save(fullPath, "JPG")

def TakePhoto(robot: cozmo.robot.Robot, path):
    global liveCamera
    global fullPath
    fullPath = path
    # Assurez-vous que la tête et le bras de Cozmo sont à un niveau raisonnable
    robot.set_head_angle(degrees(10.0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()

    liveCamera = True
    time.sleep(0.1)    
    liveCamera = False

def action_for_marker_0(robot: cozmo.robot.Robot):
    ...

def action_for_marker_1(robot: cozmo.robot.Robot):
    ...

def action_for_marker_2(robot: cozmo.robot.Robot):
    ...

def action_for_marker_3(robot: cozmo.robot.Robot):
    ...

def action_for_marker_4(robot: cozmo.robot.Robot):
    ...

def action_for_marker_5(robot: cozmo.robot.Robot):
    ...

def action_for_marker_6(robot: cozmo.robot.Robot):
    ...

def action_for_marker_7(robot: cozmo.robot.Robot):
    ...

def action_for_marker_8(robot: cozmo.robot.Robot):
    ...

def action_for_marker_9(robot: cozmo.robot.Robot):
    ...

def action_for_marker_10(robot: cozmo.robot.Robot):
    ...

def action_for_marker_11(robot: cozmo.robot.Robot):
    ...

def action_for_marker_12(robot: cozmo.robot.Robot):
    ...

def action_for_marker_13(robot: cozmo.robot.Robot):
    ...

def action_for_marker_14(robot: cozmo.robot.Robot):
    ...

def action_for_marker_15(robot: cozmo.robot.Robot):
    ...


def handle_object_appeared(evt, **kw):
    # Cela sera appelé chaque fois qu'un EvtObjectAppeared est déclanché
    # chaque fois qu'un objet entre en vue
    if isinstance(evt.obj, CustomObject):
        print(f"Cozmo started seeing a type: {str(evt.obj.object_type)} id: {str(evt.obj.object_id)}")



def cozmo_program(robot: cozmo.robot.Robot):
    global current_step
    # Gestionnaires d'évennements à chaque fois que Cozmo vois un objet
    #robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    # Chaque fois que Cozmo voit une "nouvelle" image, prends une photo
    robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)

    # Indiquer le dossier pour stocker les photos
    global directory    
    directory = f"{strftime('%y%m%d')}"
    if not os.path.exists('photos'):
        os.makedirs('photos')
    if not os.path.exists('photos/Triangles'):
        os.makedirs('photos/Triangles')
    if not os.path.exists('photos/Hexagons'):
        os.makedirs('photos/Hexagons')
    if not os.path.exists('photos/Diamonds'):
        os.makedirs('photos/Diamonds')
    if not os.path.exists('photos/Circles'):
        os.makedirs('photos/Circles')


    # Chercer les objest
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    object_found = robot.world.wait_until_observe_num_objects(num=16, timeout=60)
    lookaround.stop()

    #TODO: LOOK AT THE OBJECT BEFORE DOING THE ACTION?
    if len(object_found) > 0:
        while current_step is not 16:
            for object in object_found:
                if current_step == 0 and object.marker_type == CustomObjectMarkers.Triangles2:
                    TakePhoto(robot, "photos/Triangles/Triangle2/photo_01.jpg")
                    action_for_marker_0(robot)
                    current_step += 1
                elif current_step == 1 and object.marker_type == CustomObjectMarkers.Hexagons3:
                    TakePhoto(robot, "photos/Hexagons/Hexagon3/photo_01.jpg")
                    action_for_marker_1(robot)
                    current_step += 1
                elif current_step == 2 and object.marker_type == CustomObjectMarkers.Circles5:
                    TakePhoto(robot, "photos/Circles/Circle5/photo_01.jpg")
                    action_for_marker_2(robot)
                    current_step += 1
                elif current_step == 3 and object.marker_type == CustomObjectMarkers.Diamonds4:
                    TakePhoto(robot, "photos/Diamonds/Diamond4/photo_01.jpg")
                    action_for_marker_3(robot)
                    current_step += 1
                elif current_step == 4 and object.marker_type == CustomObjectMarkers.Triangles4:
                    TakePhoto(robot, "photos/Triangles/Triangle4/photo_01.jpg")
                    action_for_marker_4(robot)
                    current_step += 1
                elif current_step == 5 and object.marker_type == CustomObjectMarkers.Diamonds5:
                    TakePhoto(robot, "photos/Diamonds/Diamond2/photo_01.jpg")
                    action_for_marker_5(robot)
                    current_step += 1
                elif current_step == 6 and object.marker_type == CustomObjectMarkers.Circles2:
                    TakePhoto(robot, "photos/Circles/Circle2/photo_01.jpg")
                    action_for_marker_6(robot)
                    current_step += 1
                elif current_step == 7 and object.marker_type == CustomObjectMarkers.Hexagons2:
                    TakePhoto(robot, "photos/Hexagons/Hexagon2/photo_01.jpg")
                    action_for_marker_7(robot)
                    current_step += 1
                elif current_step == 8 and object.marker_type == CustomObjectMarkers.Diamonds2:
                    TakePhoto(robot, "photos/Diamonds/Diamond2/photo_01.jpg")
                    action_for_marker_8(robot)
                    current_step += 1
                elif current_step == 9 and object.marker_type == CustomObjectMarkers.Circles4:
                    TakePhoto(robot, "photos/Circles/Circle4/photo_01.jpg")
                    action_for_marker_9(robot)
                    current_step += 1
                elif current_step == 10 and object.marker_type == CustomObjectMarkers.Hexagons4:
                    TakePhoto(robot, "photos/Hexagons/Hexagon4/photo_01.jpg")
                    action_for_marker_10(robot)
                    current_step += 1
                elif current_step == 11 and object.marker_type == CustomObjectMarkers.Triangles3:
                    TakePhoto(robot, "photos/Triangles/Triangle3/photo_01.jpg")
                    action_for_marker_11(robot)
                    current_step += 1
                elif current_step == 12 and object.marker_type == CustomObjectMarkers.Triangles5:
                    TakePhoto(robot, "photos/Triangles/Triangle5/photo_01.jpg")
                    action_for_marker_12(robot)
                    current_step += 1
                elif current_step == 13 and object.marker_type == CustomObjectMarkers.Diamonds3:
                    TakePhoto(robot, "photos/Diamonds/Diamond3/photo_01.jpg")
                    action_for_marker_13(robot)
                    current_step += 1
                elif current_step == 14 and object.marker_type == CustomObjectMarkers.Circles3:
                    TakePhoto(robot, "photos/Circles/Circle3/photo_01.jpg")
                    action_for_marker_14(robot)
                    current_step += 1
                elif current_step == 15 and object.marker_type == CustomObjectMarkers.Hexagons5:
                    TakePhoto(robot, "photos/Hexagons/Hexagon5/photo_01.jpg")
                    action_for_marker_15(robot)
                    current_step += 1
    else:
        print("PANIC Button, AUTO-DESTRUCTION IMMINENTE")

    while True:
        time.sleep(0.1)

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)