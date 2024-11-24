from pydantic import BaseModel

class UserAnswersCount(BaseModel):
    user_id: int
    answers_count: int
