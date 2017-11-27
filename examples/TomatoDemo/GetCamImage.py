# The Demo to test the Cozmo's camera image

import asyncio
import time

import cozmo


last_image = None

def loop(robot: cozmo.robot.Robot):
    inc = 1

    robot.set_lift_height(50.0).wait_for_completed()
    robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()
    while True:
            im = capture_pic(robot).raw_image
            # timestamp = str(time.strftime("%H%M%S"))+"_"+str(time.time())
            print("Increment " + str(inc)+":"+str(im.size))
            im.save(str('%.4f'%time.time())+'.png','png')
            inc += 1
            time.sleep(0.15)

def capture_pic(robot: cozmo.robot.Robot):
    robot.camera.image_stream_enabled = True
    print("Waiting for a picture...")
    # wait for a new camera image to ensure it is captured properly
    global last_image
    image = robot.world.latest_image
    while image == last_image:
            time.sleep(0.02)
            image = robot.world.latest_image
    last_image = image
    return last_image

if __name__ == '__main__':
    cozmo.run_program(loop, use_viewer=True)
