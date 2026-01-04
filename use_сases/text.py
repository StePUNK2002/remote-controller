from entities.text import Text
from services.text import TextService


class TextUseCase:
    def __init__(self, text_service: TextService):
        self.text_service = text_service
    
class PrintTextUseCase(TextUseCase):
    def execute(self, text: str) -> str:
        return self.text_service.print_text(text)
    
class ReverseTextUseCase(TextUseCase):
    def execute(self, text: Text) -> Text:
        return self.text_service.reverse_text(text)