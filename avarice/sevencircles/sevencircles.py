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
        APP_HANDLE.window().send_keystrokes("1")
        APP_HANDLE.window().send_keystrokes("4")
        APP_HANDLE.window().send_keystrokes("5")
        APP_HANDLE.window().send_keystrokes("2")
        
'''
skill_auto  : skill auto function
ss_pos      : screenshot position for hay e.g. (top_left_x, top_left_y, width, height)
'''
def attack_and_match(skill_auto, ss_pos, needle):
    p1 = multiprocessing.Process(target = fm.temp_match, args = [ss_pos, needle])
    p2 = multiprocessing.Process(target = skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def change_class(sword, p_class, helm, cape):
    ITEM_CATEGORY_TOP_LEFT = (1320, 145)
    ITEM_TOP_LEFT = (1400, 200)

    ITEM_CATEGORY_WIDTH = 45
    ITEM_HEIGHT = 50

    APP_HANDLE.window().send_keystrokes("i") # open inventory
    time.sleep(0.5)
    
    # the width and height here being multiplied by index (start from 0) in your inventory
    if sword is not None:
        fm.left_click((ITEM_CATEGORY_TOP_LEFT[0] + ITEM_CATEGORY_WIDTH * 1, ITEM_CATEGORY_TOP_LEFT[1]), 0.5)
        fm.left_click((ITEM_TOP_LEFT[0], ITEM_TOP_LEFT[1] + ITEM_HEIGHT * sword), 0.5)
        fm.left_click((1070, 860), 2) # equip
    
    if p_class is not None:
        fm.left_click((ITEM_CATEGORY_TOP_LEFT[0] + ITEM_CATEGORY_WIDTH * 2, ITEM_CATEGORY_TOP_LEFT[1]), 0.5)
        fm.left_click((ITEM_TOP_LEFT[0], ITEM_TOP_LEFT[1] + ITEM_HEIGHT * p_class), 0.5)
        fm.left_click((1070, 860), 2) # equip
    
    if helm is not None:
        fm.left_click((ITEM_CATEGORY_TOP_LEFT[0] + ITEM_CATEGORY_WIDTH * 3, ITEM_CATEGORY_TOP_LEFT[1]), 0.5)
        fm.left_click((ITEM_TOP_LEFT[0], ITEM_TOP_LEFT[1] + ITEM_HEIGHT * helm), 0.5)
        fm.left_click((1070, 860), 2) # equip
    
    if cape is not None:
        fm.left_click((ITEM_CATEGORY_TOP_LEFT[0] + ITEM_CATEGORY_WIDTH * 4, ITEM_CATEGORY_TOP_LEFT[1]), 0.5)
        fm.left_click((ITEM_TOP_LEFT[0], ITEM_TOP_LEFT[1] + ITEM_HEIGHT * cape), 0.5)
        fm.left_click((1070, 860), 2) # equip
    
    fm.left_click((1780, 950), 0.5) # close inventory

ROOM_NUMBER = ["6281", "4601"]
curr_idx = 1

def reset_player():
    global curr_idx

    time.sleep(3)

    APP_HANDLE.window().send_keystrokes("/join sevencircles-"+ROOM_NUMBER[curr_idx]+"{ENTER}")
    curr_idx = 0 if curr_idx == 1 else 1

    time.sleep(4)

    fm.left_click((1760, 880), 4)
    change_class(sword=None, p_class=5, helm=2, cape=None)
    

def turn_in_quest():
    fm.left_click((270, 292), 1)
    fm.left_click((430, 820), 1.5)


def main():
    needle_1 = cv2.imread(r'img/needle_limbo.png', cv2.IMREAD_UNCHANGED) # limbo
    needle_2 = cv2.imread(r'img/needle_luxuria.png', cv2.IMREAD_UNCHANGED) # luxuria
    needle_3 = cv2.imread(r'img/needle_gluttony.png', cv2.IMREAD_UNCHANGED) # gluttony
    needle_4 = cv2.imread(r'img/needle_avarice.png', cv2.IMREAD_UNCHANGED) # avarice

    needle_1 = cv2.cvtColor(needle_1, cv2.COLOR_BGRA2BGR)
    needle_2 = cv2.cvtColor(needle_2, cv2.COLOR_BGRA2BGR)
    needle_3 = cv2.cvtColor(needle_3, cv2.COLOR_BGRA2BGR)
    needle_4 = cv2.cvtColor(needle_4, cv2.COLOR_BGRA2BGR)

    while(True):
        '''
        - Start from limbo left
        - Quest box on bottom left
        - Hide monster, start with legion revenant
        '''

        # limbo
        attack_and_match(skill_auto=skill_auto_lr, ss_pos=(295, 880, 60, 25), needle=needle_1)
        fm.left_click((1500, 880), 4)
        fm.left_click((930, 265), 1.5)
        fm.left_click((320, 710), 3)
        fm.left_click((970, 835), 2)
        fm.left_click((1790, 810), 3)
        change_class(sword=None, p_class=2, helm=1, cape=None)

        # luxuria
        attack_and_match(skill_auto=skill_auto_cav, ss_pos=(335, 800, 35, 25), needle=needle_2)
        fm.left_click((1770, 800), 4)
        fm.left_click((930, 265), 1.5)
        fm.left_click((320, 710), 3)
        fm.left_click((970, 835), 2)
        fm.left_click((1790, 810), 2)

        # gluttony
        attack_and_match(skill_auto=skill_auto_cav, ss_pos=(345, 825, 35, 25), needle=needle_3)
        fm.left_click((1160, 860), 4)
        fm.left_click((1540, 540), 2)
        fm.left_click((1100, 880), 2)

        # avarice
        APP_HANDLE.window().send_keystrokes("c") # open quest

        for _ in range(3):
            attack_and_match(skill_auto=skill_auto_cav, ss_pos=(340, 855, 35, 25), needle = needle_4)
            turn_in_quest()

        reset_player() # back to limbo

if __name__ == "__main__":
    main()