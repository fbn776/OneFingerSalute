import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from draw_landmark import draw_landmarks_on_image

# Initialize Hand Landmarker
base_options = python.BaseOptions(model_asset_path='./model/hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

# Open the webcam (0 for default camera)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()  # Read frame from webcam
    if not ret:
        break  # Stop if the frame is empty

    # Flip the camera frame first (mirror effect)
    flipped_frame = cv2.flip(frame, 1)

    # Convert the flipped frame to RGB (since OpenCV reads in BGR)
    frame_rgb = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB)

    # Convert OpenCV image to Mediapipe image format
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

    # Detect hand landmarks
    detection_result = detector.detect(mp_image)

    # Draw landmarks on the flipped frame
    annotated_frame = draw_landmarks_on_image(frame_rgb, detection_result)

    # Convert back to BGR for OpenCV display
    cv2.imshow("Hand Landmarks", cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR))

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
