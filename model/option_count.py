from pydantic import BaseModel


class OptionCount(BaseModel):
    option_id: int
    option_text: str
    count: int
