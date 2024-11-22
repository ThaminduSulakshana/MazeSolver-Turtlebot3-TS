#!/usr/bin/env python
from sensor_msgs.msg import LaserScan

front = 0
f_left = 0
left = 0
right = 0
f_right = 0

def scan_callback(msg):
    global front, f_left, left, right, f_right
    front = min(min(msg.ranges[0:5]), min(msg.ranges[355:]))
    f_left = min(msg.ranges[14:60])
    left = min(msg.ranges[74:105])
    right = min(msg.ranges[268:271])
    f_right = min(msg.ranges[299:345])
