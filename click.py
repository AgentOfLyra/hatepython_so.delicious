import time
import pyautogui
import sys
try:
    while True:
        ptx,pty = pyautogui.position()

        time.sleep(0.04)
        pyautogui.click(ptx,pty)
except KeyboardInterrupt:
    sys.exit(0)
