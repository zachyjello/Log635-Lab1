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
    

def cozmo_speak(robot: cozmo.robot.Robot):
    current_directory = os.path.dirname(os.path.realpath(__file__))    
    sdk_png = os.path.join(current_directory, "..", "Tutorial", "face_images", "cozmosdk.png")
    hello_png = os.path.join(current_directory, "..", "Tutorial", "face_images", "cozmosdk.png")
    
    image_settings = [(sdk_png, Image.BICUBIC),
                      (hello_png, Image.NEAREST)]
    face_images = []
    for image_name, resampling_mode in image_settings:
        image = Image.open(image_name)

        # resize to fit on Cozmo's face screen
        resized_image = image.resize(cozmo.oled_face.dimensions(), resampling_mode)

        # convert the image to the format used by the oled screen
        face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,
                                                                 invert_image=True)
        face_images.append(face_image)

cozmo.run_program(cozmo_program)