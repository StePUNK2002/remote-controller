from fastapi import APIRouter
from Infrastructure.web.routes.keyboard_button import router as keyboard_button
from Infrastructure.web.routes.mouse_cursor import router as mouse_cursor
from Infrastructure.web.routes.main_page import router as main_page


api_router = APIRouter()
api_router.include_router(
    keyboard_button,
    prefix="/keyboard",
    tags=["Клавиатура"]
)
api_router.include_router(
    mouse_cursor,
    prefix="/mouse",
    tags=["Мышь"]
)
api_router.include_router(
    main_page,
    prefix="",
    tags=["Главная страница"]
)