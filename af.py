import win32gui, win32con
import pywinauto
import time

time.sleep(4.5)

hwnd = win32gui.GetForegroundWindow()
hwnd = win32gui.GetWindow(hwnd, win32con.GW_CHILD)

app = pywinauto.application.Application().connect(handle=hwnd)

time.sleep(0.5)

while(True):
    # app.window().send_keystrokes("4")
    # time.sleep(0.5)
    app.window().send_keystrokes("3")
    time.sleep(0.3)
    app.window().send_keystrokes("2")
    time.sleep(0.3)