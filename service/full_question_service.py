from typing import Optional, List

from model.full_question import FullQuestion
from model.question import Question
from service import question_service, option_service


async def get_by_id(question_id: int) -> Optional[FullQuestion]:
    question = await question_service.get_by_id(question_id)
    if question is not None:
        options = await option_service.get_by_question_id(question_id)
        full_question = FullQuestion(question_id=question.id, title=question.title, options=options)
        return full_question

    return None

async def get_all() -> List[FullQuestion]:
    questions = await question_service.get_all()

    return [
        FullQuestion(
            id=question.id,
            title=question.title,
            options=(await option_service.get_by_question_id(question.id))
        )
        for question in questions]

async def create_full_question(full_question: FullQuestion) -> int:
    question = Question(title=full_question.title)
    question_id = await question_service.create_question(question)
    for option in full_question.options:
        option.question_id = question_id
        await option_service.create_option(option)

    return question_id

async def update_full_question(question_id: int, full_question: FullQuestion) -> Optional[FullQuestion]:
    existing_question = await question_service.get_by_id(question_id)
    if existing_question is not None:
        updated_question = Question(id=question_id, title=full_question.title)
        await question_service.update_question(question_id, updated_question)
        existing_options = await option_service.get_by_question_id(question_id)
        existing_options_dict = {existing_option.id: existing_option for existing_option in existing_options}
        updated_options = []
        new_options = []
        for option in full_question.options:
            if option.id in existing_options_dict.keys():
                updated_options.append(option)
            else:
                option.question_id = question_id
                new_options.append(option)

        for update in updated_options:
            await option_service.update_option(update.id, update)

        for new in new_options:
            await option_service.create_option(new)

        return await get_by_id(question_id)

async def delete_question_option(option_id: int):
    await option_service.delete_option(option_id)

async def delete_full_question(question_id: int):
    await option_service.delete_options(question_id)
    await question_service.delete_question(question_id)

