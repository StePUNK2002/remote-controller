import ctypes
import time
from ctypes import wintypes

import win32api

from .strategy import Strategy

# --- DPI awareness: должен быть выставлен как можно раньше -------------------
try:
    ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))  # per-monitor v2
except Exception:
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        pass

# Английская раскладка
win32api.LoadKeyboardLayout("00000409", 1)

# Не давать системе засыпать (ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

user32 = ctypes.WinDLL('user32', use_last_error=True)

# --- SendInput ---------------------------------------------------------------

INPUT_MOUSE = 0

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_WHEEL = 0x0800
MOUSEEVENTF_VIRTUALDESK = 0x4000
MOUSEEVENTF_ABSOLUTE = 0x8000

SM_XVIRTUALSCREEN = 76
SM_YVIRTUALSCREEN = 77
SM_CXVIRTUALSCREEN = 78
SM_CYVIRTUALSCREEN = 79

WHEEL_DELTA = 120


class MOUSEINPUT(ctypes.Structure):
    _fields_ = (
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.c_size_t),
    )


class INPUT(ctypes.Structure):
    class _I(ctypes.Union):
        _fields_ = (("mi", MOUSEINPUT),)

    _anonymous_ = ("i",)
    _fields_ = (("type", wintypes.DWORD), ("i", _I))


user32.SendInput.argtypes = (wintypes.UINT, ctypes.POINTER(INPUT), ctypes.c_int)
user32.SendInput.restype = wintypes.UINT


def _send(flags, dx=0, dy=0, mouse_data=0):
    inp = INPUT(
        type=INPUT_MOUSE,
        mi=MOUSEINPUT(dx, dy, mouse_data & 0xFFFFFFFF, flags, 0, 0),
    )
    if user32.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT)) != 1:
        raise ctypes.WinError(ctypes.get_last_error())


def _cursor_pos():
    pt = wintypes.POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y


def _virtual_screen():
    return (
        user32.GetSystemMetrics(SM_XVIRTUALSCREEN),
        user32.GetSystemMetrics(SM_YVIRTUALSCREEN),
        user32.GetSystemMetrics(SM_CXVIRTUALSCREEN),
        user32.GetSystemMetrics(SM_CYVIRTUALSCREEN),
    )
    


def _abs_move(x, y):
    """Точное перемещение в пиксели (x, y) настоящим событием мыши, без ускорения."""
    left, top, w, h = _virtual_screen()
    x = min(max(int(x), left), left + w - 1)
    y = min(max(int(y), top), top + h - 1)
    # ceil((x - left) * 65536 / w): так пиксель после преобразования совпадёт с x
    nx = -(-((x - left) * 65536) // w)
    ny = -(-((y - top) * 65536) // h)
    _send(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_VIRTUALDESK, nx, ny)


# --- Стратегия ---------------------------------------------------------------

class WindowsStrategy(Strategy):
    HOVER_SETTLE = 0.03   # пауза после «оживляющего» перемещения перед DOWN
    MIN_HOLD = 0.04       # минимальное удержание кнопки (для быстрых кликов)

    def __init__(self):
        super().__init__()
        self._down_time = {"left": 0.0, "right": 0.0}

    # --- позиция и перемещение (всё через один путь ввода) -------------------
    def get_position(self):
        return _cursor_pos()

    def move_to(self, x, y):
        _abs_move(x, y)

    def move_relative(self, dx, dy):
        x, y = _cursor_pos()
        _abs_move(x + dx, y + dy)

    def scroll(self, notches):
        """notches > 0 вверх, < 0 вниз."""
        _send(MOUSEEVENTF_WHEEL, mouse_data=int(notches) * WHEEL_DELTA)

    def offset_cursor(self, dx, dy):          # <- 4 пробела, внутри класса
        _send(MOUSEEVENTF_MOVE, int(dx), int(dy))

    # --- кнопки ---------------------------------------------------------------
    def _wake_hover(self):
        # Настоящие события MOVE, чтобы элемент под курсором перешёл в hover.
        # Возвращаемся точно в ту же точку (абсолютные координаты, дрейфа нет).
        x, y = _cursor_pos()
        left, _, w, _ = _virtual_screen()
        step = -1 if x >= left + w - 1 else 1
        _abs_move(x + step, y)
        _abs_move(x, y)
        time.sleep(self.HOVER_SETTLE)

    def _press(self, name, down_flag):
        self._wake_hover()
        _send(down_flag)
        self._down_time[name] = time.monotonic()

    def _release(self, name, up_flag):
        elapsed = time.monotonic() - self._down_time[name]
        if elapsed < self.MIN_HOLD:
            time.sleep(self.MIN_HOLD - elapsed)
        _send(up_flag)

    def press_left_click(self):
        self._press("left", MOUSEEVENTF_LEFTDOWN)

    def release_left_click(self):
        self._release("left", MOUSEEVENTF_LEFTUP)

    def press_right_click(self):
        self._press("right", MOUSEEVENTF_RIGHTDOWN)

    def release_right_click(self):
        self._release("right", MOUSEEVENTF_RIGHTUP)

    # Блокировка экрана без кликов
    def lock_screen(self):
        user32.LockWorkStation()