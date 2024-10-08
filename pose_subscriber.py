#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def pose_callback(msg):
    rospy.loginfo(msg)


if __name__ == '__main__':
    rospy.init_node("turtle_pose_subscriber")  #initialize node
    #you can choose different name for node and executable
    #here node name is "turtle_pose_subscriber" and executable name is pose_subscriber

    sub = rospy.Subscriber("/turtle1/pose",Pose,callback=pose_callback)
    #here we used pose_callback function

    rospy.loginfo("Node has been started")
    rospy.spin()

