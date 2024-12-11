import numpy as np
import cv2
import mediapipe as mp
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from move_arm.msg import Coords


bridge = CvBridge()

def image_callback(img_msg):
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
    except CvBridgeError as e:
        rospy.logerr("CvBridge Error: {0}".format(e))
    
    # Process the cv_image (e.g., display it)
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

    with mp_hands.Hands(min_detection_confidence=0.25, min_tracking_confidence=0.25, max_num_hands=1) as hands:
        frame = cv_image

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
                print(palm_position)
                print(hand_angle)

                # r = rospy.Rate(10)
                coords = Coords() 
                # Publish our string to the 'chatter_talk' topic
                coords.y = palm_position[0]
                coords.z = palm_position[1]
                coords.theta = hand_angle
                print("Y: \"%s\"" % coords.y + ", Z:  \"%s\"" % coords.z + ", theta:  \"%s\"" % coords.theta)
                pub.publish(coords)
                # Use our rate object to sleep until it is time to publish again
                # r.sleep()

    cv2.imshow("Image Window", cv_image)
    cv2.waitKey(3)  # Needed to display the image

image_topic = "/camera/color/image_raw" # Replace with your actual topic name
image_subscriber = rospy.Subscriber(image_topic, Image, image_callback)
pub = rospy.Publisher('user_messages', Coords, queue_size=10)

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


width = 424
height = 240


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



if __name__ == '__main__':
    rospy.init_node('image_listener', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()
