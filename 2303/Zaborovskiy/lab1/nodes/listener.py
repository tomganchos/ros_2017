#!/usr/bin/env python
from __future__ import print_function
import rospy
from std_msgs.msg import String

import os
import sys
clear = lambda: os.system('clear')

level = [
    1, 1, 1, 1, 1,
    1, 0, 0, 2, 1,
    1, 0, 1, 0, 1,
    1, 0, 0, 0, 1,
    1, 1, 1, 1, 1
]

size = 5

ux = 1
uy = 1


def draw_maze():
    clear()
    y = 0

    while y < size:
        x = 0
        line = ""
        while x < size:
            if x == ux and y == uy:
                line = line + '@'
                if level[y * size + x] == 2:
                    print ("WIN!")
                    print ("WIN!")
                    print ("WIN!")
                    print ("WIN!")
            elif level[y * size + x] == 1:
                line = line + '#'
            elif level[y * size + x] == 2:
                line = line + 'F'
            else:
                line = line + ' '
            x=x+1
        print (line)
        y=y+1



def callback(data):
    msg = data.data
    if msg == "up":
        if level[(uy+1) * size + ux] == 0:
            uy=uy+1
    elif msg == "down":
        if level[(uy-1) * size + ux] == 0:
            ux=ux-1
    elif msg == "left":
        if level[(uy * size) + (ux-1)] == 0:
            ux=ux-1
    elif msg == "right":
        if level[(uy * size) + (ux+1)] == 0:
            ux=ux+1

    rospy.loginfo(rospy.get_name()+"Go to %s",data.data)
    draw_maze()

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()