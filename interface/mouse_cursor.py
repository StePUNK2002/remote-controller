from entities.mouse_cursor import MouseCursorEntity, OffsetMouseCursorEntity
from abc import ABC, abstractmethod


class IMouseCursorRepository(ABC):

    @abstractmethod
    def get_current_position_cursor() -> MouseCursorEntity:
        pass

    @abstractmethod
    def offset_position_cursor(offsetMouseCursor: OffsetMouseCursorEntity) -> MouseCursorEntity:
        pass

    @abstractmethod
    def right_click_down() -> bool:
        pass

    @abstractmethod
    def right_click_up() -> bool:
        pass

    @abstractmethod
    def left_click_down() -> bool:
        pass
    
    @abstractmethod
    def left_click_up() -> bool:
        pass

    @abstractmethod
    def scroll_up() -> bool:
        pass

    @abstractmethod
    def scroll_down() -> bool:
        pass