from typing import Optional

from pydantic import BaseModel

class Option(BaseModel):
    id: Optional[int] = None
    question_id: int
    text: str
