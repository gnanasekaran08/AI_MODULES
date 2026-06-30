from sentence_transformers import SentenceTransformer

from app.utils.config import Config
from app.utils.logger import get_logger

logger = get_logger(__name__)


class TrainingService:

    _model = None

    @classmethod
    def initialize(cls):
        """
        Load the embedding model only once.
        """

        if cls._model is None:

            logger.info(f"Loading model : {Config.MODEL_NAME}")

            cls._model = SentenceTransformer(
                Config.MODEL_NAME
            )

            logger.info("SentenceTransformer loaded successfully.")

    @classmethod
    def get_model(cls):

        if cls._model is None:
            cls.initialize()

        return cls._model

    @classmethod
    def encode(cls, text: str):

        model = cls.get_model()

        embedding = model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()