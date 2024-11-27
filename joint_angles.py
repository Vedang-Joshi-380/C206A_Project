import numpy as np
import cv2
import mediapipe as mp



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

                draw_landmarks(frame, landmarks, color=(255, 0, 0), thickness=5)

                draw_lines(frame, landmarks, color=(0, 0, 255), thickness=3)

                palm_position = calculate_palm_pose(landmarks)
                draw_landmarks(frame, [palm_position], color=(0, 255, 0), thickness=5)

                finger_positions = calculate_finger_pose(landmarks)
                draw_landmarks(frame, finger_positions, color=(0, 255, 0), thickness=5)

                hand_width = calculate_hand_width(landmarks)
                print([np.linalg.norm(finger_position - palm_position) / hand_width for finger_position in finger_positions])

        # show frame
        cv2.imshow("Joint Angles", frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
