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

# Only the middle finger and joints are used for points plot
selected_indices = [5, 13, 17, 0, 9, 10, 11, 12]
custom_connections = [(9, 10), (10, 11), (11, 12), (5, 9), (9, 13), (13, 17), (0, 5), (0, 9), (0, 13), (0, 17)]

def draw_landmarks_on_image(rgb_image, detection_result):
    hand_landmarks_list = detection_result.hand_landmarks
    # handedness_list = detection_result.handedness
    annotated_image = np.copy(rgb_image)

    for idx in range(len(hand_landmarks_list)):
        hand_landmarks = hand_landmarks_list[idx]

        # Draw the hand landmarks.
        hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
        ])


        # solutions.drawing_utils.draw_landmarks(
        #     annotated_image,
        #     hand_landmarks_proto,
        #     solutions.hands.HAND_CONNECTIONS,
        #     solutions.drawing_styles.get_default_hand_landmarks_style(),
        #     solutions.drawing_styles.get_default_hand_connections_style(),
        #     # is_drawing_landmarks=False
        # )

        # Get the top left corner of the detected hand's bounding box.
        height, width, _ = annotated_image.shape
        x_coordinates = [landmark.x for landmark in hand_landmarks]
        y_coordinates = [landmark.y for landmark in hand_landmarks]

        for i in selected_indices:
            lm = hand_landmarks[i]
            cx, cy = int(lm.x * width), int(lm.y * height)
            cv2.circle(annotated_image, (cx, cy), 6, (255, 0, 0), -1)  # Blue dots

        # Draw custom connections
        for connection in custom_connections:
            start_idx, end_idx = connection
            x0 = int(hand_landmarks[start_idx].x * width)
            y0 = int(hand_landmarks[start_idx].y * height)
            x1 = int(hand_landmarks[end_idx].x * width)
            y1 = int(hand_landmarks[end_idx].y * height)
            cv2.line(annotated_image, (x0, y0), (x1, y1), (0, 255, 255), 2)

        # # Bounding box;
        # x_min, x_max = min(x_coordinates), max(x_coordinates)
        # y_min, y_max = min(y_coordinates), max(y_coordinates)
        #
        # cv2.rectangle(annotated_image,
        #               (int(x_min * width), int(y_min * height)),
        #               (int(x_max * width), int(y_max * height)),
        #               (0, 255, 0), 2)

        text_x = int(min(x_coordinates) * width)
        text_y = int(min(y_coordinates) * height) - MARGIN



        middle_finger_detected = is_middle_finger_gesture(hand_landmarks, width, height)

        # Display result
        if middle_finger_detected:
            cv2.putText(annotated_image, "Middle finger gesture detected",
                        (text_x, text_y - 30), cv2.FONT_HERSHEY_DUPLEX,
                        FONT_SIZE, (0, 0, 255), FONT_THICKNESS, cv2.LINE_AA)
            return annotated_image, True

    return annotated_image, False