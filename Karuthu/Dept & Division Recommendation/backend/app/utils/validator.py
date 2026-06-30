import re


def normalize_question(question: str) -> str:
    """
    Normalize a question for duplicate detection.
    """

    question = question.strip().lower()

    question = re.sub(r"\s+", " ", question)

    return question