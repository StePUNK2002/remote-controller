from entities.keyboard_button import KeyboardButtonEntity
from interface.keyboard_button import IKeyboardButtonRepository


class KeyboardButtonService:
    def __init__(self, keyboard_button_repository: IKeyboardButtonRepository):
        self.keyboard_button_repository = keyboard_button_repository
    
    def press_button_down_by_name(self, name: str) -> KeyboardButtonEntity:
        return self.keyboard_button_repository.press_button_down_by_name(name)
    
    def press_button_up_by_name(self, name: str) -> KeyboardButtonEntity:
        return self.keyboard_button_repository.press_button_up_by_name(name)