import logging
import os

from logging.handlers import RotatingFileHandler

from app.utils.config import Config


def get_logger(name: str):

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(Config.LOG_LEVEL)

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

    )

    file_handler = RotatingFileHandler(

        Config.LOG_FILE,

        maxBytes=10 * 1024 * 1024,

        backupCount=5,

        encoding="utf-8"

    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)

    return logger