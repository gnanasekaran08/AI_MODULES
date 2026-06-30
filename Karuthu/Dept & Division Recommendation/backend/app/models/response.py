from pydantic import BaseModel


class PredictionResponse(BaseModel):

    success: bool

    department: str | None = None

    division: str | None = None

    similarity: float | None = None

    matched_question: str | None = None

    message: str | None = None