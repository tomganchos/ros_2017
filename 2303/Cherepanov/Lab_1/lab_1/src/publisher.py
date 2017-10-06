#!/usr/bin/env python
import turtle
import rospy
import random
from std_msgs.msg import String

def generate_key():
    key = random.randint(1,6)
    if key == 1: return "Up"
    if key == 2: return "Down"
    if key == 3: return "Left"
    if key == 4: return "Right"
    if key == 5: return "Print"

def publisher():
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    pub = rospy.Publisher('chatter', String, queue_size=1000)

    while not rospy.is_shutdown():
        key = generate_key()
        rospy.loginfo("%s - Generate key %s" % (rospy.get_time(),key))
        pub.publish(key)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
