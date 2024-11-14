from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from starlette import status

from model.full_question import FullQuestion
from service import full_question_service

router = APIRouter(
    prefix="/question",
    tags=["question"]
)

@router.get("/{question_id}", response_model=FullQuestion, status_code=status.HTTP_200_OK)
async def get_question_by_id(question_id: int) -> FullQuestion:
    existing_question = await full_question_service.get_by_id(question_id)
    if not existing_question:
        raise HTTPException(status_code=400, detail=f"Question with question_id: {question_id} not found")
    else:
        return existing_question

@router.post("/", response_model=int, status_code=status.HTTP_201_CREATED)
async def create_full_question(full_question: FullQuestion) -> int:
    try:
        create_question_id = await full_question_service.create_full_question(full_question)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404, detail="Can't create new question")

    return create_question_id


@router.put("/{question_id}", status_code=status.HTTP_200_OK)
async def update_full_question(question_id: int, full_question: FullQuestion) -> Optional[FullQuestion]:
    try:
        return await full_question_service.update_full_question(question_id, full_question)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404, detail="Can't update question")


@router.delete("/option/{option_id}", status_code=status.HTTP_200_OK)
async def delete_question_option(option_id: int):
    await full_question_service.delete_question_option(option_id)

@router.delete("/{question_id}", status_code=status.HTTP_200_OK)
async def delete_full_question(question_id: int):
    await full_question_service.delete_full_question(question_id)

@router.get("/", response_model=FullQuestion, status_code=status.HTTP_200_OK)
async def get_full_questions() -> List[FullQuestion]:
    return await full_question_service.get_all()
