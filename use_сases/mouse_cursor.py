from entities.mouse_cursor import MouseCursorEntity, OffsetMouseCursorEntity
from services.mouse_cursor import MouseCursorService


class MouseCursorUseCase:
    def __init__(self, mouse_cursor_service: MouseCursorService):
        self.mouse_cursor_service = mouse_cursor_service

class GetCurrentPositionCursorUseCase(MouseCursorUseCase):
    def execute(self) -> MouseCursorEntity:
        return self.mouse_cursor_service.get_current_position_cursor()
    
class OffSetPositionCursorUseCase(MouseCursorUseCase):
    def execute(self, offsetMouseCursor: OffsetMouseCursorEntity) -> OffsetMouseCursorEntity:
        return self.mouse_cursor_service.offset_position_cursor(offsetMouseCursor)

class RightClickDownUseCase(MouseCursorUseCase):
    def execute(self) -> bool:
        return self.mouse_cursor_service.right_click_down()

class RightClickUpUseCase(MouseCursorUseCase):
    def execute(self) -> bool:
        return self.mouse_cursor_service.right_click_up()
    
class LeftClickDownUseCase(MouseCursorUseCase):
    def execute(self) -> bool:
        return self.mouse_cursor_service.left_click_down()

class LeftClickUpUseCase(MouseCursorUseCase):
    def execute(self) -> bool:
        return self.mouse_cursor_service.left_click_up()

class ScrollUpUseCase(MouseCursorUseCase):
    def execute(self) -> bool:
        return self.mouse_cursor_service.scroll_up()

class ScrollDownUseCase(MouseCursorUseCase):
    def execute(self) -> bool:
        return self.mouse_cursor_service.scroll_down()