from .strategy import Strategy
import ctypes
from ctypes import wintypes

WM_INPUTLANGCHANGEREQUEST = 0x0050
INPUTLANGCHANGE_FORWARD = 0x0002
INPUTLANGCHANGE_BACKWARD = 0x0004

user32 = ctypes.WinDLL('user32', use_last_error=True)
hwnd = user32.GetForegroundWindow()
hkl = user32.LoadKeyboardLayoutW("00000409", 0x00000001)
user32.ActivateKeyboardLayout(hkl, 0)
user32.PostMessageW(
        hwnd,
        WM_INPUTLANGCHANGEREQUEST,
        0,
        hkl
    )

import pyautogui

class WindowsStrategy(Strategy):
    def press_button_down_by_name(self, name: str) -> None:
        pyautogui.keyDown(name)
    
    def press_button_up_by_name(self, name: str):
        pyautogui.keyUp(name)