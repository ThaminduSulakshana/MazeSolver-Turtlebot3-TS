
import rospy
from geometry_msgs.msg import Twist

class TrajectoryFollower:
    def _init_(self, path_id):
        rospy.init_node('trajectory_follower', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.twist = Twist()
        self.path_id = path_id

    def follow_path(self):
        if self.path_id == 1:
            self.execute_path_1()
        elif self.path_id == 2:
            self.execute_path_2()
        elif self.path_id == 3:
            self.execute_path_3()
        else:
            rospy.logerr("Invalid path ID")

    def execute_path_1(self):
        rospy.loginfo("Executing Path 1...")
        self.move_forward(2)
        self.turn(90)
        self.move_forward(1)

    def execute_path_2(self):
        rospy.loginfo("Executing Path 2...")
        self.move_forward(3)
        self.turn(-45)
        self.move_forward(2)

    def execute_path_3(self):
        rospy.loginfo("Executing Path 3...")
        self.move_forward(1)
        self.turn(135)
        self.move_forward(1.5)

    def move_forward(self, duration):
        self.twist.linear.x = 0.2
        self.twist.angular.z = 0.0
        self.publish_command(duration)

    def turn(self, angle):
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.5 if angle > 0 else -0.5
        self.publish_command(abs(angle) / 45)  # Adjust duration based on angle

    def publish_command(self, duration):
        rate = rospy.Rate(10)
        for _ in range(int(duration * 10)):
            self.cmd_vel_pub.publish(self.twist)
            rate.sleep()

if _name_ == '_main_':
    path_id = int(input("Enter Path ID (1, 2, or 3): "))
    follower = TrajectoryFollower(path_id)
    follower.follow_path()
