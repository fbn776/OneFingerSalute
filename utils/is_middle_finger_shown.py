import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def is_middle_finger_gesture(hand_landmarks, width, height):
    coords = [(int(landmark.x * width), int(landmark.y * height)) for landmark in hand_landmarks]

    thumb_tip = coords[4]
    index_tip = coords[8]
    middle_tip = coords[12]
    ring_tip = coords[16]
    pinky_tip = coords[20]

    wrist = coords[0]
    middle_base = coords[9]

    middle_extension = distance(middle_tip, wrist)
    middle_base_to_wrist = distance(middle_base, wrist)
    middle_is_extended = middle_extension > 1.5 * middle_base_to_wrist

    index_mcp = coords[5]
    ring_mcp = coords[13]
    pinky_mcp = coords[17]

    index_is_curled = distance(index_tip, wrist) < 1.2 * distance(index_mcp, wrist)
    ring_is_curled = distance(ring_tip, wrist) < 1.2 * distance(ring_mcp, wrist)
    pinky_is_curled = distance(pinky_tip, wrist) < 1.2 * distance(pinky_mcp, wrist)

    is_gesture = (middle_is_extended and
                  index_is_curled and
                  ring_is_curled and
                  pinky_is_curled)

    return is_gesture
