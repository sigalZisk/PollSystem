from typing import Optional, List

from model.question import Question
from repository.database import database

TABLE_NAME = "questions"

async def get_by_id(question_id: int) -> Optional[Question]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id = :question_id"
    result = await database.fetch_one(query, values={"question_id": question_id})
    if result:
        return Question(**result)
    else:
        return None

async def get_all() -> List[Question]:
    query = f"SELECT * FROM {TABLE_NAME}"
    results = await database.fetch_all(query)
    return [Question(**result) for result in results]

async def create_question(question: Question) -> int:
    query = f"INSERT INTO {TABLE_NAME} (title) VALUES(:title)"

    async with database.transaction():
        await database.execute(query, values={"title": question.title})
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")

    return last_record_id[0]

async def update_question(question_id: int, question: Question):
    query = f"UPDATE {TABLE_NAME} SET title = :title WHERE id = :question_id"

    values = {"question_id": question_id, "title": question.title}

    await database.execute(query, values)

async def delete_question(question_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id = :question_id"

    await database.execute(query, values={"question_id": question_id})
