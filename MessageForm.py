from pydantic import BaseModel

class MessageForm(BaseModel):
    message: str | None = None