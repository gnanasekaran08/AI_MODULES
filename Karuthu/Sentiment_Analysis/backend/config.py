from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "Sentiment Service"
    APP_VERSION: str = "1.0.0"

    ENVIRONMENT: str = "development"


    HOST: str = "0.0.0.0"
    PORT: int = 9000

    MODEL_NAME: str = "distilbert-base-uncased"
    MODEL_PATH: str = "app/models/sentiment_model"

    MAX_TEXT_LENGTH: int = 2000

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()