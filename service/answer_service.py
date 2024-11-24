from typing import Optional, List

from api.internalApi.user_service import user_service_api
from exceptions.CreateAnswerException import CreateAnswerException, AlreadyAnsweredException
from exceptions.UserNotRegisteredExcetpion import UserNotRegisteredException
from exceptions.option_exceptions import OptionDoesNotBelongToQuestion
from model.answer import Answer
from model.answer_response import AnswerResponse
from repository import answer_repository
from service import option_service, question_service


async def get_by_id(answer_id: int) -> Optional[AnswerResponse]:
    answer = await answer_repository.get_by_id(answer_id)

    if answer is not None:
        return await answer_to_answer_response(answer)
    else:
        return None

async def get_by_question_id(question_id: int) -> List[Answer]:
    return await answer_repository.get_by_question_id(question_id)

async def get_by_user_id(user_id: int) -> List[Answer]:
    if await user_registered(user_id):
        return await answer_repository.get_by_user_id(user_id)
    else:
        raise UserNotRegisteredException(f"""Please register this user (user_id is {user_id}) before trying to access polls.""")

async def create_answer(answer: Answer) -> int:
    if await user_registered(answer.user_id):
        existing_answer = await answer_repository.get_by_user_id_and_question_id(
                                                    user_id=answer.user_id, question_id=answer.question_id)
        if existing_answer is not None:
            raise AlreadyAnsweredException(f"""Please use 'Update' method to update an existing answer - (answer_id is {existing_answer.id})""")

        await check_if_option_belongs_to_question(question_id=answer.question_id, option_id=answer.option_id)

        return await answer_repository.create_answer(answer)
    else:
        raise UserNotRegisteredException(f"""Please register this user (user_id is {answer.user_id}) before trying to access polls.""")

async def create_answers(answers: List[Answer]) -> List[int]:
    returned_ids = []

    for answer in answers:
        try:
            returned_ids.append(await create_answer(answer))
        except Exception as e:
            print(str(e))
            raise CreateAnswerException(f"Can't create answer for question_id : {answer.question_id}: {str(e)}")

    return returned_ids

async def update_answer(answer_id: int, answer: Answer):
    existing_answer = await get_by_id(answer_id)
    if existing_answer is not None:
        await answer_repository.update_answer(answer_id, answer)

async def delete_answer(answer_id: int):
    await answer_repository.delete_answer(answer_id)

async def delete_answers_by_question_id(question_id: int):
    await answer_repository.delete_answers_by_question_id(question_id)

async def delete_answers_by_user_id(user_id: int):
    await answer_repository.delete_answers_by_user_id(user_id)

async def answer_to_answer_response(answer: Answer) -> AnswerResponse:
    print("answer is:", answer)
    question = await question_service.get_by_id(answer.question_id)
    option = await option_service.get_by_id(answer.option_id)

    print("question is:", question)
    print("option is:", option)
    answer_response = AnswerResponse(
        id=answer.id,
        user_id=answer.user_id,
        question=question,
        option=option
    )

    return answer_response

async def answers_to_answer_responses(answers: List[Answer]) -> List[AnswerResponse]:
    answer_responses = []
    for answer in answers:
        answer_responses.append(await answer_to_answer_response(answer))

    return answer_responses

async def user_registered(user_id: int) -> bool:
    return await user_service_api.is_user_registered(user_id)

async def check_for_existing_answer(user_id=int, question_id=int) -> bool:
    answer = await answer_repository.get_by_user_id_and_question_id(user_id=user_id, question_id=question_id)

    return answer is not None

async def check_if_option_belongs_to_question(question_id: int, option_id: int):
    existing_options = await option_service.get_by_question_id(question_id)
    matching = [option for option in existing_options if option.id == option_id]

    if len(matching) == 0:
        raise OptionDoesNotBelongToQuestion(f"option_id {option_id} does not belong to question_id {question_id}.")
