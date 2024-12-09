import time
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
cube_taps = [0]*3
def handle_object_tapped(evt, **kw):
    global keepGoing
    # This will be called whenever an EvtObjectMovingStarted event is dispatched -
    # whenever we detect a cube starts moving (via an accelerometer in the cube)
    i = evt.obj.object_id - 1
    cube_taps[i] = cube_taps[i] + evt.tap_count if cube_taps[i] < 3 else 0
    print(cube_taps)
    if all(x == 3 for x in cube_taps):
        keepGoing=False

def cozmo_program(robot: cozmo.robot.Robot):
    global keepGoing
    # Add event handlers that will be called for the corresponding event
    robot.add_event_handler(cozmo.objects.EvtObjectTapped, handle_object_tapped)
    robot.say_text("Light up cubes").wait_for_completed()
    # looks like a paperclip
    cube1 = robot.world.get_light_cube(LightCube1Id)
    # looks like a lamp / heart
    cube2 = robot.world.get_light_cube(LightCube2Id)
    # looks like the letters 'ab' over 'T'
    cube3 = robot.world.get_light_cube(LightCube3Id) 

    print(str(cube1) + "\n" + str(cube2) + "\n" + str(cube3))
    robot.say_text("waiting for tapped cube").wait_for_completed()
    keepGoing=True
    # keep the program running until user closes / quits it
    #print("Press CTRL-C to quit")
    while keepGoing:
        time.sleep(0.1)
    robot.say_text("cube Tapped").wait_for_completed()
cozmo.run_program(cozmo_program)