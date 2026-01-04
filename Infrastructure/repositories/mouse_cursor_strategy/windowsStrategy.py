from .strategy import Strategy
import ctypes
hkl = ctypes.windll.user32.LoadKeyboardLayoutW("00000409", 1)
ctypes.windll.user32.ActivateKeyboardLayout(hkl, 0)
import keyboard

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
    }
    
    def _normalize_key_name(self, name: str) -> str:
        """Нормализует имя клавиши для библиотеки keyboard"""
        name_lower = name.lower().strip()
        
        # Проверяем маппинг специальных клавиш
        if name_lower in self.KEY_MAPPING:
            return self.KEY_MAPPING[name_lower]
        
        # Для букв и цифр возвращаем как есть (в нижнем регистре)
        if len(name) == 1:
            return name_lower
        
        # Если не нашли, возвращаем оригинальное имя (может вызвать ошибку в keyboard)
        return name
    
    def press_button_down_by_name(self, name: str) -> None:
        """Нажимает клавишу (удерживает)"""
        try:
            normalized_name = self._normalize_key_name(name)
            keyboard.press(normalized_name)
            print(f"Клавиша нажата: {name} -> {normalized_name}")
        except Exception as e:
            print(f"Ошибка при нажатии клавиши '{name}': {e}")
            # Можно выбросить исключение дальше или обработать иначе
            raise
    
    def press_button_up_by_name(self, name: str) -> None:
        """Отпускает клавишу"""
        try:
            normalized_name = self._normalize_key_name(name)
            keyboard.release(normalized_name)
            print(f"Клавиша отпущена: {name} -> {normalized_name}")
        except Exception as e:
            print(f"Ошибка при отпускании клавиши '{name}': {e}")
            raise
    
    def press_button_by_name(self, name: str, delay: float = 0.1) -> None:
        """Нажимает и отпускает клавишу с задержкой"""
        self.press_button_down_by_name(name)
        import time
        time.sleep(delay)
        self.press_button_up_by_name(name)
    