import multiprocessing
import cv2
import mss
import numpy as np
import time
import pyautogui
import win32gui, win32con
import pywinauto

time.sleep(5)

hwnd = win32gui.GetForegroundWindow()
hwnd = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
app = pywinauto.application.Application().connect(handle=hwnd)

ndl_1 = cv2.imread(r'img/1.jpg', cv2.IMREAD_UNCHANGED)
ndl_2 = cv2.imread(r'img/2.jpg', cv2.IMREAD_UNCHANGED)
ndl_3 = cv2.imread(r'img/3.jpg', cv2.IMREAD_UNCHANGED)
ndl_4 = cv2.imread(r'img/4.jpg', cv2.IMREAD_UNCHANGED)
ndl_5 = cv2.imread(r'img/5.jpg', cv2.IMREAD_UNCHANGED)
ndl_6 = cv2.imread(r'img/6.jpg', cv2.IMREAD_UNCHANGED)
ndl_7 = cv2.imread(r'img/7.jpg', cv2.IMREAD_UNCHANGED)
ndl_8 = cv2.imread(r'img/8.jpg', cv2.IMREAD_UNCHANGED)
ndl_9 = cv2.imread(r'img/9.jpg', cv2.IMREAD_UNCHANGED)
ndl_10 = cv2.imread(r'img/10.jpg', cv2.IMREAD_UNCHANGED)
last_ndl = cv2.imread(r'img/lastdrop.jpg', cv2.IMREAD_UNCHANGED)


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


def drag_click(strt, stp):
    pyautogui.moveTo(strt[0], strt[1])
    time.sleep(0.5)
    pyautogui.dragTo(stp[0], stp[1], button='left', duration=1)
    time.sleep(1)


def bail_out(loc):
    list_loc = {
        'time_space' : (113, 711),
        'citadel' : (1494, 914),
        'ggwest' : (102, 915),
        'mudluk' : (1527, 912),
        'aqlesson' : (1816, 922),
        'necro_cav' : (1202, 914),
        'hachiko' : (107, 96),
        'time_void' : (800, 923),
        'dragon' : (1016, 76),
        'maul' : (1118, 917)
    }
    pyautogui.click(list_loc[loc][0], list_loc[loc][1], 1, button='left')
    time.sleep(2)
    app.window().send_keystrokes("y")
    time.sleep(5)


def turn_in_quest():
    pyautogui.click(270, 292, 1, button='left') # quest
    time.sleep(1.5)
    pyautogui.click(430, 820, 1, button='left') # turn in
    time.sleep(1.5)
    return


def skill_auto():
    while(True):
        app.window().send_keystrokes("2")
        time.sleep(0.5)
        app.window().send_keystrokes("3")
        time.sleep(0.5)


def temp_match(coord, ndl):
    tmp_bool = False
    threshold = .90

    while(not tmp_bool):
        hy = take_ss(coord[0], coord[1], coord[2], coord[3])
        result = cv2.matchTemplate(hy, ndl, cv2.TM_CCOEFF_NORMED)

        target = np.where(result >= threshold)

        if(len(target[0]) > 0):
            tmp_bool = True
        time.sleep(1)


def fast_travel(loc):
    list_loc = {
        'time_space' : (763, 615),
        'citadel' : (1066, 615),
        'ggwest' : (1355, 400),
        'mudluk' : (1355, 475),
        'aqlesson' : (1355, 550),
        'necro_cav' : (1355, 625),
        'hachiko' : (1655, 400),
        'time_void' : (1655, 475),
        'dragon' : (1655, 550),
        'maul' : (1655, 625)
    }

    pyautogui.click(455, 614, button='left')
    time.sleep(0.5)
    pyautogui.click(955, 704, button='left')
    time.sleep(0.5)
    pyautogui.click(list_loc[loc][0], list_loc[loc][1], button='left')
    time.sleep(5)

'''

Each map operation starts from here

'''

def time_space():
    fast_travel('time_space')
    pyautogui.click(1803, 225, 1, button='left') # This is a special case
    time.sleep(3)

    p1 = multiprocessing.Process(target=temp_match, args=[(1711, 71, 80, 27), ndl_1])
    p2 = multiprocessing.Process(target=skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()


def citadel():
    fast_travel('citadel')

    p1 = multiprocessing.Process(target=temp_match, args=[(1680, 101, 80, 27), ndl_2])
    p2 = multiprocessing.Process(target=skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()


def ggwest():
    fast_travel('ggwest')

    p1 = multiprocessing.Process(target=temp_match, args=[(1646, 125, 86, 30), ndl_3])
    p2 = multiprocessing.Process(target=skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()


def mudluk():
    fast_travel('mudluk')

    p1 = multiprocessing.Process(target=temp_match, args=[(1642, 156, 80, 27), ndl_4])
    p2 = multiprocessing.Process(target=skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()
    


def aqlesson():
    fast_travel('aqlesson')

    p1 = multiprocessing.Process(target=temp_match, args=[(1597, 180, 86, 30), ndl_5])
    p2 = multiprocessing.Process(target=skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()
    


def necro_cav():
    fast_travel('necro_cav')

    p1 = multiprocessing.Process(target=temp_match, args=[(1673, 81, 80, 27), ndl_6])
    p2 = multiprocessing.Process(target=skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()
    


def hachiko():
    fast_travel('hachiko')

    p1 = multiprocessing.Process(target=temp_match, args=[(1627, 107, 80, 27), ndl_7])
    p2 = multiprocessing.Process(target=skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()


def time_void():
    fast_travel('time_void')

    p1 = multiprocessing.Process(target=temp_match, args=[(1690, 136, 80, 27), ndl_8])
    p2 = multiprocessing.Process(target=skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()


def dragon():
    fast_travel('dragon')
    # Special case
    pyautogui.click(960, 468, 1, button='left')
    time.sleep(2)
    pyautogui.click(586, 401, 1, button='left')
    time.sleep(1)
    pyautogui.click(1093, 775, 1, button='left')
    time.sleep(1)
    pyautogui.click(1041, 685, 1, button='left')
    time.sleep(1)


    p1 = multiprocessing.Process(target=temp_match, args=[(1648, 163, 80, 27), ndl_9])
    p2 = multiprocessing.Process(target=skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()


def maul():
    p1 = multiprocessing.Process(target=temp_match, args=[(1699, 190, 80, 27), ndl_10])
    p2 = multiprocessing.Process(target=skill_auto)

    p2.daemon = True
    
    p1.start()
    p2.start()

    p1.join()

    p3 = multiprocessing.Process(target=temp_match, args=[(770, 655, 385, 260), last_ndl])

    p3.start()

    p3.join()
    p2.terminate()
    

def main():
    while(True):
        drag_click((1798, 110), (1798, 130))

        time_space()
        time.sleep(1)
        drag_click((1713, 79), (1718, 79)) #reset
        time.sleep(1)
        bail_out('time_space')

        citadel()
        bail_out('citadel')

        ggwest()
        bail_out('ggwest')

        mudluk()
        bail_out('mudluk')

        aqlesson()
        bail_out('aqlesson')

        drag_click((1798, 125), (1798, 295))

        necro_cav()
        bail_out('necro_cav')

        hachiko()
        bail_out('hachiko')

        time_void()
        bail_out('time_void')

        dragon()
        bail_out('dragon')

        # Special case
        fast_travel('maul')
        app.window().send_keystrokes("c")

        for _ in range(4):
            maul()
            turn_in_quest()

        time.sleep(1)
        drag_click((1713, 79), (1750, 79)) # reset
        time.sleep(1)
        bail_out('maul')

        drag_click((1798, 202), (1798, 82))


if __name__ == '__main__':
    main()