from entities.text import Text
from interface.text import ITextRepository


class TextService:
    def __init__(self, text_repository: ITextRepository):
        self.text_repository = text_repository
    

    def print_text(self, text: str) -> str:
        """
        Печать текста в консоли
        """
        return self.text_repository.print_text(text)
    
    def reverse_text(self, text: Text) -> Text:
        """
        Переворачиваем текст с использованием сущности
        """
        return self.text_repository.reverse_text(text)