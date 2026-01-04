from .strategy import Strategy
import pyautogui

class MacOSStrategy(Strategy):
    def press_button_down_by_name(self, name: str) -> None:
        pyautogui.keyDown(name)
    
    def press_button_up_by_name(self, name: str):
        pyautogui.keyUp(name)
        