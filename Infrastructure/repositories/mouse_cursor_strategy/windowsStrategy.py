from .strategy import Strategy
import ctypes
import keyboard
import time

# Устанавливаем английскую раскладку при импорте
try:
    hkl = ctypes.windll.user32.LoadKeyboardLayoutW("00000409", 1)
    ctypes.windll.user32.ActivateKeyboardLayout(hkl, 0)
    print("Английская раскладка установлена")
except Exception as e:
    print(f"Не удалось установить английскую раскладку: {e}")

class WindowsStrategy(Strategy):
    # Словарь для маппинга имен клавиш к правильному формату keyboard
    KEY_MAPPING = {
        'ctrl': 'ctrl',
        'control': 'ctrl',
        'shift': 'shift',
        'alt': 'alt',
        'enter': 'enter',
        'return': 'enter',
        'space': 'space',
        'spacebar': 'space',
        'esc': 'esc',
        'escape': 'esc',
        'tab': 'tab',
        'backspace': 'backspace',
        'delete': 'delete',
        'del': 'delete',
        'insert': 'insert',
        'ins': 'insert',
        'home': 'home',
        'end': 'end',
        'pageup': 'page up',
        'pagedown': 'page down',
        'up': 'up',
        'down': 'down',
        'left': 'left',
        'right': 'right',
        'f1': 'f1',
        'f2': 'f2',
        'f3': 'f3',
        'f4': 'f4',
        'f5': 'f5',
        'f6': 'f6',
        'f7': 'f7',
        'f8': 'f8',
        'f9': 'f9',
        'f10': 'f10',
        'f11': 'f11',
        'f12': 'f12',
        'win': 'win',
        'windows': 'win',
        'cmd': 'cmd',
        'command': 'cmd',
        'capslock': 'caps lock',
        'numlock': 'num lock',
        'scrolllock': 'scroll lock',
        'printscreen': 'print screen',
        'prtsc': 'print screen',
        'pause': 'pause',
        'break': 'pause',
        'context': 'menu',  # клавиша контекстного меню
    }
    
    def __init__(self):
        super().__init__()
        self._ensure_english_layout()
    
    def _ensure_english_layout(self):
        """Дополнительная проверка английской раскладки"""
        try:
            # Проверяем текущую раскладку
            current_layout = ctypes.windll.user32.GetKeyboardLayout(0)
            # 0x409 - английская раскладка (США)
            if current_layout != 0x409:
                hkl = ctypes.windll.user32.LoadKeyboardLayoutW("00000409", 1)
                ctypes.windll.user32.ActivateKeyboardLayout(hkl, 0)
                print("Английская раскладка активирована")
        except Exception as e:
            print(f"Ошибка при проверке раскладки: {e}")
    
    def _normalize_key_name(self, name: str) -> str:
        """Нормализует имя клавиши для библиотеки keyboard"""
        if len(name) > 1:
            return name
        
        russian_to_english = {
            'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 
            'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 
            'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 
            'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 
            'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.',
            'ё': '`',
            # Заглавные буквы
            'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U',
            'Ш': 'I', 'Щ': 'O', 'З': 'P', 'Х': '{', 'Ъ': '}', 'Ф': 'A', 'Ы': 'S',
            'В': 'D', 'А': 'F', 'П': 'G', 'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L',
            'Ж': ':', 'Э': '"', 'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B',
            'Т': 'N', 'Ь': 'M', 'Б': '<', 'Ю': '>',
            'Ё': '~'
        }
        return russian_to_english.get(name, name)
    
    def _normalize_single_key(self, key: str) -> str:
        """Нормализует одиночную клавишу"""
        # Если это специальная клавиша
        if key in self.KEY_MAPPING:
            return self.KEY_MAPPING[key]
        
        # Если это одиночный символ (буква, цифра)
        if len(key) == 1:
            return key
        
        # Попробуем добавить поддержку цифрового блока
        if key.startswith('num'):
            return key.replace('num', 'numpad ')
        
        # Возвращаем как есть (keyboard может поддерживать)
        return key
    
    def press_button_down_by_name(self, name: str) -> None:
        """Нажимает клавишу (удерживает)"""
        try:
            normalized_name = self._normalize_key_name(name)
            
            keyboard.press(normalized_name)
            print(f"Клавиша нажата: '{name}' -> '{normalized_name}'")
        except Exception as e:
            print(f"Ошибка при нажатии клавиши '{name}': {e}")
            raise
    
    def press_button_up_by_name(self, name: str) -> None:
        """Отпускает клавишу"""
        try:
            normalized_name = self._normalize_key_name(name)
            keyboard.release(normalized_name)
            print(f"Клавиша отпущена: '{name}' -> '{normalized_name}'")
        except Exception as e:
            print(f"Ошибка при отпускании клавиши '{name}': {e}")
            raise
    
    def press_button_by_name(self, name: str, delay: float = 0.1) -> None:
        """Нажимает и отпускает клавишу с задержкой"""
        self.press_button_down_by_name(name)
        time.sleep(delay)
        self.press_button_up_by_name(name)
    
    def press_hotkey(self, *keys: str, delay: float = 0.1) -> None:
        """Нажимает комбинацию клавиш (горячие клавиши)"""
        try:
            normalized_keys = [self._normalize_key_name(k) for k in keys]
            keyboard.press(*normalized_keys)
            time.sleep(delay)
            keyboard.release(*normalized_keys)
            print(f"Горячая клавиша нажата: {'+'.join(keys)}")
        except Exception as e:
            print(f"Ошибка при нажатии горячей клавиши {'+'.join(keys)}: {e}")
            raise
    
    def write_text(self, text: str, delay: float = 0.01) -> None:
        """Печатает текст с задержкой между символами"""
        try:
            # Убедимся, что раскладка английская
            self._ensure_english_layout()
            
            for char in text:
                keyboard.write(char)
                time.sleep(delay)
            print(f"Текст напечатан: '{text}'")
        except Exception as e:
            print(f"Ошибка при печати текста: {e}")
            raise