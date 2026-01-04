from .strategy import Strategy
import keyboard

class WindowsStrategy(Strategy):
    def press_button_down_by_name(self, name: str) -> None:
        scan_code = keyboard.key_to_scan_codes(name)
        keyboard.press(scan_code)
    
    def press_button_up_by_name(self, name: str):
        scan_code = keyboard.key_to_scan_codes(name)
        keyboard.release(scan_code)