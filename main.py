from fastapi import FastAPI
from repository.database import database

from controller.full_question_controller import router as question_router
from controller.answer_controller import router as answer_router
from controller.analytics_controller import router as analystics_router

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(question_router)
app.include_router(answer_router)
app.include_router(analystics_router)
