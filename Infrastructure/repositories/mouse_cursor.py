from Infrastructure.repositories.mouse_strategy.context import Context
from Infrastructure.repositories.mouse_strategy.windowsStrategy import WindowsStrategy
from Infrastructure.repositories.mouse_strategy.MacOSStrategy import MacOSStrategy
from entities.mouse_cursor import MouseCursorEntity, OffsetMouseCursorEntity
from interface.mouse_cursor import IMouseCursorRepository
import pyautogui
from pynput.mouse import Controller, Button
import platform


class MouseCursorRepositoryImpl(IMouseCursorRepository):
    def __init__(self):
        self.mouse = Controller()
        self._strategys = {
            "Windows": WindowsStrategy,
            "Darwin": MacOSStrategy
        }
        self._stategy_context = Context(self._strategys[platform.system()]())
    
    def get_current_position_cursor(self) -> MouseCursorEntity:
        x,y = pyautogui.position().x, pyautogui.position().y
        return MouseCursorEntity(axis_x=x, axis_y=y)
    
    def offset_position_cursor(self, offsetMouseCursor: OffsetMouseCursorEntity) -> OffsetMouseCursorEntity:
        dx = offsetMouseCursor.offset_axis_x
        dy = offsetMouseCursor.offset_axis_y
        self._stategy_context.offset_cursor(dx, dy)
        return OffsetMouseCursorEntity(offset_axis_x=offsetMouseCursor.offset_axis_x, offset_axis_y=offsetMouseCursor.offset_axis_y)
    
    def right_click_down(self) -> bool:
        try:
            self._stategy_context.press_right_click()
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False
    
    def right_click_up(self) -> bool:
        try:
            self._stategy_context.release_right_click()
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False
    
    def left_click_down(self) -> bool:
        try:
            self._stategy_context.press_left_click()
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False
    
    def left_click_up(self) -> bool:
        try:
            self._stategy_context.release_left_click()
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False
    
    def scroll_up(self) -> bool:
        try:
            self.mouse.scroll(0, 1)
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False

    def scroll_down(self) -> bool:
        try:
            self.mouse.scroll(0, -1)
            return True
        except Exception as e:
            print(f"Ошибка {e}")
            return False