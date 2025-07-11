import pyautogui

def perform_action(gesture, landmarks):
    if gesture == "move_cursor":
        x, y = landmarks[8]
        screen_w, screen_h = pyautogui.size()
        pyautogui.moveTo(x * screen_w / 640, y * screen_h / 480)

    elif gesture == "left_click":
        pyautogui.click()

    elif gesture == "scroll":
        pyautogui.scroll(-20)
