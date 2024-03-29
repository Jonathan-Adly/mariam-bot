import time

import pyautogui


def move_mouse_and_refresh():
    print ("Starting the program and refreshing")
    pyautogui.click(x=118, y=73)
    while True:
        # Move the mouse slightly
        pyautogui.move(0, 1)
        pyautogui.move(0, -1)
        print("Mouse moved to prevent sleep.")
        time.sleep(60)  # Wait for 1 minute

        # Every 10 minutes, click at the refresh button coordinates (example coordinates given)
        if time.time() % 600 < 60:
            pyautogui.click(x=118, y=73)
            print("Browser refreshed.")


if __name__ == "__main__":
    move_mouse_and_refresh()
