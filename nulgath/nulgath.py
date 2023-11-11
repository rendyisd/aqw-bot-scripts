import time
import sys
import multiprocessing
import cv2
import pywinauto
import pyautogui

sys.path.append("..")
import func_module as fm

APP_HANDLE = fm.get_app_handle()

def skill_auto():
    while(True):
        APP_HANDLE.window().send_keystrokes("4")
        time.sleep(1)
        APP_HANDLE.window().send_keystrokes("5")
        time.sleep(1)
        APP_HANDLE.window().send_keystrokes("3")
        time.sleep(1)
        APP_HANDLE.window().send_keystrokes("2")
        time.sleep(1)

def mobius_imp(app : pywinauto.Application, needle):
    app.window().send_keystrokes("y")
    time.sleep(4)

    pyautogui.click(1060, 60, 1, button='left')

    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1565, 158, 40, 32), needle])
    p2 = multiprocessing.Process(target = skill_auto)


    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def mobius_slugfit(app : pywinauto.Application, needle):
    pyautogui.click(1790, 250, 1, button='left')

    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1575, 100, 40, 32), needle])
    p2 = multiprocessing.Process(target = skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def evilmarsh(app : pywinauto.Application, needle):
    app.window().send_keystrokes("y")
    time.sleep(4)

    pyautogui.click(1800, 690, 1, button='left')

    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1575, 130, 40, 32), needle])
    p2 = multiprocessing.Process(target = skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

    pyautogui.click(115, 675, 1, button='left')
    time.sleep(0.5)

def faerie(app : pywinauto.Application, needle):
    app.window().send_keystrokes("y")
    time.sleep(4)

    pyautogui.click(880, 895, 1, button='left')
    time.sleep(1)
    pyautogui.click(1800, 815, 1, button='left')
    time.sleep(5)

    pyautogui.click(1800, 815, 1, button='left')
    time.sleep(5.5)

    pyautogui.click(802, 902, 1, button='left')
    time.sleep(0.5)
    pyautogui.click(1800, 865, 1, button='left')
    time.sleep(5)

    pyautogui.click(1000, 415, 1, button='left')

    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1593, 185, 40, 32), needle])
    p2 = multiprocessing.Process(target = skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

    pyautogui.click(960, 900, 1, button='left')
    time.sleep(0.5)

def ggwest(app : pywinauto.Application, needle):
    app.window().send_keystrokes("y")
    time.sleep(4)

    fm.drag_click((1787, 90), (1787, 235))

    pyautogui.click(280, 620, 1, button='left')
    time.sleep(4)

    pyautogui.click(120, 630, 1, button='left')
    time.sleep(5)

    pyautogui.click(120, 470, 1, button='left')
    time.sleep(5)

    pyautogui.click(130, 640, 1, button='left')
    time.sleep(2)

    pyautogui.click(815, 590, 1, button='left')
    time.sleep(2)
    pyautogui.click(425, 290, 1, button='left')
    time.sleep(2)

    pyautogui.click(1195, 890, 1, button='left')
    time.sleep(2)

    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1611, 185, 40, 32), needle])
    p2 = multiprocessing.Process(target = skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

    fm.drag_click((1787, 175), (1787, 40))

    app.window().send_keystrokes("c")
    time.sleep(0.5)
    fm.turn_in_quest()
    time.sleep(1)


def main():
    NEEDLE_1 = cv2.imread(r'img/needle1.jpg', cv2.IMREAD_UNCHANGED) # Imp
    NEEDLE_2 = cv2.imread(r'img/needle2.jpg', cv2.IMREAD_UNCHANGED) # Slugfit
    NEEDLE_3 = cv2.imread(r'img/needle3.jpg', cv2.IMREAD_UNCHANGED) # Makai
    NEEDLE_4 = cv2.imread(r'img/needle4.jpg', cv2.IMREAD_UNCHANGED) # Cyclops
    NEEDLE_5 = cv2.imread(r'img/needle5.jpg', cv2.IMREAD_UNCHANGED) # Wereboar

    while(True):
        mobius_imp(app = APP_HANDLE, needle = NEEDLE_1)
        mobius_slugfit(app = APP_HANDLE, needle = NEEDLE_2)
        evilmarsh(app = APP_HANDLE, needle = NEEDLE_3)
        faerie(app = APP_HANDLE, needle = NEEDLE_4)
        ggwest(app = APP_HANDLE, needle = NEEDLE_5)

if __name__ == "__main__":
    main()