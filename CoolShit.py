import cozmo
import os
import sys
import time
try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")
    
from PIL import Image, ImageTk

def cozmo_program(robot: cozmo.robot.Robot):
    #Necessary stuff for taking and saving pictures
    robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)   
    global directory    
    directory = f"{strftime('%y%m%d')}"
    if not os.path.exists('photos'):
        os.makedirs('photos')
    if not os.path.exists(f'photos/{directory}'):
        os.makedirs(f'photos/{directory}')
     
    robot.play_anim_trigger(cozmo.anim.Triggers.FrustratedByFailure).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.PetDetectionCat).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.PetDetectionDog).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.Surprise).wait_for_completed()
    
def on_new_camera_image(evt, **kwargs):    
    global liveCamera
    if liveCamera:
        print("Cozmo is taking a photo")
        pilImage = kwargs['image'].raw_image
        global directory
        pilImage.save(f"photos/{directory}/{directory}-{kwargs['image'].image_number}.jpeg", "JPEG")
        liveCamera = False
        
def take_photo(robot: cozmo.robot.Robot):
    global liveCamera    
    
    # Assurez-vous que la tête et le bras de Cozmo sont à un niveau raisonnable
    robot.set_head_angle(angle=10.0).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()
        
    liveCamera = True
    time.sleep(0.1)    
    liveCamera = False   
    
#Makes cozmo raise head, lower arms, and speak
def cozmo_speak(robot: cozmo.robot.Robot, textToSay):
    raise_head_action = robot.set_head_angle(angle=25)
    lift_action = robot.set_lift_height(0.0, in_parallel=True)
    robot.say_text(textToSay).wait_for_completed()

def cozmo_showImage(robot: cozmo.robot.Robot, imageName, duration):
    current_directory = os.path.dirname(os.path.realpath(__file__))    
    image_png = os.path.join(current_directory, "..", "Tutorial", "face_images", imageName + ".png")
        
    image_settings = (image_png, Image.BICUBIC)
    
    image = Image.open(image_png)
    resized_image = image.resize(cozmo.oled_face.dimensions(), Image.BICUBIC)
    face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,
                                                                 invert_image=True)
    robot.display_oled_face_image(face_image, duration * 1000.0)
    
def cozmo_findFaces(robot: cozmo.robot.Robot):
    
    findfaces= robot.start_behavior(cozmo.behavior.BehaviorTypes.FindFaces)    
    face = robot.world.wait_for_observed_face(timeout=None, include_existing=True)
    findfaces.stop()
    
    if face is not None:
        robot.say_text(f"{face.name}").wait_for_completed()
    
    while True:
        time.sleep(0.1)

cozmo.run_program(cozmo_program)