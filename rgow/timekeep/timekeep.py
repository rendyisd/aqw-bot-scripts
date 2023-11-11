import time
import sys
import multiprocessing
import cv2
import pywinauto
import pyautogui

sys.path.append("../..")
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

def locust(app : pywinauto.Application, needle):
    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1620, 155, 55, 30), needle])
    p2 = multiprocessing.Process(target = skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def mumbler(app : pywinauto.Application, needle):
    pyautogui.click(1800, 650, 1, button='left')
    time.sleep(1)

    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1635, 130, 55, 30), needle])
    p2 = multiprocessing.Process(target = skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def gar(app : pywinauto.Application, needle):
    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1725, 100, 40, 30), needle])
    p2 = multiprocessing.Process(target = skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def change_class(app : pywinauto.Application, to_):
    app.window().send_keystrokes("i") # open inventory
    time.sleep(0.5)

    if(to_ == 'lr'):
        pyautogui.click(1410, 140, 1, button='left') # open class
        time.sleep(0.5)
        pyautogui.click(1480, 470, 1, button='left') # select lr (6th item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)

        pyautogui.click(1460, 140, 1, button='left') # open helmet
        time.sleep(0.5)
        pyautogui.click(1480, 300, 1, button='left') # select helmet (3rd item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)

        pyautogui.click(1510, 140, 1, button='left') # open cape
        time.sleep(0.5)
        pyautogui.click(1480, 250, 1, button='left') # select cape (2nd item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)
    
    if(to_ == 'vhl'):
        pyautogui.click(1410, 140, 1, button='left') # open class
        time.sleep(0.5)
        pyautogui.click(1480, 685, 1, button='left') # select vhl (10th item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)

        pyautogui.click(1460, 140, 1, button='left') # open helmet
        time.sleep(0.5)
        pyautogui.click(1480, 250, 1, button='left') # select helmet (2nd item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)

        pyautogui.click(1510, 140, 1, button='left') # open cape
        time.sleep(0.5)
        pyautogui.click(1480, 300, 1, button='left') # select cape (3rd item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)
    
    pyautogui.click(1780, 950, 1, button='left') # close inventory
    time.sleep(0.5)


def reset_player():
    pyautogui.click(135, 690, 1, button='left')
    time.sleep(4)
    change_class(app = APP_HANDLE, to_='lr')
    pyautogui.click(120, 650, 1, button='left')
    time.sleep(4)

def turn_in_quest():
    pyautogui.click(270, 292, 1, button='left') # quest
    time.sleep(1)
    pyautogui.click(430, 820, 1, button='left') # turn in
    time.sleep(1.5)


def main():
    needle_1 = cv2.imread(r'img/needle_locust.png', cv2.IMREAD_UNCHANGED) # Locust
    needle_2 = cv2.imread(r'img/needle_mumbler.png', cv2.IMREAD_UNCHANGED) # Mumbler
    needle_3 = cv2.imread(r'img/needle_gar.png', cv2.IMREAD_UNCHANGED) # Gar

    needle_1 = cv2.cvtColor(needle_1, cv2.COLOR_BGRA2BGR)
    needle_2 = cv2.cvtColor(needle_2, cv2.COLOR_BGRA2BGR)
    needle_3 = cv2.cvtColor(needle_3, cv2.COLOR_BGRA2BGR)

    while(True):
        # Start from locust right side
        locust(app = APP_HANDLE, needle = needle_1)
        mumbler(app = APP_HANDLE, needle = needle_2)

        pyautogui.click(1600, 460, 1, button='left')
        time.sleep(4)

        change_class(app = APP_HANDLE, to_='vhl')

        APP_HANDLE.window().send_keystrokes("t") # select gar
        time.sleep(0.5)
        APP_HANDLE.window().send_keystrokes("1") # attack
        APP_HANDLE.window().send_keystrokes("c") # open quest

        for _ in range(4):
            gar(app = APP_HANDLE, needle = needle_3)
            turn_in_quest()

        reset_player() # back to locust

if __name__ == "__main__":
    main()