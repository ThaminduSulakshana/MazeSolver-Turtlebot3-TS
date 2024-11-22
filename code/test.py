#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist, Point
from navigation_utils import normalize_angle, stop_robot
from odom_handler import odom_callback, robot_pos, robot_yaw
from scan_handler import scan_callback, front, f_left, left, right, f_right

# Global variables
cmd_pub = None
state = 0
section = 0
door1 = 0
door2 = 0

# Target positions
des_pos1 = Point(3, 3.5, 0)
des_pos2 = Point(3.0, 4.3, 0)
des_pos3 = Point(2.75, 5.5, 0)
des_pos4 = Point(3.25, 5.5, 0)

def fix_yaw(des_pos):
    global robot_yaw, cmd_pub, state
    destination_yaw = math.atan2(des_pos.y - robot_pos.y, des_pos.x - robot_pos.x)
    err_yaw = normalize_angle(destination_yaw - robot_yaw)
    command = Twist()
    if math.fabs(err_yaw) > YAW_PREC:
        command.angular.z = 0.3 if err_yaw > 0 else -0.3
    cmd_pub.publish(command)
    if math.fabs(err_yaw) <= YAW_PREC:
        state = 1

def go_to_position(des_pos):
    global robot_yaw, cmd_pub, state
    err_pos = math.sqrt(pow(des_pos.y - robot_pos.y, 2) + pow(des_pos.x - robot_pos.x, 2))
    if err_pos > DIST_PRE:
        command = Twist()
        command.linear.x = 0.2
        cmd_pub.publish(command)
    else:
        state = 2

def main():
    global cmd_pub, state, section, door1, door2

    rospy.init_node('maze_navigation')
    cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('/scan', LaserScan, scan_callback)
    rospy.Subscriber('/odom', Odometry, odom_callback)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # Control logic
        if section == 1:
            if state == 0:
                fix_yaw(des_pos1)
            elif state == 1:
                go_to_position(des_pos1)
            else:
                section = 2
                state = 0

        # Add further section handling logic here
        rate.sleep()

if __name__ == '__main__':
    main()
