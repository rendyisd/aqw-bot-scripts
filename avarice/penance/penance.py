import time
import sys
import multiprocessing
import cv2
import pywinauto
import pyautogui

sys.path.append("../..")
import func_module as fm

APP_HANDLE = fm.get_app_handle()

def skill_auto_cav():
    while(True):
        APP_HANDLE.window().send_keystrokes("3")
        APP_HANDLE.window().send_keystrokes("1")
        APP_HANDLE.window().send_keystrokes("4")
        APP_HANDLE.window().send_keystrokes("5")
        APP_HANDLE.window().send_keystrokes("2")

def attack_and_match(skill_auto, ss_pos, needle):
    p1 = multiprocessing.Process(target = fm.temp_match, args = [ss_pos, needle])
    p2 = multiprocessing.Process(target = skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()

def turn_in_quest():
    fm.left_click((270, 292), 1)
    fm.left_click((430, 820), 1.5)

def main():
    needle = cv2.imread(r'needle.png', cv2.IMREAD_UNCHANGED)
    needle = cv2.cvtColor(needle, cv2.COLOR_BGRA2BGR)

    while(True):
        attack_and_match(skill_auto=skill_auto_cav, ss_pos=(1730, 100, 40, 30), needle=needle)
        turn_in_quest()

if __name__ == "__main__":
    main()