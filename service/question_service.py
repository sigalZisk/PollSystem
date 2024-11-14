from typing import Optional, List

from model.question import Question
from repository import question_repository


async def get_by_id(question_id: int) -> Optional[Question]:
    question = await question_repository.get_by_id(question_id)
    return question

async def get_all() -> List[Question]:
    return await question_repository.get_all()

async def create_question(question: Question):
    return await question_repository.create_question(question)

async def update_question(question_id: int, question: Question):
    existing_question = await question_repository.get_by_id(question_id)
    if existing_question is not None:
        question.id = existing_question.id
        await question_repository.update_question(question_id, question)

async def delete_question(question_id: int):
    await question_repository.delete_question(question_id)
