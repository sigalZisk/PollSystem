from pydantic import BaseModel

class Answer(BaseModel):
    id: int
    user_id: int
    question_id: int
    option_id: int
