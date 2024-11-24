from typing import List

from fastapi import HTTPException, APIRouter
from starlette import status

from model.answer import Answer
from model.answer_response import AnswerResponse
from service import answer_service

router = APIRouter(
    prefix="/answer",
    tags=["answer"]
)

@router.get("/{answer_id}", response_model=AnswerResponse, status_code=status.HTTP_200_OK)
async def get_answer_by_id(answer_id: int) -> AnswerResponse:
    existing_answer = await answer_service.get_by_id(answer_id)
    if not existing_answer:
        raise HTTPException(status_code=400, detail=f"Answer with answer_id: {answer_id} not found")
    return existing_answer

@router.post("/", response_model=List[int], status_code=status.HTTP_200_OK)
async def create_answers(answers: List[Answer]) -> List[int]:
    try:
        answer_ids = await answer_service.create_answers(answers)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return answer_ids

@router.put("/{answer_id}", status_code=status.HTTP_200_OK)
async def update_answer(answer_id: int, answer: Answer):
    try:
        await answer_service.update_answer(answer_id, answer)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=400, detail=f"Can't update answer with answer_id : {answer_id}")
    return answer_id

@router.delete("/{answer_id}", status_code=status.HTTP_200_OK)
async def delete_answer(answer_id: int):
    await answer_service.delete_answer(answer_id)

