#!/usr/bin/env python
import math
from geometry_msgs.msg import Twist, Point
from tf.transformations import euler_from_quaternion

# Constants
YAW_PREC = math.pi / 90
DIST_PRE = 0.3

# Utility functions
def normalize_angle(angle):
    if math.fabs(angle) > math.pi:
        angle = angle - (2 * math.pi * angle) / math.fabs(angle)
    return angle

def stop_robot(cmd_pub):
    command = Twist()
    command.linear.x = 0
    command.angular.z = 0
    cmd_pub.publish(command)
