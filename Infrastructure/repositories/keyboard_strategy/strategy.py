from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def press_button_down_by_name(self, name: str):
        pass

    @abstractmethod
    def press_button_up_by_name(self, name: str):
        pass