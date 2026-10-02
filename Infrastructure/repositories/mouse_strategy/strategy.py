from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def press_left_click(self):
        pass

    @abstractmethod
    def release_left_click(self):
        pass

    @abstractmethod
    def press_right_click(self):
        pass

    @abstractmethod
    def release_right_click(self):
        pass

    @abstractmethod
    def offset_cursor(self, dx, dy):
        pass