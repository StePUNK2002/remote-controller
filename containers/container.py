from dependency_injector import containers, providers
from Infrastructure.repositories.keyboard_button import KeyboardButtonRepositoryImpl
from Infrastructure.repositories.text import TextRepositoryImpl
from services.keyboard_button import KeyboardButtonService
from services.text import TextService
from use_сases.keyboard_button import PressButtonDownByNameUseCase, PressButtonUpByNameUseCase
from use_сases.text import PrintTextUseCase, ReverseTextUseCase
from Infrastructure.repositories.mouse_cursor import MouseCursorRepositoryImpl
from services.mouse_cursor import MouseCursorService
from use_сases.mouse_cursor import GetCurrentPositionCursorUseCase, LeftClickDownUseCase, LeftClickUpUseCase, OffSetPositionCursorUseCase, RightClickDownUseCase, RightClickUpUseCase, ScrollDownUseCase, ScrollUpUseCase


class Container(containers.DeclarativeContainer):
    
    text_repository = providers.Singleton(
        TextRepositoryImpl
    )
    
    text_service = providers.Singleton(
        TextService,
        text_repository=text_repository
    )

    print_text_use_case = providers.Factory(
        PrintTextUseCase,
        text_service=text_service
    )

    reverse_text_use_case = providers.Factory(
        ReverseTextUseCase,
        text_service=text_service
    )

    mouse_cursor_repository = providers.Singleton(
        MouseCursorRepositoryImpl
    )
    
    mouse_cursor_service = providers.Singleton(
        MouseCursorService,
        mouse_cursor_repository=mouse_cursor_repository
    )
    
    get_current_position_cursor_use_case = providers.Factory(
        GetCurrentPositionCursorUseCase,
        mouse_cursor_service=mouse_cursor_service 
    )
    
    off_set_position_cursor_use_case = providers.Factory(
        OffSetPositionCursorUseCase,
        mouse_cursor_service=mouse_cursor_service 
    )
    
    right_click_down_down_use_case = providers.Factory(
        RightClickDownUseCase,
        mouse_cursor_service=mouse_cursor_service
    )

    right_click_up_use_case = providers.Factory(
        RightClickUpUseCase,
        mouse_cursor_service=mouse_cursor_service
    )
    
    left_click_down_use_case = providers.Factory(
        LeftClickDownUseCase,
        mouse_cursor_service=mouse_cursor_service
    )
    
    left_click_up_use_case = providers.Factory(
        LeftClickUpUseCase,
        mouse_cursor_service=mouse_cursor_service 
    )

    keyboard_button_repository = providers.Singleton(
        KeyboardButtonRepositoryImpl
    )

    keyboard_button_service = providers.Singleton(
        KeyboardButtonService,
        keyboard_button_repository=keyboard_button_repository
    )

    press_button_down_by_name_use_case = providers.Factory(
        PressButtonDownByNameUseCase,
        keyboard_button_service=keyboard_button_service
    )

    press_button_up_by_name_use_case = providers.Factory(
        PressButtonUpByNameUseCase,
        keyboard_button_service=keyboard_button_service
    )

    scroll_up_use_case = providers.Factory(
        ScrollUpUseCase,
        mouse_cursor_service=mouse_cursor_service
    )

    scroll_down_use_case = providers.Factory(
        ScrollDownUseCase,
        mouse_cursor_service=mouse_cursor_service
    )