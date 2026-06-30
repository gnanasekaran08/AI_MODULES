from qdrant_client import QdrantClient

from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue
)

from app.utils.config import Config
from app.utils.logger import get_logger

logger = get_logger(__name__)


class QdrantService:

    _client = None

    @classmethod
    def initialize(cls):

        if cls._client is None:

            logger.info("Connecting to Qdrant...")

            cls._client = QdrantClient(

                host=Config.QDRANT_HOST,

                port=Config.QDRANT_PORT

            )

            logger.info("Connected to Qdrant.")

    @classmethod
    def client(cls):

        if cls._client is None:
            cls.initialize()

        return cls._client
    

    @classmethod
    def create_collection(cls):

        client = cls.client()

        collections = client.get_collections().collections

        names = [c.name for c in collections]

        if Config.COLLECTION_NAME in names:

            logger.info("Collection already exists.")

            return

        logger.info("Creating Collection...")

        client.create_collection(

            collection_name=Config.COLLECTION_NAME,

            vectors_config=VectorParams(

                size=384,

                distance=Distance.COSINE

            )

        )

        logger.info("Collection Created.")



    @classmethod
    def insert_vector(
        cls,
        question_id: int,
        embedding: list,
        question: str,
        department: str,
        division: str
    ):

        client = cls.client()

        client.upsert(

            collection_name=Config.COLLECTION_NAME,

            points=[

                PointStruct(

                    id=question_id,

                    vector=embedding,

                    payload={

                        "question": question,

                        "department": department,

                        "division": division

                    }

                )

            ]

        )

        logger.info(f"Vector inserted : {question_id}")


    @classmethod
    def search_vector(
        cls,
        embedding: list,
        limit: int = 1
    ):

        client = cls.client()

        results = client.query_points(

            collection_name=Config.COLLECTION_NAME,

            query=embedding,

            limit=limit,

            with_payload=True

        )

        return results
    
    @classmethod
    def delete_vector(
        cls,
        question_id: int
    ):

        client = cls.client()

        client.delete(

            collection_name=Config.COLLECTION_NAME,

            points_selector=[question_id]

        )

        logger.info(f"Vector deleted : {question_id}")


    @classmethod
    def update_vector(
        cls,
        question_id,
        embedding,
        question,
        department,
        division
    ):

        cls.insert_vector(

            question_id,

            embedding,

            question,

            department,

            division

        )

    @classmethod
    def get_vector(
        cls,
        question_id
    ):

        client = cls.client()

        result = client.retrieve(

            collection_name=Config.COLLECTION_NAME,

            ids=[question_id],

            with_payload=True

        )

        return result