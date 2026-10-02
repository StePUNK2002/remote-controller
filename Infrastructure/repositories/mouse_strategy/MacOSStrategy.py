from .strategy import Strategy
import pyautogui

class MacOSStrategy(Strategy):
    def press_left_click(self):
        pyautogui.mouseDown()

    def release_left_click(self):
        pyautogui.mouseUp()

    def press_right_click(self):
        pyautogui.mouseDown(button='right')

    def release_right_click(self):
        pyautogui.mouseUp(button='right')

    def offset_cursor(self, dx, dy):
        pyautogui.move(dx, dy)