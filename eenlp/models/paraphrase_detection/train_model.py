import numpy as np
from datasets import load_dataset, load_metric
from pyprojroot import here
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)

if __name__ == "__main__":
    raw_datasets = load_dataset(
        "json",
        data_files=here("data/paraphrase_detection/glue_mrpc/english.train.jsonl"),
    )

    pretrained_model_name = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)

    def tokenize_function(example):
        return tokenizer(example["sentence1"], example["sentence2"], truncation=True)

    tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
    original_glue_dataset = load_dataset("glue", "mrpc").map(
        tokenize_function, batched=True
    )

    def compute_metrics(eval_preds):
        metric = load_metric("glue", "mrpc")
        logits, labels = eval_preds
        predictions = np.argmax(logits, axis=-1)
        return metric.compute(predictions=predictions, references=labels)

    training_args = TrainingArguments(
        output_dir=here("models/paraphrase_detection", warn=False),
        evaluation_strategy="epoch",
    )
    model = AutoModelForSequenceClassification.from_pretrained(
        pretrained_model_name,
        num_labels=2,
    )

    trainer = Trainer(
        model,
        training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=original_glue_dataset["validation"],
        tokenizer=tokenizer,
        compute_metrics=compute_metrics,
    )

    trainer.train()
