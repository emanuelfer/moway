import sys, atexit, msvcrt
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

if __name__ == '__main__':
 atexit.register(exit_mow)

channel = 7
moway.usbinit_moway()
ret = moway.init_moway(channel)

if ret == 0:
    print ('Moway RFUSB Connected')
else:
    print ('Moway RFUSB not connected. Exit')
    #exit(-1)

while moway.get_obs_center_left() < 20 and moway.get_obs_center_right() < 20:
    if(moway.get_line_left() > 50): #verifica se o moway ainda está na linha preta
        moway.set_distance(15)
        moway.set_speed(100)
        moway.command_moway(CMD_GO,0)
        moway.wait_mot_end(0)
    else: #verifica se chegou em uma bifurcação
        moway.set_distance(10)
        moway.set_speed(100)
        moway.command_moway(CMD_GO,0)
        moway.wait_mot_end(0)
        
        moway.set_rotation(90)
        moway.set_rotation_axis(CENTER)
        moway.command_moway(CMD_ROTATERIGHT,0)
        moway.wait_mot_end(0)

        if (moway.get_line_left() < 50):
            moway.set_rotation(90)
            moway.set_rotation_axis(CENTER)
            moway.command_moway(CMD_ROTATELEFT,0)
            moway.wait_mot_end(0)

            moway.set_distance(20)
            moway.set_speed(100)
            moway.command_moway(CMD_GO,0)
            moway.wait_mot_end(0)
            
        if (moway.get_line_left() < 50):
            moway.set_rotation(180)
            moway.set_rotation_axis(CENTER)
            moway.command_moway(CMD_ROTATELEFT,0)
            moway.wait_mot_end(0)

            moway.set_distance(20)
            moway.set_speed(100)
            moway.command_moway(CMD_GO,0)
            moway.wait_mot_end(0)
   

moway.command_moway(CMD_STOP, 0)
