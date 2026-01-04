from pydantic import BaseModel


class KeyboardButtonEntity(BaseModel):
    button_name: str