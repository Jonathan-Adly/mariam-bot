import time

import pyautogui


def move_mouse_and_refresh():
    while True:
        # Move the mouse slightly
        pyautogui.move(0, 1)
        pyautogui.move(0, -1)
        print("Mouse moved to prevent sleep.")
        time.sleep(60)  # Wait for 1 minute

        # Every 10 minutes, click at the refresh button coordinates (example coordinates given)
        if time.time() % 600 < 60:
            # Please replace (x, y) with the actual coordinates of your refresh button
            pyautogui.click(x=100, y=100)
            print("Browser refreshed.")


if __name__ == "__main__":
    move_mouse_and_refresh()
