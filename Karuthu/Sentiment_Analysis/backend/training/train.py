import os
import sys

ROOT_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, ROOT_DIR)

import pandas as pd

from datasets import Dataset

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support
)

from config import settings
from transformers import EarlyStoppingCallback


LABEL_MAP = {
    "negative": 0,
    "neutral": 1,
    "positive": 2
}


def compute_metrics(pred):

    labels = pred.label_ids

    preds = pred.predictions.argmax(-1)

    precision, recall, f1, _ = precision_recall_fscore_support(
        labels,
        preds,
        average="weighted"
    )

    accuracy = accuracy_score(
        labels,
        preds
    )

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }


print("Loading Dataset...")

df = pd.read_csv(
    "training/sentiment_dataset.csv"
)

df["label"] = df["sentiment"].map(
    LABEL_MAP
)

dataset = Dataset.from_pandas(df)

print(
    f"Records Loaded: {len(df)}"
)

tokenizer = AutoTokenizer.from_pretrained(
    settings.MODEL_NAME
)


def tokenize(batch):

    return tokenizer(
        batch["feedback"],
        truncation=True,
        padding="max_length",
        max_length=128
    )


dataset = dataset.map(
    tokenize,
    batched=True
)

dataset = dataset.train_test_split(
    test_size=0.2,
    stratify_by_column="label"
)

train_dataset = dataset["train"]

test_dataset = dataset["test"]

print(
    f"Train: {len(train_dataset)}"
)

print(
    f"Test : {len(test_dataset)}"
)

model = AutoModelForSequenceClassification.from_pretrained(
    settings.MODEL_NAME,
    num_labels=3
)

training_args = TrainingArguments(
    output_dir="training/results",

    num_train_epochs=5,

    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,

    learning_rate=2e-5,

    weight_decay=0.01,
    metric_for_best_model="f1",
    greater_is_better=True,

    evaluation_strategy="epoch",

    save_strategy="epoch",
    save_total_limit=1,
    load_best_model_at_end=True,

    logging_steps=50
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics
    callbacks=[
        EarlyStoppingCallback(
            early_stopping_patience=2
        )
    ]
)

print("Training Started...")

trainer.train()

print("Training Completed")

os.makedirs(
    settings.MODEL_PATH,
    exist_ok=True
)

trainer.save_model(settings.MODEL_PATH)


tokenizer.save_pretrained(
    settings.MODEL_PATH
)

print(
    f"Model Saved To: {settings.MODEL_PATH}"
)