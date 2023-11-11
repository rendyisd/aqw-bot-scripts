import multiprocessing
import cv2
import mss
import numpy as np
import time
import pyautogui
import win32gui, win32con
import pywinauto

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


def temp_match(hy, ndl):
    result = cv2.matchTemplate(hy, ndl, cv2.TM_CCOEFF_NORMED)
    threshold = .90

    target = np.where(result >= threshold)

    if(len(target[0]) > 0):
        return True


def open_quest():
    pyautogui.click(1400, 960, 1, button="left")
    time.sleep(0.5)
    pyautogui.click(1390, 850, 1, button="left")
    time.sleep(0.5)


def turn_in_quest():
    pyautogui.click(270, 292, 1, button="left") # quest
    time.sleep(1.5)
    pyautogui.click(430, 820, 1, button="left") # turn in
    time.sleep(1.5)
    return


def walk_to_mana():
    pyautogui.click(1555, 890, 1, button="left")
    time.sleep(2)
    pyautogui.click(422, 722, 1, button="left")
    time.sleep(2)
    pyautogui.click(1750, 840, 1, button="left")
    time.sleep(3)


def walk_to_elemental():
    pyautogui.click(963, 113, 1, button="left")
    time.sleep(2)
    pyautogui.click(267, 532, 1, button="left")
    time.sleep(2)
    pyautogui.click(1615, 265, 1, button="left")
    time.sleep(2)


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

    elem = cv2.imread('elem.jpg', cv2.IMREAD_UNCHANGED)
    mana = cv2.imread('mana.jpg', cv2.IMREAD_UNCHANGED)

    while(True):
        tmp_bool = False
        while(not tmp_bool):
            hay_elem = take_ss(1684, 103, 43, 30)
            if(temp_match(hay_elem, elem)):
                walk_to_mana()
                open_quest()

                it = 0

                while(not tmp_bool and it < 12):
                    hay_mana = take_ss(1409, 156, 40, 30)
                    if(temp_match(hay_mana, mana)):
                        turn_in_quest()
                        it += 1
                    time.sleep(1)

                tmp_bool = True
                walk_to_elemental()
                
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


'''
elem ss: (1684, 103, 43, 30)

mana ss: (1409, 156, 40, 30)

======================================

e = elemental room
m = mana room

e -> m
(1555, 890)
(422, 722) then (1750, 840)

m -> e
(963, 113)
(267, 532) then (1615, 265)

======================================

open quest pop up

(1400, 960) then (1390, 850)
'''
