import win32gui, win32con
import pywinauto
import time

time.sleep(3)

hwnd = win32gui.GetForegroundWindow()
hwnd = win32gui.GetWindow(hwnd, win32con.GW_CHILD)

app = pywinauto.application.Application().connect(handle=hwnd)

while(True):
    app.window().send_keystrokes("2")
    app.window().send_keystrokes("3")
    app.window().send_keystrokes("4")
    app.window().send_keystrokes("5")
    app.window().send_keystrokes("1")
