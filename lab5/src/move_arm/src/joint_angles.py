import rospy
from move_arm.msg import Coords

import numpy as np
import cv2
import mediapipe as mp
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
import tf


class ObjectDetector:
    def __init__(self):
        rospy.init_node('object_detector', anonymous=True)

        self.bridge = CvBridge()

        self.cv_color_image = None
        self.cv_depth_image = None

        self.color_image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.color_image_callback)

        self.fx = None
        self.fy = None
        self.cx = None
        self.cy = None

        self.camera_info_sub = rospy.Subscriber("/camera/color/camera_info", CameraInfo, self.camera_info_callback)

        self.tf_listener = tf.TransformListener()  # Create a TransformListener object

        self.point_pub = rospy.Publisher("goal_point", Point, queue_size=10)
        self.image_pub = rospy.Publisher('detected_cup', Image, queue_size=10)

        rospy.spin()
if __name__ == '__main__':
    ObjectDetector()


# initialize variables
mp_hands = mp.solutions.hands

finger_edges = [[0, 1], [1, 2], [2, 3], [3, 4],
                [0, 5], [5, 6], [6, 7], [7, 8],
                [9, 10], [10, 11], [11, 12],
                [13, 14], [14, 15], [15, 16],
                [0, 17], [17, 18], [18, 19], [19, 20],
                [5, 9], [9, 13], [13, 17]]


palm_points = [0, 1, 5, 9, 13, 17]
finger_points = [[2, 3, 4], [6, 7, 8], [10, 11, 12], [14, 15, 16], [18, 19, 20]]
left_point = 5
right_point = 17



# webcam input
cv2.namedWindow("Joint Angles")
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
width = len(frame[0])
height = len(frame)
fps = 25

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, fps)



def get_landmarks(hand_landmarks):
    # get landmarks from hand landmarks
    landmarks = []
    for landmark in hand_landmarks.landmark:
        landmarks.append([int(landmark.x * width), int(landmark.y * height)])
            
    return landmarks

def draw_landmarks(frame, landmarks, color, thickness):
    for landmark in landmarks:
        cv2.circle(frame, landmark, thickness, color, cv2.FILLED)

def draw_lines(frame, landmarks, color, thickness):
    for index1, index2 in finger_edges:
        cv2.line(frame, landmarks[index1], landmarks[index2], color, thickness)

def calculate_palm_pose(landmarks):
    return np.round(np.average([landmarks[point] for point in palm_points], axis=0)).astype(int)

def calculate_finger_pose(landmarks):
    finger_positions = []
    for finger in finger_points:
        finger_positions.append(np.round(np.average([landmarks[point] for point in finger], axis=0)).astype(int))
    return finger_positions

def calculate_hand_width(landmarks):
    left = np.round(landmarks[left_point]).astype(int)
    right = np.round(landmarks[right_point]).astype(int)
    return np.linalg.norm(left - right)

def calculate_hand_angle(landmarks):
    left = np.round(landmarks[left_point]).astype(int)
    right = np.round(landmarks[right_point]).astype(int)
    return -np.arctan2(right[1] - left[1], right[0] - left[0])

def talker():
    pub = rospy.Publisher('user_messages', Coords, queue_size=10)
    r = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1) as hands:
            while cap.isOpened():
                # get frame
                ret, frame = cap.read()
                if not ret: break

                # get hands
                results = hands.process(frame)

                if results.multi_hand_landmarks:
                    # get hand landmarks from multi hand landmarks
                    for hand_landmarks in results.multi_hand_landmarks:
                        landmarks = get_landmarks(hand_landmarks)

                        draw_lines(frame, landmarks, color=(0, 0, 255), thickness=3)

                        palm_position = calculate_palm_pose(landmarks)
                        draw_landmarks(frame, [palm_position], color=(0, 255, 0), thickness=5)

                        finger_positions = calculate_finger_pose(landmarks)
                        draw_landmarks(frame, finger_positions, color=(255, 0, 0), thickness=5)

                        hand_width = calculate_hand_width(landmarks)
                        hand_angle = calculate_hand_angle(landmarks)
                        print([np.linalg.norm(finger_position - palm_position) / hand_width for finger_position in finger_positions])

                        coords = Coords()
                        coords.y = palm_position[0]
                        coords.z = palm_position[1]
                        coords.theta = hand_angle
                        pub.publish(coords)

                # show frame
                cv2.imshow("Joint Angles", frame)
                if cv2.waitKey(1) == ord('q'):
                    break

                r.sleep()

cap.release()
cv2.destroyAllWindows()

# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('talker', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    try:
        talker()
    except rospy.ROSInterruptException: pass
