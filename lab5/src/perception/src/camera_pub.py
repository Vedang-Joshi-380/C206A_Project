# Derived from: https://automaticaddison.com/working-with-ros-and-opencv-in-ros-noetic/

import rospy 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 
  
def publish_message():
 
  pub = rospy.Publisher('webcam', Image, queue_size=10)
     
  # Tells rospy the name of the node.
  # Anonymous = True makes sure the node has a unique name. Random
  # numbers are added to the end of the name.
  rospy.init_node('video_pub_py', anonymous=True)
     
  
  rate = rospy.Rate(10) # 10hz
     

  cap = cv2.VideoCapture(0)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 848)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  cap.set(cv2.CAP_PROP_FPS, 25)
     
  # Used to convert between ROS and OpenCV images
  br = CvBridge()
 
  # While ROS is still running.
  while not rospy.is_shutdown():
     
      
      ret, frame = cap.read()
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      if ret == True:
        pub.publish(br.cv2_to_imgmsg(frame))
             
      # Sleep just enough to maintain the desired rate
      rate.sleep()
         
if __name__ == '__main__':
  try:
    publish_message()
  except rospy.ROSInterruptException:
    pass