from entities.keyboard_button import KeyboardButtonEntity
from services.keyboard_button import KeyboardButtonService


class KeyboardButtonUseCase:
    def __init__(self, keyboard_button_service: KeyboardButtonService):
        self.keyboard_button_service = keyboard_button_service

class PressButtonDownByNameUseCase(KeyboardButtonUseCase):
    def execute(self, name: str) -> KeyboardButtonEntity:
        return self.keyboard_button_service.press_button_down_by_name(name)

class PressButtonUpByNameUseCase(KeyboardButtonUseCase):
    def execute(self, name: str) -> KeyboardButtonEntity:
        return self.keyboard_button_service.press_button_up_by_name(name)