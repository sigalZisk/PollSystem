from typing import List

from model.answer import Answer
from model.answer_response import AnswerResponse
from model.option_count import OptionCount
from model.question_options_distribution import QuestionOptionDistribution
from service import answer_service, option_service


async def get_answers_by_user_id(user_id: int) -> List[Answer]:
    return await answer_service.get_by_user_id(user_id)

async def get_answers_by_question_id(question_id: int) -> List[Answer]:
    return await answer_service.get_by_question_id(question_id)

async def get_answer_responses_by_user_id(user_id: int) -> List[AnswerResponse]:
    answers = await get_answers_by_user_id(user_id)
    return await answer_service.answers_to_answer_responses(answers)

async def get_dist_answers_by_question_id(question_id: int) -> QuestionOptionDistribution:
    answers = await get_answers_by_question_id(question_id)
    options = await option_service.get_by_question_id(question_id)
    result = dict.fromkeys([option.id for option in options], 0)

    for answer in answers:
        option_id = answer.option_id
        result[option_id] = result.get(option_id) + 1

    return QuestionOptionDistribution(
        question_id=question_id,
        option_distribution=[OptionCount(option_id=option.id, option_text=option.text, count=result[option.id]) for option in options]
    )
