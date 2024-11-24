from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from model.answer_response import AnswerResponse
from model.question_options_distribution import QuestionOptionDistribution
from service import analytics_service

router = APIRouter(
    prefix="/analytics",
    tags=["analytics"]
)

@router.get("/question/{question_id}/responses/count", response_model=int, status_code=status.HTTP_200_OK)
async def get_total_answers_by_question_id(question_id: int) -> int:
    question_answers = await analytics_service.get_answers_by_question_id(question_id)
    return len(question_answers)

@router.get("/question/{question_id}/responses/distribution", response_model=QuestionOptionDistribution, status_code=status.HTTP_200_OK)
async def get_dist_answers_by_question_id(question_id: int) -> QuestionOptionDistribution:
    question_answers = await analytics_service.get_dist_answers_by_question_id(question_id)
    return question_answers

@router.get("/user/{user_id}/responses/count", response_model=int, status_code=status.HTTP_200_OK)
async def get_total_answers_by_user_id(user_id: int) -> int:
    try:
        user_answers = await analytics_service.get_answers_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return len(user_answers)

@router.get("/user/{user_id}/responses", response_model=List[AnswerResponse], status_code=status.HTTP_200_OK)
async def get_answers_by_user_id(user_id: int) -> List[AnswerResponse]:
    try:
        existing_user_answers = await analytics_service.get_answer_responses_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return existing_user_answers
