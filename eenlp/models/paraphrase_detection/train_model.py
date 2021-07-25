import numpy as np
from datasets import load_dataset, load_metric
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)

if __name__ == "__main__":
    raw_datasets = load_dataset("glue", "mrpc")
    checkpoint = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)

    def tokenize_function(example):
        return tokenizer(example["sentence1"], example["sentence2"], truncation=True)

    tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)

    def compute_metrics(eval_preds):
        metric = load_metric("glue", "mrpc")
        logits, labels = eval_preds
        predictions = np.argmax(logits, axis=-1)
        return metric.compute(predictions=predictions, references=labels)

    training_args = TrainingArguments("test-trainer", evaluation_strategy="epoch")
    model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)

    trainer = Trainer(
        model,
        training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["validation"],
        tokenizer=tokenizer,
        compute_metrics=compute_metrics,
    )

    trainer.train()
