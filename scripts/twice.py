#!/usr/bin/env python3

#NODE_AUTHOR("Ryuichi Ueda");
#NODE_LICENSE("BSD");

import rospy
from std_msgs.msg import Int32

def cb(message):
    rospy.loginfo(message.data*2)

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
rospy.spin()
