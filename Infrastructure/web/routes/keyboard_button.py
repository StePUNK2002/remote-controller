from fastapi import APIRouter, HTTPException
from containers.container import Container
from entities.keyboard_button import KeyboardButtonEntity
from urllib.parse import unquote

router = APIRouter()
container = Container()

@router.post(
    "/down_by_name",
    summary="Нажать кнопку по ее названию",
    response_model=KeyboardButtonEntity,
    status_code=200
)
async def press_button_down_by_name(button_name: str):
    use_case = container.press_button_down_by_name_use_case()
    result = use_case.execute(button_name)
    return result

@router.post(
    "/up_by_name",
    summary="Отпустить кнопку по ее названию",
    response_model=KeyboardButtonEntity,
    status_code=200
)
async def press_button_up_by_name(button_name: str):
    use_case = container.press_button_up_by_name_use_case()
    result = use_case.execute(button_name)
    return result


@router.post(
    "/press_and_release",
    summary="Нажать и отпустить кнопку",
    response_model=KeyboardButtonEntity,
    status_code=200
)
async def press_and_release(button_name: str):
    print(button_name)
    press_button_down_by_name_use_case = container.press_button_down_by_name_use_case()
    press_button_up_by_name_use_case = container.press_button_up_by_name_use_case()
    result = press_button_down_by_name_use_case.execute(button_name)
    result = press_button_up_by_name_use_case.execute(button_name)
    return result