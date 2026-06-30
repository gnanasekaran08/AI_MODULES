import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Central configuration for the application.
    """

    # --------------------------
    # API
    # --------------------------

    API_TITLE = "Department & Division Prediction API"

    API_VERSION = "1.0.0"

    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # --------------------------
    # Model
    # --------------------------

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    SIMILARITY_THRESHOLD = float(
        os.getenv(
            "SIMILARITY_THRESHOLD",
            0.80
        )
    )

    # --------------------------
    # MySQL
    # --------------------------

    MYSQL_HOST = os.getenv("MYSQL_HOST")

    MYSQL_PORT = int(
        os.getenv("MYSQL_PORT", 3306)
    )

    MYSQL_USER = os.getenv("MYSQL_USER")

    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    # --------------------------
    # Qdrant
    # --------------------------

    QDRANT_HOST = os.getenv(
        "QDRANT_HOST",
        "localhost"
    )

    QDRANT_PORT = int(
        os.getenv(
            "QDRANT_PORT",
            6333
        )
    )

    COLLECTION_NAME = os.getenv(
        "COLLECTION_NAME",
        "department_prediction"
    )

    # --------------------------
    # Logging
    # --------------------------

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    LOG_FILE = os.getenv(
        "LOG_FILE",
        "logs/application.log"
    )