from app.services.training_service import TrainingService
from app.services.qdrant_service import QdrantService
from app.utils.config import Config
from app.utils.logger import get_logger

logger = get_logger(__name__)


class Predictor:

    @staticmethod
    def predict(question: str):

        try:

            embedding = TrainingService.encode(question)

            results = QdrantService.search_vector(
                embedding=embedding,
                limit=1
            )

            if not results.points:
                return {
                    "success": False,
                    "message": "No matching question found."
                }


            result = results.points[0]

            score = result.score

            payload = result.payload

            if score < Config.SIMILARITY_THRESHOLD:

                return {
                    "success": False,
                    "message": "No similar question found.",
                    "score": round(score, 4)
                }

            return {

                "success": True,

                "question": payload["question"],

                "department": payload["department"],

                "division": payload["division"],

                "similarity": round(score, 4)

            }

        except Exception as e:

            logger.exception(e)

            raise