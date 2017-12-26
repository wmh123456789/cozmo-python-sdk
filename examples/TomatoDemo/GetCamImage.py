# The Demo to test the Cozmo's camera image

import asyncio
import time
import os

import cozmo

# BUFF_PATH = "/home/wmh/work/seqbuff/"
BUFF_PATH = "/Users/wty/work/TestSeq/MoveOnMat1/"

BUFF_LENGTH = 10000
last_image = None

def loop(robot: cozmo.robot.Robot):
    inc = 1
    HeadAngle = -15

    robot.set_lift_height(50.0).wait_for_completed()
    # MIN_HEAD_ANGLE = util.degrees(-25)
    robot.set_head_angle(cozmo.util.degrees(HeadAngle)).wait_for_completed()
    # robot.set_head_angle(cozmo.robot.MIN_HEAD_ANGLE).wait_for_completed()

    # initialize csv log file
    csvfp = open(BUFF_PATH+'RobotState.csv','w')
    csvfp.write('Time, HeadAngle')
    csvfp.write('PosX, PosY, PosZ,')
    csvfp.write('RotQ0, RotQ2, RotQ3, RotQ4,')
    csvfp.write('AngleZ, OriginID,')
    csvfp.write('AccX, AccY, AccZ,')
    csvfp.write('GyroX, GyroY, GyroZ\n')

    while inc < BUFF_LENGTH :
        timestamp = str('%.4f' % time.time())
        # im = capture_pic(robot).raw_image
        # # timestamp = str(time.strftime("%H%M%S"))+"_"+str(time.time())

        # print("Get image No." + str(inc)+", in size:"+str(im.size))
        # # im.save(str('%.4f'%time.time())+'.png','png')
        # # im.save(BUFF_PATH + str(inc) + '.png','png')
        # im.save(BUFF_PATH + str(inc) + '.jpg')
        #
        # #Write timestamp and robot state to file
        # fp = open(BUFF_PATH+str(inc)+'.txt','w')

        # fp.write(timestamp)
        # fp.close()

        # GetRobotState(robot,timestamp,csvfp)
        pose = robot.pose
        csvfp.write(timestamp +',' + str(HeadAngle) + ',')
        csvfp.write('%.1f, %.1f, %.1f,' % pose.position.x_y_z)
        csvfp.write('%.1f, %.1f, %.1f, %.1f,' % pose.rotation.q0_q1_q2_q3)
        csvfp.write('%.1f,' % pose.rotation.angle_z.degrees)
        csvfp.write('%s,' % pose.origin_id)

        csvfp.write('%.1f, %.1f, %.1f,' % robot.accelerometer.x_y_z)
        csvfp.write('%.1f, %.1f, %.1f,' % robot.gyro.x_y_z)
        csvfp.write('\n')

        inc += 1
        print(inc)
        time.sleep(0.19)
    csvfp.close()

def GetRobotState(robot:cozmo.robot.Robot):

    # Display the Pose info for the robot
    pose = robot.pose
    print('Pose: Pos = <%.1f, %.1f, %.1f>' % pose.position.x_y_z)
    print('Pose: Rot quat = <%.1f, %.1f, %.1f, %.1f>' % pose.rotation.q0_q1_q2_q3)
    print('Pose: angle_z = %.1f' % pose.rotation.angle_z.degrees)
    print('Pose: origin_id: %s' % pose.origin_id)

    # Display the Accelerometer and Gyro data for the robot
    print('Accelmtr: <%.1f, %.1f, %.1f>' % robot.accelerometer.x_y_z)
    print('Gyro: <%.1f, %.1f, %.1f>' % robot.gyro.x_y_z)



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
