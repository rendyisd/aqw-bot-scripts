import cv2
import mss
import numpy as np
import time
import pyautogui
import pywinauto
import win32gui, win32con


def get_app_handle():
    time.sleep(3)

    hwnd = win32gui.GetForegroundWindow()
    hwnd = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
    app = pywinauto.application.Application().connect(handle=hwnd)

    return app


def take_ss(left=0, top=0, width=1920, height=1080):
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


def temp_match(coord, ndl):
    tmp_bool = False
    threshold = .95

    while(not tmp_bool):
        hy = take_ss(coord[0], coord[1], coord[2], coord[3]) # Top, left, width, height
        result = cv2.matchTemplate(hy, ndl, cv2.TM_CCOEFF_NORMED)

        target = np.where(result >= threshold)

        if(len(target[0]) > 0):
            tmp_bool = True
        time.sleep(1)


def left_click(coord, delay):
    pyautogui.click(coord[0], coord[1], 1, button='left') # open class
    time.sleep(delay)


def drag_click(start, stop):
    pyautogui.moveTo(start[0], start[1])
    time.sleep(0.5)
    pyautogui.dragTo(stop[0], stop[1], button='left', duration=1)
    time.sleep(1)