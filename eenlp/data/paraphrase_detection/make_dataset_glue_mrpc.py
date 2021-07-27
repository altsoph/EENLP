import pandas as pd
from datasets import load_dataset
from pyprojroot import here


def make_dataset():
    dataset_name = "glue_mrpc"

    dataset = load_dataset("glue", "mrpc")
    df = dataset["train"].to_pandas()

    result = pd.DataFrame()
    result["sentence1"] = df["sentence1"]
    result["sentence2"] = df["sentence2"]
    result["label"] = df["label"]
    result["lang"] = "English"
    result["source"] = dataset_name
    result["split"] = "train"

    output_path = here(
        f"data/processed/paraphrase_detection/{dataset_name}/english.train.jsonl",
        warn=False,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)


if __name__ == "__main__":
    make_dataset()
