from typing import List, Optional

from pydantic import BaseModel

from model.option import Option


class FullQuestion(BaseModel):
    question_id: Optional[int] = None
    title: str
    options: List[Option]
