import time
import sys
import multiprocessing
import cv2
import pywinauto
import pyautogui

sys.path.append("../..")
import func_module as fm

APP_HANDLE = fm.get_app_handle()

def skill_auto_vhl():
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
        

def mana(needle):
    p1 = multiprocessing.Process(target = fm.temp_match, args = [(320, 850, 55, 30), needle])
    p2 = multiprocessing.Process(target = skill_auto_vhl)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def elemental(needle):
    pyautogui.click(120, 680, 1, button='left')
    time.sleep(2.5)
    pyautogui.click(1350, 350, 1, button='left')
    time.sleep(2)
    pyautogui.click(1000, 680, 1, button='left')
    time.sleep(2)
    pyautogui.click(1790, 570, 1, button='left')
    time.sleep(2)
    pyautogui.click(900, 660, 1, button='left')
    time.sleep(1)

    p1 = multiprocessing.Process(target = fm.temp_match, args = [(395, 825, 55, 30), needle])
    p2 = multiprocessing.Process(target = skill_auto_vhl)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def mask(needle):
    p1 = multiprocessing.Process(target = fm.temp_match, args = [(300, 880, 40, 30), needle])
    p2 = multiprocessing.Process(target = skill_auto_cav)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def change_class(app : pywinauto.Application, to_):
    app.window().send_keystrokes("i") # open inventory
    time.sleep(0.5)

    if(to_ == 'vhl'):
        pyautogui.click(1410, 140, 1, button='left') # open class
        time.sleep(0.5)
        pyautogui.click(1480, 680, 1, button='left') # select vhl (10th item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)

        pyautogui.click(1460, 140, 1, button='left') # open helmet
        time.sleep(0.5)
        pyautogui.click(1480, 190, 1, button='left') # select helmet (1st item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)

        pyautogui.click(1500, 140, 1, button='left') # open cape
        time.sleep(0.5)
        pyautogui.click(1480, 300, 1, button='left') # select cape (3rd item)
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

        pyautogui.click(1500, 140, 1, button='left') # open cape
        time.sleep(0.5)
        pyautogui.click(1480, 250, 1, button='left') # select cape (2nd item)
        time.sleep(0.5)
        pyautogui.click(1070, 860, 1, button='left') # equip
        time.sleep(2)
    
    pyautogui.click(1780, 950, 1, button='left') # close inventory
    time.sleep(0.5)


def reset_player():
    pyautogui.click(590, 890, 1, button='left')
    time.sleep(1)
    change_class(app = APP_HANDLE, to_='vhl')
    pyautogui.click(980, 680, 1, button='left')
    time.sleep(3)
    pyautogui.click(130, 700, 1, button='left')
    time.sleep(3)
    pyautogui.click(890, 680, 1, button='left')
    time.sleep(3)
    pyautogui.click(130, 540, 1, button='left')
    time.sleep(3)
    pyautogui.click(1790, 520, 1, button='left')
    time.sleep(3)
    pyautogui.click(700, 660, 1, button='left')
    

def turn_in_quest():
    pyautogui.click(270, 292, 1, button='left') # quest
    time.sleep(1)
    pyautogui.click(430, 820, 1, button='left') # turn in
    time.sleep(1.5)


def main():
    needle_1 = cv2.imread(r'img/needle_mana.png', cv2.IMREAD_UNCHANGED) # mana
    needle_2 = cv2.imread(r'img/needle_elemental.png', cv2.IMREAD_UNCHANGED) # elemental
    needle_3 = cv2.imread(r'img/needle_mask.png', cv2.IMREAD_UNCHANGED) # mask

    needle_1 = cv2.cvtColor(needle_1, cv2.COLOR_BGRA2BGR)
    needle_2 = cv2.cvtColor(needle_2, cv2.COLOR_BGRA2BGR)
    needle_3 = cv2.cvtColor(needle_3, cv2.COLOR_BGRA2BGR)

    while(True):
        # Start from mana middle
        mana(needle = needle_1)
        elemental(needle = needle_2)

        pyautogui.click(1640, 240, 1, button='left')
        time.sleep(3)

        change_class(app = APP_HANDLE, to_='cav')

        APP_HANDLE.window().send_keystrokes("c") # open quest

        for _ in range(5):
            mask(needle = needle_3)
            turn_in_quest()

        reset_player() # back to mana

if __name__ == "__main__":
    main()