#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math

def talker():
    pub = rospy.Publisher('/MYROBOT/joint1_position_controller/command',Float64, queue_size=10)
    pub1 = rospy.Publisher('/MYROBOT/joint2_position_controller/command',Float64, queue_size=10)
    pub2 = rospy.Publisher('/MYROBOT/joint3_position_controller/command',Float64, queue_size=10)
    pub3 = rospy.Publisher('/MYROBOT/joint4_position_controller/command',Float64, queue_size=10)
    # pub4= rospy.Publisher('/MYROBOT/joint5_position_controller/command',Float64, queue_size=10)
    # pub5 = rospy.Publisher('/MYROBOT/joint6_position_controller/command',Float64, queue_size=10)
    rospy.init_node('rr_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i=0
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        position = math.sin(i)
        rospy.loginfo(position)
        pub.publish(position)
        pub1.publish(position)
        pub2.publish(position)
        pub3.publish(position)
        # pub4.publish(position)
        # pub5.publish(position)
        rate.sleep()
        i +=0.1
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
