from fastapi import APIRouter, HTTPException
from containers.container import Container
from entities.mouse_cursor import MouseCursorEntity, OffsetMouseCursorEntity

router = APIRouter()
container = Container()

@router.post(
    "/offset",
    summary="Переместить курсор мыши на установленные значения",
    response_model=OffsetMouseCursorEntity,
    status_code=200
    
)
async def mouse_offset(entity: OffsetMouseCursorEntity):
    use_case = container.off_set_position_cursor_use_case()
    result = use_case.execute(entity)
    return result

@router.post(
    "/scroll_up",
    summary="Скролить вверх",
    response_model=bool,
    status_code=200
    
)
async def scroll_up_use_case():
    use_case = container.scroll_up_use_case()
    result = use_case.execute()
    return result

@router.post(
    "/scroll_down",
    summary="Скролить вниз",
    response_model=bool,
    status_code=200
    
)
async def scroll_down_use_case():
    use_case = container.scroll_down_use_case()
    result = use_case.execute()
    return result


@router.post(
    "/click_down",
    summary="Зажать левую кнопку мыши",
    response_model=bool,
    status_code=200
    
)
async def left_click_down_use_case():
    use_case = container.left_click_down_use_case()
    result = use_case.execute()
    return result

@router.post(
    "/click_up",
    summary="Отпустить левую кнопку мыши",
    response_model=bool,
    status_code=200
    
)
async def left_click_up_use_case():
    use_case = container.left_click_up_use_case()
    result = use_case.execute()
    return result


@router.post(
    "/right_click",
    summary="Выполнить правый клик",
    response_model=bool,
    status_code=200
    
)
async def right_click():
    right_click_down_down_use_case = container.right_click_down_down_use_case()
    right_click_up_use_case = container.right_click_up_use_case()
    result = right_click_down_down_use_case.execute()
    result = right_click_up_use_case.execute()
    return result