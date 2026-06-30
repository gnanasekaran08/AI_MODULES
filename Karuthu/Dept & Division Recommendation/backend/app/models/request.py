from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):

    question: str = Field(..., min_length=5, max_length=500)

    department: str = Field(..., min_length=2)

    division: str = Field(..., min_length=2)


class QuestionUpdateRequest(BaseModel):

    question: str = Field(..., min_length=5, max_length=500)

    department: str = Field(..., min_length=2)

    division: str = Field(...,min_length=2)


class PredictionRequest(BaseModel):

    question: str = Field(..., min_length=5, max_length=500)