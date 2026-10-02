from .strategy import Strategy

class Context():
    """
    Принимает стратегию и ее вызывает
    """

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def press_left_click(self):
        self._strategy.press_left_click()

    def release_left_click(self):
        self._strategy.release_left_click()

    def press_right_click(self):
        self._strategy.press_right_click()

    def release_right_click(self):
        self._strategy.release_right_click()

    def offset_cursor(self, dx, dy):
        self._strategy.offset_cursor(dx, dy)