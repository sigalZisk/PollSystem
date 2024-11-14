from typing import Optional, List

from model.option import Option
from repository import option_repository


async def get_by_id(option_id: int) -> Optional[Option]:
    return await option_repository.get_by_id(option_id)

async def get_by_question_id(question_id: int) -> List[Option]:
    return await option_repository.get_by_question_id(question_id)


async def create_option(option: Option):
    return await option_repository.create_option(option)

async def update_option(option_id: int, option: Option):
    existing_option = await get_by_id(option_id)
    if existing_option is not None:
        option.id = existing_option.id
        await option_repository.update_option(option_id, option)

async def delete_option(option_id: int):
    await option_repository.delete_option(option_id)

async def delete_options(question_id: int):
    await option_repository.delete_options(question_id)