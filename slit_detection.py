import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class SlitDetection:
    def _init_(self):
        rospy.init_node('slit_detection', anonymous=True)
        self.image_sub = rospy.Subscriber('/camera/image_raw', Image, self.image_callback)
        self.bridge = CvBridge()

    def image_callback(self, msg):
        # Convert ROS Image message to OpenCV image
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        
        # Detect gaps (slits) in the thresholded image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        slits_detected = sum(1 for c in contours if cv2.contourArea(c) > 100)
        rospy.loginfo(f"Slits detected: {slits_detected}")

        # Show the image (for debugging)
        cv2.imshow("Slit Detection", frame)
        cv2.waitKey(1)

if _name_ == '_main_':
    slit_detection = SlitDetection()
    rospy.spin()