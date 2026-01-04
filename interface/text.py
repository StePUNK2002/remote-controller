from entities.text import Text
from abc import ABC, abstractmethod



class ITextRepository(ABC):
    @abstractmethod
    def print_text(text: str) -> str:
        pass

    @abstractmethod
    def reverse_text(text: Text) -> Text:
        pass