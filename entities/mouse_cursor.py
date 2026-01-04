from pydantic import BaseModel


class MouseCursorEntity(BaseModel):
    axis_x: int
    axis_y: int


class OffsetMouseCursorEntity(BaseModel):
    offset_axis_x: int
    offset_axis_y: int
