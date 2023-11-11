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

def reset_player():
    fm.left_click((120, 700), 3)
    fm.left_click((120, 680), 5)
    fm.left_click((120, 680), 5)
    fm.left_click((120, 680), 5)
    fm.left_click((890, 670), 5)
    change_class(sword=None, p_class=None, helm=1, cape=None)
    

def turn_in_quest():
    fm.left_click((270, 292), 1)
    fm.left_click((430, 820), 1.5)


def main():
    needle_1 = cv2.imread(r'img/needle_mana.png', cv2.IMREAD_UNCHANGED) # mana
    needle_2 = cv2.imread(r'img/needle_malgor.png', cv2.IMREAD_UNCHANGED) # malgor
    needle_3 = cv2.imread(r'img/needle_mainyu.png', cv2.IMREAD_UNCHANGED) # mainyu

    needle_1 = cv2.cvtColor(needle_1, cv2.COLOR_BGRA2BGR)
    needle_2 = cv2.cvtColor(needle_2, cv2.COLOR_BGRA2BGR)
    needle_3 = cv2.cvtColor(needle_3, cv2.COLOR_BGRA2BGR)

    while(True):
        '''
        - Setup: Valiance, CAv, Anima, Vainglory (change anima to lucky when mainyu)
        - Start from mana, between the monsters
        - Quest box on bottom left
        - Hide monster
        '''

        # mana
        attack_and_match(skill_auto=skill_auto_cav, ss_pos=(300, 825, 50, 30), needle=needle_1)
        fm.left_click((1800, 680), 2.5)
        fm.left_click((1800, 690), 5)
        fm.left_click((1800, 700), 5)

        # malgor
        attack_and_match(skill_auto=skill_auto_cav, ss_pos=(385, 855, 40, 30), needle=needle_2)
        fm.left_click((1800, 700), 5)

        # mainyu
        change_class(sword=None, p_class=None, helm=0, cape=None)
        APP_HANDLE.window().send_keystrokes("c") # open quest

        for _ in range(5):
            attack_and_match(skill_auto=skill_auto_cav, ss_pos=(290, 880, 35, 30), needle = needle_3)
            turn_in_quest()

        reset_player() # back to mana

if __name__ == "__main__":
    main()