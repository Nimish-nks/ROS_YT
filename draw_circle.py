#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__=='__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has been started.")

    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10) #name of topic, type of message and buffer size
#quesize is sort of buffer
    rate = rospy.Rate(2) #at this rate of 2 Hz it is sending message

    while not rospy.is_shutdown():
        
        rospy.loginfo("Publish cmd vel")
        #creating message to send
        msg = Twist()
        #by seeing rosmsg info you can know what exactly to send
        msg.linear.x = 2.0  # you don't need to fill every field
        msg.angular.z = 1.0
        pub.publish(msg)     #send the message to topic
        rate.sleep()
