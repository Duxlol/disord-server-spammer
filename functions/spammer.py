import sys
import time
import pyautogui
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from python_imagesearch.imagesearch import imagesearch

keyboard = KeyboardController()
mouse = MouseController()

def bot():
    # take ss of screen
    im1 = pyautogui.screenshot('screen.png', region=(0, 0, 1920, 1080))
    time.sleep(0.5)

    # find + icon
    pos = imagesearch(r"D:\coding\discord-server-spammer\functions\plus.png")
    if pos[0] != -1:
        print("Found plus icon")
        time.sleep(0.5)
        pyautogui.click(pos[0],pos[1])
    else:
        print("Didn't find plus icon")
        sys.exit

    # move mouse and click
    pyautogui.click(970,450)
    time.sleep(0.5)
    pyautogui.click(942,518)
    time.sleep(0.5)
    pyautogui.click(1100,730)
    time.sleep(0.5)