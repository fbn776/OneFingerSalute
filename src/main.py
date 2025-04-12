import os
from time import sleep
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from utils.draw_landmark import draw_landmarks_on_image
from utils.shutdown import shutdown

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'model', 'hand_landmarker.task')

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)


def do_hand_detection():
    cap = cv2.VideoCapture(0)

    is_middle_finger_up = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from webcam.")
            break

        flipped_frame = cv2.flip(frame, 1)

        frame_rgb = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

        detection_result = detector.detect(mp_image)

        annotated_frame, middle_finger_up = draw_landmarks_on_image(frame_rgb, detection_result)

        cv2.imshow("Hand Landmarks", cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR))

        if middle_finger_up:
            is_middle_finger_up = True
            break

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    if is_middle_finger_up:
        cap.release()
        cv2.destroyAllWindows()
        try:
            print("F you!!!")
            print("Shutting down in: 3")
            sleep(1)
            print("Shutting down in: 2")
            sleep(1)
            print("Shutting down in: 1")
            sleep(1)
            print("Shutting down now...")
            shutdown()
        except KeyboardInterrupt:
            print("Shutdown interrupted.")
            return
        except:
            print("An error occurred during shutdown.")
            return


    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    do_hand_detection()