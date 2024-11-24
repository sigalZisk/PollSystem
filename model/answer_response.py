from typing import Optional

from pydantic import BaseModel

from model.option import Option
from model.question import Question


class AnswerResponse(BaseModel):
    id: Optional[int] = None
    user_id: int
    question: Question
    option: Option
