from Infrastructure.repositories.mouse_cursor_strategy.MacOSStrategy import MacOSStrategy
from Infrastructure.repositories.mouse_cursor_strategy.context import Context
from Infrastructure.repositories.mouse_cursor_strategy.windowsStrategy import WindowsStrategy
from entities.keyboard_button import KeyboardButtonEntity
from interface.keyboard_button import IKeyboardButtonRepository
import platform

class KeyboardButtonRepositoryImpl(IKeyboardButtonRepository):
    def __init__(self):
        # Маппинг русских символов на соответствующие английские клавиши
        self.russian_to_english_map = {
            'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u',
            'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's',
            'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l',
            'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b',
            'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', 'ё': '`',
            # Заглавные буквы
            'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U',
            'Ш': 'I', 'Щ': 'O', 'З': 'P', 'Х': '{', 'Ъ': '}', 'Ф': 'A', 'Ы': 'S',
            'В': 'D', 'А': 'F', 'П': 'G', 'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L',
            'Ж': ':', 'Э': '"', 'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B',
            'Т': 'N', 'Ь': 'M', 'Б': '<', 'Ю': '>', 'Ё': '~'
        }
        self._strategys = {
            "Windows": WindowsStrategy,
            "Darwin": MacOSStrategy
        }
        self._stategy_context = Context(self._strategys[platform.system()]())
    
    def _convert_to_english_key(self, name: str) -> str:
        """Конвертирует русский символ в соответствующую английскую клавишу."""
        if len(name) == 1 and name in self.russian_to_english_map:
            return self.russian_to_english_map[name]
        return name
    
    def press_button_down_by_name(self, name: str) -> KeyboardButtonEntity:
        # Конвертируем символ, если это русская буква
        converted_name = self._convert_to_english_key(name)
        
        self._stategy_context.press_button_down_by_name(converted_name)
        
        return KeyboardButtonEntity(button_name=name) 
    
    def press_button_up_by_name(self, name: str) -> KeyboardButtonEntity:
        converted_name = self._convert_to_english_key(name)

        self._stategy_context.press_button_up_by_name(converted_name)
        
        return KeyboardButtonEntity(button_name=name)   