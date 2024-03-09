import cv2
import os
import cv2
from hand_detection import HandDetector
from gesture_recognition import are_fingers_up, perform_action

def main():
    hand_detector = HandDetector()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame.")
            break

        landmarks = hand_detector.detect_hand_landmarks(frame)

        if landmarks.multi_hand_landmarks:
            for hand_landmarks in landmarks.multi_hand_landmarks:
                fingers_up = are_fingers_up(hand_landmarks)
                if all(fingers_up):
                    perform_action("play")
                elif not any(fingers_up):
                    perform_action("pause")
                elif hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                    perform_action("rewind")

        cv2.imshow('Hand Gesture Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
