def are_fingers_up(landmarks):
    finger_tip_indices = [8, 12, 16, 20]
    fingers_up = [landmarks.landmark[index].y < landmarks.landmark[index - 2].y for index in finger_tip_indices]
    return fingers_up

def perform_action(gesture):
    if gesture == "play":
        print("Action: Play")



    elif gesture == "pause":
        print("Action: Pause")



    elif gesture == "rewind":
        print("Action: Rewind")


