from typing import Optional, List

from model.answer import Answer
from repository.database import database

TABLE_NAME = "answers"

async def get_by_id(answer_id: int) -> Optional[Answer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id = :answer_id"
    result = await database.fetch_one(query, values={"answer_id": answer_id})
    if result:
        return Answer(**result)
    else:
        return None

async def get_by_question_id(question_id: int) -> list[Answer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE question_id = :question_id"
    results = await database.fetch_all(query, values={"question_id": question_id})
    return [Answer(**result) for result in results]

async def get_by_user_id(user_id: int) -> list[Answer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE user_id = :user_id"
    results = await database.fetch_all(query, values={"user_id": user_id})
    return [Answer(**result) for result in results]

async def get_by_user_id_and_question_id(user_id=int, question_id=int) -> Optional[Answer]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE user_id = :user_id AND question_id = :question_id"
    values = {"user_id": user_id,
              "question_id": question_id}
    result = await database.fetch_one(query, values=values)
    if result:
        return Answer(**result)
    else:
        return None

async def create_answer(answer: Answer) -> int:
    query = f"""INSERT INTO {TABLE_NAME} (user_id, question_id, option_id) 
                VALUES(:user_id, :question_id, :option_id)
            """
    values = {"user_id": answer.user_id,
              "question_id": answer.question_id,
              "option_id": answer.option_id}

    async with database.transaction():
        await database.execute(query, values=values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")

    return last_record_id[0]

async def update_answer(answer_id: int, answer: Answer):
    query = f"""
            UPDATE {TABLE_NAME}
            SET option_id = :option_id
            WHERE id = :answer_id
        """
    values = {"answer_id": answer_id, "option_id": answer.option_id}

    await database.execute(query, values)

async def delete_answer(answer_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id = :answer_id"

    await database.execute(query, values={"answer_id": answer_id})

async def delete_answers_by_question_id(question_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE question_id = :question_id"

    await database.execute(query, values={"question_id": question_id})

async def delete_answers_by_user_id(user_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE user_id = :user_id"

    await database.execute(query, values={"user_id": user_id})
