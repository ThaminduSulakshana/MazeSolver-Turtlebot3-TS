import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class MazeSolver:
    def _init_(self):
        rospy.init_node('maze_solver', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.laser_sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        self.twist = Twist()
        self.obstacle_distance = 1.0  # Threshold distance to avoid obstacles

    def laser_callback(self, data):
        # Check for obstacles in the front
        front_range = min(min(data.ranges[:30]), min(data.ranges[-30:]))
        if front_range < self.obstacle_distance:
            self.avoid_obstacle()
        else:
            self.move_forward()

    def move_forward(self):
        self.twist.linear.x = 0.2
        self.twist.angular.z = 0.0
        self.cmd_vel_pub.publish(self.twist)

    def avoid_obstacle(self):
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.5  # Turn right
        self.cmd_vel_pub.publish(self.twist)

    def run(self):
        rospy.spin()

if _name_ == '_main_':
    maze_solver = MazeSolver()
    maze_solver.run()
