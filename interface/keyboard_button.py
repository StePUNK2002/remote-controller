from entities.keyboard_button import KeyboardButtonEntity
from abc import ABC, abstractmethod


class IKeyboardButtonRepository(ABC):

    @abstractmethod
    def press_button_down_by_name(name: str) -> KeyboardButtonEntity:
        pass

    @abstractmethod
    def press_button_up_by_name(name: str) -> KeyboardButtonEntity:
        pass