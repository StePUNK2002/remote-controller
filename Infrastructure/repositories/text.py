from entities.text import Text
from interface.text import ITextRepository


class TextRepositoryImpl(ITextRepository):
    def __init__(self):
        ...
    
    def print_text(self, text: str) -> str:
        return text
    
    def reverse_text(self, text: Text) -> Text:
        return text.text[::-1]