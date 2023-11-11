import multiprocessing
import cv2
import mss
import numpy as np
import time
import pyautogui
import win32gui, win32con
import pywinauto

def take_ss(left=0, top=0, width=1920, height=1080): # 1656 101 70 30
    stc = mss.mss()
    scr = stc.grab({
        'left':left,
        'top':top,
        'width':width,
        'height':height
    })
    
    img = np.array(scr)
    img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

    return img


def temp_match(hy, ndl):
    result = cv2.matchTemplate(hy, ndl, cv2.TM_CCOEFF_NORMED)
    threshold = .95

    target = np.where(result >= threshold)

    if(len(target[0]) > 0):
        return True


def turn_in_quest():
    pyautogui.click(270, 292, 1, button="left") # quest
    time.sleep(1)
    pyautogui.click(430, 820, 1, button="left") # turn in
    time.sleep(1)
    return


def script1():
    time.sleep(4)

    hwnd = win32gui.GetForegroundWindow()
    hwnd = win32gui.GetWindow(hwnd, win32con.GW_CHILD)

    app = pywinauto.application.Application().connect(handle=hwnd)

    while(True):
        app.window().send_keystrokes("2")
        time.sleep(1)
        app.window().send_keystrokes("3")
        time.sleep(1)


def script2():
    time.sleep(4)

    needle1 = cv2.imread('ndl1.jpg', cv2.IMREAD_UNCHANGED)
    needle2 = cv2.imread('ndl2.jpg', cv2.IMREAD_UNCHANGED)

    while(True):
        tmp_bool = False
        while(not tmp_bool):
            hay1 = take_ss(219, 889, 64, 28)
            if(temp_match(hay1, needle1)):
                time.sleep(7)
                while(not tmp_bool):
                    hay2 = take_ss(790, 730, 340, 200)
                    if(temp_match(hay2, needle2)):
                        turn_in_quest()
                        tmp_bool = True
                        time.sleep(100)
                    time.sleep(1)
            time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=script1)
    p2 = multiprocessing.Process(target=script2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
