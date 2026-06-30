import pandas as pd

from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

from app.services.predictor import predictor


df = pd.read_csv(
    "training/sentiment_dataset.csv"
)

actual = []

predicted = []

for _, row in df.iterrows():

    result = predictor.predict(
        row["feedback"]
    )

    actual.append(
        row["sentiment"]
    )

    predicted.append(
        result["sentiment"]
    )

print(
    classification_report(
        actual,
        predicted
    )
)

print(
    confusion_matrix(
        actual,
        predicted
    )
)