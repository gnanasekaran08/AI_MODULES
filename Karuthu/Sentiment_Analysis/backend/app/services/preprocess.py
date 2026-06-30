import re

import re



class TextPreprocessor:

    @staticmethod
    def clean(text: str) -> str:

        if not text:
            return ""

        text = text.strip()

        text = re.sub(r"\s+", " ", text)

        text = re.sub(
            r"http\S+|www\S+",
            "",
            text
        )

        return text
    
    @staticmethod
    def preprocess(text: str) -> str:

        text = re.sub(r"[.,!?;:]", " ", text)

        text = re.sub(r"\s+", " ", text)

        return text

    @staticmethod
    def normalize(text: str) -> str:

        text = text.lower()

        return text

    @classmethod
    def process(cls, text: str) -> str:

        text = cls.clean(text)

        text = cls.normalize(text)

        text = cls.preprocess(text)

        return text