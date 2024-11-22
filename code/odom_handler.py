#!/usr/bin/env python
import math
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

robot_pos = None
robot_yaw = 0

def odom_callback(msg):
    global robot_pos, robot_yaw
    robot_pos = msg.pose.pose.position
    odom_ori = msg.pose.pose.orientation
    euler = euler_from_quaternion([odom_ori.x, odom_ori.y, odom_ori.z, odom_ori.w])
    robot_yaw = euler[2]
