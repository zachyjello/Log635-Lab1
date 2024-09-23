import time
from time import strftime
import os
import cozmo
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject
from cozmo.util import Pose, degrees

alreadyDoneImages = []
liveCamera = False
fullPath = "photos"

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

def on_new_camera_image(evt, **kwargs):    
    global liveCamera
    global fullPath
    if liveCamera:
        print("Cozmo is taking a photo")
        pilImage = kwargs['image'].raw_image
        #TODO: Modify path to increment photo_01, photo_02, ...
        pilImage.save(fullPath, "JPEG")

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
    print("I do action 1")
    robot.say_text("My name is Jeff").wait_for_completed()

#EMOTION
def action_for_marker_1(robot: cozmo.robot.Robot):
    print("I do action 2")
    robot.play_anim_trigger(cozmo.anim.Triggers.Surprise).wait_for_completed()

#STACK CUBES
def action_for_marker_2(robot: cozmo.robot.Robot):
    print("I do action 3")


def action_for_marker_3(robot: cozmo.robot.Robot):
    #Fart sound
    nothing = True

def action_for_marker_4(robot: cozmo.robot.Robot):
    #FBI Open Up
    nothing = True

def action_for_marker_5(robot: cozmo.robot.Robot):
    #No
    nothing = True

def action_for_marker_6(robot: cozmo.robot.Robot):
    #Amogus
    nothing = True

def action_for_marker_7(robot: cozmo.robot.Robot):
    #gas gas gas
    nothing = True

def action_for_marker_8(robot: cozmo.robot.Robot):
    #I'm a magic unicorn
    nothing = True

def action_for_marker_9(robot: cozmo.robot.Robot):
    #I'm tired
    nothing = True

def action_for_marker_10(robot: cozmo.robot.Robot):
    #Do you think it will work
    nothing = True

def action_for_marker_11(robot: cozmo.robot.Robot):
    #I doubt, but I try
    nothing = True

def action_for_marker_12(robot: cozmo.robot.Robot):
    #I don't have any inspi
    nothing = True

def action_for_marker_13(robot: cozmo.robot.Robot):
    #Formule ETS is cool
    nothing = True

def action_for_marker_14(robot: cozmo.robot.Robot):
    #Piranha too
    nothing = True

def action_for_marker_15(robot: cozmo.robot.Robot):
    #Enfin
    nothing = True

def cozmo_program(robot: cozmo.robot.Robot):
    createAllDirectories()
    # Gestionnaires d'évennements à chaque fois que Cozmo vois un objet
    #robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    # Chaque fois que Cozmo voit une "nouvelle" image, prends une photo
    robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)

    #Création des objets customs
    robot.world.define_custom_wall(CustomObjectTypes.CustomType00,
                                   CustomObjectMarkers.Triangles2,
                                   50, 50, 10, 10, True)
    robot.world.define_custom_wall(CustomObjectTypes.CustomType01,
                                   CustomObjectMarkers.Circles2,
                                   50, 50, 10, 10, True)
    #TODO: Create you custom object

    
    while len(alreadyDoneImages) < 16:
        # Chercher les objets
        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        object_found = robot.world.wait_until_observe_num_objects(num=1, timeout=60) #LOOK TIMEOUTS
        lookaround.stop()

        for obj in object_found:
            # Vérifiez si l'objet est un marqueur que vous surveillez
            if obj.object_type not in alreadyDoneImages:
                if obj.object_type == CustomObjectTypes.CustomType00:
                    TakePhoto(robot, "photos/Triangles/Triangle2/photo_01.jpg") #TODO: For each picture make sure you're in front, so hardcode some position
                    action_for_marker_0(robot)
                    alreadyDoneImages.append(CustomObjectTypes.CustomType00)
                if obj.object_type == CustomObjectTypes.CustomType01:
                    TakePhoto(robot, "photos/Circles/Circle2/photo_01.jpg")
                    action_for_marker_1(robot)
                    alreadyDoneImages.append(CustomObjectTypes.CustomType01)
                #TODO: ADD your step here

    while True:
        time.sleep(0.1)

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)