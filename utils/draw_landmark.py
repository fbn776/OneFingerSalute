import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np

from utils.is_middle_finger_shown import is_middle_finger_gesture
from utils.utils import compute_slope

MARGIN = 10
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54)

def draw_landmarks_on_image(rgb_image, detection_result):
    hand_landmarks_list = detection_result.hand_landmarks
    handedness_list = detection_result.handedness
    annotated_image = np.copy(rgb_image)

    # Loop through the detected hands to visualize.
    for idx in range(len(hand_landmarks_list)):
        hand_landmarks = hand_landmarks_list[idx]
        handedness = handedness_list[idx]

        # Draw the hand landmarks.
        hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
        ])
        solutions.drawing_utils.draw_landmarks(
            annotated_image,
            hand_landmarks_proto,
            solutions.hands.HAND_CONNECTIONS,
            solutions.drawing_styles.get_default_hand_landmarks_style(),
            solutions.drawing_styles.get_default_hand_connections_style())

        # Get the top left corner of the detected hand's bounding box.
        height, width, _ = annotated_image.shape
        x_coordinates = [landmark.x for landmark in hand_landmarks]
        y_coordinates = [landmark.y for landmark in hand_landmarks]

        coord = [(int(landmark.x * width), int(landmark.y * height)) for landmark in hand_landmarks]

        wrist = coord[0]
        finger_base = coord[9] # A
        finger_lower_mid = coord[10] # B
        finger_upper_mid = coord[11] # C
        finger_tip = coord[12] # D

        m_ad = compute_slope(finger_base, finger_tip)
        m_bc = compute_slope(finger_lower_mid, finger_upper_mid)

        is_in_line = abs(m_ad - m_bc) < 0.2 if m_ad != float('inf') and m_bc != float('inf') else m_ad == m_bc

        # print("Is in line:", is_in_line, "Mad =", m_ad, "Mbc =", m_bc, "diff =", abs(m_ad - m_bc))

        # Bounding box;
        x_min, x_max = min(x_coordinates), max(x_coordinates)
        y_min, y_max = min(y_coordinates), max(y_coordinates)

        cv2.rectangle(annotated_image,
                      (int(x_min * width), int(y_min * height)),
                      (int(x_max * width), int(y_max * height)),
                      (0, 255, 0), 2)

        text_x = int(min(x_coordinates) * width)
        text_y = int(min(y_coordinates) * height) - MARGIN



        middle_finger_detected = is_middle_finger_gesture(hand_landmarks, width, height)

        # Display result
        if middle_finger_detected:
            cv2.putText(annotated_image, "Middle finger gesture detected",
                        (text_x, text_y - 30), cv2.FONT_HERSHEY_DUPLEX,
                        FONT_SIZE, (0, 0, 255), FONT_THICKNESS, cv2.LINE_AA)
            return annotated_image, True


        # Draw handedness (left or right hand) on the image.
        cv2.putText(annotated_image, f"{handedness[0].category_name}",
                    (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                    FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

    return annotated_image, False