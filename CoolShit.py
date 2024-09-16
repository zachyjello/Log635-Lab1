import cozmo
import os
import sys
try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

def cozmo_program(robot: cozmo.robot.Robot):    
    robot.play_anim_trigger(cozmo.anim.Triggers.FrustratedByFailure).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.PetDetectionCat).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.PetDetectionDog).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.Surprise).wait_for_completed()
    
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
    
def comzo_takePicture(robot: cozmo.robot.Robot):
    robot.set_head_angle(angle=10.0).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()

cozmo.run_program(cozmo_program)