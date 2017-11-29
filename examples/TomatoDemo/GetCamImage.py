# The Demo to test the Cozmo's camera image

import asyncio
import time
import os

import cozmo

BUFF_PATH = "/home/wmh/work/seqbuff/"
BUFF_LENGTH = 10000
last_image = None

def loop(robot: cozmo.robot.Robot):
    inc = 1

    robot.set_lift_height(50.0).wait_for_completed()
    # MIN_HEAD_ANGLE = util.degrees(-25)
    robot.set_head_angle(cozmo.util.degrees(15)).wait_for_completed()
    # robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()
    while inc < BUFF_LENGTH :
            im = capture_pic(robot).raw_image
            # timestamp = str(time.strftime("%H%M%S"))+"_"+str(time.time())
            # timestamp = str('%.4f' % time.time())
            print("Increment " + str(inc)+":"+str(im.size))
            # im.save(str('%.4f'%time.time())+'.png','png')
            im.save(BUFF_PATH + str(inc) + '.png','png')
            # im.save(BUFF_PATH + str(inc) + '.jpg')
            fp = open(BUFF_PATH+str(inc)+'.txt','w')
            fp.write(str('%.4f' % time.time()))
            fp.close()
            inc += 1


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
