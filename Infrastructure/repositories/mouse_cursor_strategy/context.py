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

    def press_button_down_by_name(self, name: str) -> None:
        self._strategy.press_button_down_by_name(name)
    
    def press_button_up_by_name(self, name: str):
        self._strategy.press_button_up_by_name(name)