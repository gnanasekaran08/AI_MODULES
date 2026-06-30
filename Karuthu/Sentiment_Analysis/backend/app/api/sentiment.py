from typing import List

from fastapi import APIRouter
from fastapi import HTTPException

from pydantic import BaseModel
from pydantic import Field

from config import settings

from app.services.predictor import predictor


router = APIRouter(
    prefix="/sentiment",
    tags=["Sentiment"]
)


class SentimentRequest(BaseModel):

    feedback: str = Field(
        ...,
        min_length=1,
        max_length=settings.MAX_TEXT_LENGTH
    )


class BulkSentimentRequest(BaseModel):

    feedbacks: List[str]


@router.post("/predict")
async def predict_sentiment(
    request: SentimentRequest
):

    try:

        return predictor.predict_feedback(request.feedback)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/predict-batch")
async def predict_batch(
    request: BulkSentimentRequest
):

    try:

        return {
            "count": len(request.feedbacks),
            "results": predictor.predict_batch(
                request.feedbacks
            )
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/health")
async def health():

    return {
        "status": "healthy"
    }