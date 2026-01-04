from Infrastructure.repositories.mouse_cursor_strategy.MacOSStrategy import MacOSStrategy
from Infrastructure.repositories.mouse_cursor_strategy.context import Context
from Infrastructure.repositories.mouse_cursor_strategy.windowsStrategy import WindowsStrategy
from entities.keyboard_button import KeyboardButtonEntity
from interface.keyboard_button import IKeyboardButtonRepository
import platform

class KeyboardButtonRepositoryImpl(IKeyboardButtonRepository):
    def __init__(self):
        self._strategys = {
            "Windows": WindowsStrategy,
            "Darwin": MacOSStrategy
        }
        self._stategy_context = Context(self._strategys[platform.system()]())
    
    
    def press_button_down_by_name(self, name: str) -> KeyboardButtonEntity:
        self._stategy_context.press_button_down_by_name(name)
        
        return KeyboardButtonEntity(button_name=name) 
    
    def press_button_up_by_name(self, name: str) -> KeyboardButtonEntity:
        self._stategy_context.press_button_up_by_name(name)
        
        return KeyboardButtonEntity(button_name=name)   