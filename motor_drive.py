#!/usr/bin/env python3
""" Drive wheel motors according to topic /cmd_vel."""

import rospy
from geometry_msgs.msg import Twist

cmd_vel_x = 0.0  # X velocity (meters/sec)
cmd_vel_theta_z = 0.0  # theta Z velocity (radians/sec)

def listener():
    """Listen to cmd_vel topic. Send Twist msg to callback."""
    rospy.Subscriber("/cmd_vel", Twist, listener_callback)

def listener_callback(msg):
    """Extract linear.x and angular.z from Twist msg."""
    global cmd_vel_x, cmd_vel_theta_z
    cmd_vel_x = msg.linear.x  # meters/sec
    cmd_vel_theta_z = msg.angular.z  # radians/sec

def set_mtr_spd():
    """Drive motors according to command velocity."""
    pass

if __name__ == '__main__':

    rospy.init_node('motor_drive', anonymous=True)
    listener()
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        set_mtr_spd()
        rate.sleep()

