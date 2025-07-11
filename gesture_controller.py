class GestureController:
    def recognize(self, landmarks):
        if not landmarks:
            return None

        # Example: if only index finger is up
        if self.is_finger_up(landmarks, 8):
            return "move_cursor"
        elif self.is_pinch(landmarks, 8, 4):
            return "left_click"
        elif self.is_scroll_gesture(landmarks):
            return "scroll"

        return None

    def is_finger_up(self, lm, tip_id):
        return lm[tip_id][1] < lm[tip_id - 2][1]

    def is_pinch(self, lm, i1, i2):
        x1, y1 = lm[i1]
        x2, y2 = lm[i2]
        return abs(x1 - x2) < 40 and abs(y1 - y2) < 40

    def is_scroll_gesture(self, lm):
        return self.is_finger_up(lm, 8) and self.is_finger_up(lm, 12)
