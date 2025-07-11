import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, max_hands=1):
        self.hands = mp.solutions.hands.Hands(max_num_hands=max_hands)
        self.draw = mp.solutions.drawing_utils

    def get_landmarks(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)
        landmarks = []
        if result.multi_hand_landmarks:
            for hand in result.multi_hand_landmarks:
                self.draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
                for id, lm in enumerate(hand.landmark):
                    h, w, _ = frame.shape
                    landmarks.append((int(lm.x * w), int(lm.y * h)))
        return landmarks if landmarks else None
