from entities.mouse_cursor import MouseCursorEntity, OffsetMouseCursorEntity
from interface.mouse_cursor import IMouseCursorRepository
import pyautogui
from pynput.mouse import Controller, Button


class MouseCursorRepositoryImpl(IMouseCursorRepository):
    def __init__(self):
        self.mouse = Controller()
    
    def get_current_position_cursor(self) -> MouseCursorEntity:
        x,y = pyautogui.position().x, pyautogui.position().y
        return MouseCursorEntity(axis_x=x, axis_y=y)
    
    def offset_position_cursor(self, offsetMouseCursor: OffsetMouseCursorEntity) -> OffsetMouseCursorEntity:
        self.mouse.move(offsetMouseCursor.offset_axis_x, offsetMouseCursor.offset_axis_y)
        return OffsetMouseCursorEntity(offset_axis_x=offsetMouseCursor.offset_axis_x, offset_axis_y=offsetMouseCursor.offset_axis_y)
    
    def right_click_down(self) -> bool:
        try:
            pyautogui.mouseDown(button='right')
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False
    
    def right_click_up(self) -> bool:
        try:
            pyautogui.mouseUp(button='right')
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False
    
    def left_click_down(self) -> bool:
        try:
            pyautogui.mouseDown()
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False
    
    def left_click_up(self) -> bool:
        try:
            pyautogui.mouseUp()
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False
    
    def scroll_up(self) -> bool:
        try:
            self.mouse.scroll(0, 3)
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False

    def scroll_down(self) -> bool:
        try:
            self.mouse.scroll(0, -3)
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False