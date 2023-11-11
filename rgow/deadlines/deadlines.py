import time
import sys
import multiprocessing
import cv2
import pywinauto
import pyautogui

sys.path.append("../..")
import func_module as fm

APP_HANDLE = fm.get_app_handle()

def skill_auto_lr():
    while(True):
        APP_HANDLE.window().send_keystrokes("4")
        time.sleep(1)
        APP_HANDLE.window().send_keystrokes("5")
        time.sleep(1)
        APP_HANDLE.window().send_keystrokes("3")
        time.sleep(1)
        APP_HANDLE.window().send_keystrokes("2")
        time.sleep(1)

def skill_auto_cav():
    while(True):
        APP_HANDLE.window().send_keystrokes("3")
        APP_HANDLE.window().send_keystrokes("4")
        APP_HANDLE.window().send_keystrokes("5")
        APP_HANDLE.window().send_keystrokes("2")
        

def knight(needle):
    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1645, 100, 55, 30), needle])
    p2 = multiprocessing.Process(target = skill_auto_lr)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def mana(needle):
    pyautogui.click(1800, 650, 1, button='left')
    time.sleep(1)
    pyautogui.click(770, 610, 1, button='left')

    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1675, 130, 55, 30), needle])
    p2 = multiprocessing.Process(target = skill_auto_lr)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def dragon(needle):
    p1 = multiprocessing.Process(target = fm.temp_match, args = [(1730, 155, 40, 30), needle])
    p2 = multiprocessing.Process(target = skill_auto_cav)

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
    
    if(to_ == 'cav'):
        pyautogui.click(1410, 140, 1, button='left') # open class
        time.sleep(0.5)
        pyautogui.click(1480, 300, 1, button='left') # select cav (3rd item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)

        pyautogui.click(1460, 140, 1, button='left') # open helmet
        time.sleep(0.5)
        pyautogui.click(1480, 250, 1, button='left') # select helmet (2nd item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)
    
    pyautogui.click(1780, 950, 1, button='left') # close inventory
    time.sleep(0.5)


def reset_player():
    pyautogui.click(1200, 900, 1, button='left')
    time.sleep(1)
    change_class(app = APP_HANDLE, to_='lr')
    pyautogui.click(120, 710, 1, button='left')
    time.sleep(4)
    pyautogui.click(960, 890, 1, button='left')
    time.sleep(3)
    pyautogui.click(120, 320, 1, button='left')
    time.sleep(4)

def turn_in_quest():
    pyautogui.click(270, 292, 1, button='left') # quest
    time.sleep(1)
    pyautogui.click(430, 820, 1, button='left') # turn in
    time.sleep(1.5)


def main():
    needle_1 = cv2.imread(r'img/needle_knight.png', cv2.IMREAD_UNCHANGED) # Knight
    needle_2 = cv2.imread(r'img/needle_mana.png', cv2.IMREAD_UNCHANGED) # Mana
    needle_3 = cv2.imread(r'img/needle_dragon.png', cv2.IMREAD_UNCHANGED) # Dragon

    needle_1 = cv2.cvtColor(needle_1, cv2.COLOR_BGRA2BGR)
    needle_2 = cv2.cvtColor(needle_2, cv2.COLOR_BGRA2BGR)
    needle_3 = cv2.cvtColor(needle_3, cv2.COLOR_BGRA2BGR)

    while(True):
        # Start from knight right side
        knight(needle = needle_1)
        mana(needle = needle_2)

        pyautogui.click(1800, 740, 1, button='left')
        time.sleep(3)
        pyautogui.click(1800, 760, 1, button='left')
        time.sleep(2.5)
        pyautogui.click(1800, 720, 1, button='left')
        time.sleep(4)

        change_class(app = APP_HANDLE, to_='cav')

        APP_HANDLE.window().send_keystrokes("c") # open quest

        for _ in range(5):
            dragon(needle = needle_3)
            turn_in_quest()

        reset_player() # back to knight

if __name__ == "__main__":
    main()