from typing import List

from pydantic import BaseModel

from model.option_count import OptionCount


class QuestionOptionDistribution(BaseModel):
    question_id: int
    option_distribution: List[OptionCount]
