import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)
from app.services.clause_splitter import ClauseSplitter

from config import settings

from app.services.preprocess import (
    TextPreprocessor
)

from app.services.rules import (
    RuleEngine
)


class SentimentPredictor:

    _instance = None

    LABELS = {
        0: "negative",
        1: "neutral",
        2: "positive"
    }

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.load_model()

        return cls._instance

    def load_model(self):

        self.tokenizer = AutoTokenizer.from_pretrained(
            settings.MODEL_PATH
        )

        self.model = AutoModelForSequenceClassification.from_pretrained(
            settings.MODEL_PATH
        )

        self.model.eval()

    def predict(self, text: str):

        rule_result = RuleEngine.predict(text)

        if rule_result:
            return rule_result

        text = TextPreprocessor.process(text)

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        with torch.no_grad():

            outputs = self.model(**inputs)

            probabilities = torch.softmax(
                outputs.logits,
                dim=1
            )

        confidence = torch.max(
            probabilities
        ).item()

        predicted_class = torch.argmax(
            probabilities
        ).item()

        probabilities = torch.softmax(outputs.logits, dim=1)[0]

        negative = probabilities[0].item()
        neutral = probabilities[1].item()
        positive = probabilities[2].item()

        return {
            "positive": round(positive, 4),
            "neutral": round(neutral, 4),
            "negative": round(negative, 4),
            "sentiment": self.LABELS[torch.argmax(probabilities).item()],
            "source": "ml_model"
        }
    
    import re

    # def split_feedback(feedback):

    #     sentences = [
    #         s.strip()
    #         for s in re.split(pattern, feedback, flags=re.IGNORECASE)
    #         if s.strip()
    #     ]

    #     return sentences

    def predict_feedback(self, feedback: str):

        # Overall prediction
        overall = self.predict(feedback)

        sentences = ClauseSplitter.split(feedback)

        sentence_results = []

        for sentence in sentences:

            result = self.predict(sentence)
            # print(result)

            sentence_results.append({
                "text": sentence,
                "positive": result["positive"],
                "neutral": result["neutral"],
                "negative": result["negative"],
                "sentiment": result["sentiment"]
            })

        return {
            "positive": overall["positive"],
            "neutral": overall["neutral"],
            "negative": overall["negative"],
            "overall_sentiment": overall["sentiment"],
            "source": overall["source"],
            "sentences": sentence_results
        }
   
    def predict_batch(
        self,
        texts: list[str]
    ):

        results = []

        for text in texts:

            results.append(
                self.predict_feedback(text)
            )

        return results


predictor = SentimentPredictor()