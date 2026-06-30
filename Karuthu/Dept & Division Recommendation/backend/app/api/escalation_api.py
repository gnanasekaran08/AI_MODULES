from fastapi import APIRouter, HTTPException

from app.models.request import (
    QuestionRequest,
    QuestionUpdateRequest
)

from app.services.question_service import QuestionService
from app.services.predictor import Predictor
from app.models.request import PredictionRequest


router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)

@router.post("/predict")
def predict(request: PredictionRequest):

    return Predictor.predict(request.question)


@router.post("/add")
def add_question(request: QuestionRequest):

    try:

        question_id = QuestionService.add_question(

            request.question,

            request.department,

            request.division

        )

        return {

            "success": True,

            "id": question_id,

            "message": "Question Added Successfully"

        }

    except ValueError as e:

        raise HTTPException(
            status_code=409,
            detail=str(e)
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
    

@router.get("/")
def get_questions():

    return QuestionService.get_all()


@router.get("/{question_id}")
def get_question(question_id: int):

    data = QuestionService.get_question(question_id)

    if not data:

        raise HTTPException(
            status_code=404,
            detail="Question Not Found"
        )

    return data


@router.delete("/{question_id}")
def delete(question_id: int):

    QuestionService.delete_question(question_id)

    return {

        "success": True,

        "message": "Deleted Successfully"

    }


@router.put("/{question_id}")
def update(
    question_id: int,
    request: QuestionUpdateRequest
):

    QuestionService.update_question(

        question_id,

        request.question,

        request.department,

        request.division

    )

    return {

        "success": True,

        "message": "Updated Successfully"

    }

