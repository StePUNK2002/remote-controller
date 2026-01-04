from entities.mouse_cursor import MouseCursorEntity, OffsetMouseCursorEntity
from interface.mouse_cursor import IMouseCursorRepository


class MouseCursorService:
    def __init__(self, mouse_cursor_repository: IMouseCursorRepository):
        self.mouse_cursor_repository = mouse_cursor_repository
    
    def get_current_position_cursor(self) -> MouseCursorEntity:
        return self.mouse_cursor_repository.get_current_position_cursor()
    
    def offset_position_cursor(self, offsetMouseCursor: OffsetMouseCursorEntity) -> OffsetMouseCursorEntity:
        return self.mouse_cursor_repository.offset_position_cursor(offsetMouseCursor)

    def right_click_down(self) -> bool:
        return self.mouse_cursor_repository.right_click_down()
    
    def right_click_up(self) -> bool:
        return self.mouse_cursor_repository.right_click_up()
    
    def left_click_down(self) -> bool:
        return self.mouse_cursor_repository.left_click_down()
    
    def left_click_up(self) -> bool:
        return self.mouse_cursor_repository.left_click_up()
    