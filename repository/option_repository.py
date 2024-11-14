from typing import Optional, List

from model.option import Option
from repository.database import database

TABLE_NAME = "options"

async def get_by_id(option_id: int) -> Optional[Option]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id = :option_id"
    result = await database.fetch_one(query, values={"option_id": option_id})
    if result:
        return Option(**result)
    else:
        return None

async def get_by_question_id(question_id: int) -> list[Option]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE question_id = :question_id"
    results = await database.fetch_all(query, values={"question_id": question_id})
    return [Option(**result) for result in results]

async def create_option(option: Option) -> int:
    query = f"""INSERT INTO {TABLE_NAME} (question_id, text) 
                VALUES(:question_id, :text)
            """
    values = {"question_id": option.question_id,
              "text": option.text}

    async with database.transaction():
        await database.execute(query, values=values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")

    return last_record_id[0]

async def update_option(option_id: int, option: Option):
    query = f"UPDATE {TABLE_NAME} SET text = :text WHERE id = :option_id"

    values = {"option_id": option_id, "text": option.text}

    await database.execute(query, values)

async def delete_option(option_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id = :option_id"

    await database.execute(query, values={"option_id": option_id})

async def delete_options(question_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE question_id = :question_id"

    await database.execute(query, values={"question_id": question_id})
