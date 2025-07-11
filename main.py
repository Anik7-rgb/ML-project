import cv2
from utils.hand_detector import HandDetector
from utils.gesture_controller import GestureController
from utils.actions import perform_action

def find_working_camera():
    for i in range(3):  # Check first 3 camera indexes
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"✅ Camera index {i} is working.")
            return cap
        cap.release()
    print("❌ No available camera found.")
    return None

def main():
    cap = find_working_camera()
    if cap is None:
        return

    detector = HandDetector()
    controller = GestureController()

    while True:
        success, frame = cap.read()
        if not success or frame is None:
            print("⚠️ Frame not received from camera.")
            continue

        frame = cv2.flip(frame, 1)
        hand_landmarks = detector.get_landmarks(frame)

        if hand_landmarks:
            gesture = controller.recognize(hand_landmarks)
            if gesture:
                perform_action(gesture, hand_landmarks)

        cv2.imshow("Air Gesture Controller", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("👋 Exiting program.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
