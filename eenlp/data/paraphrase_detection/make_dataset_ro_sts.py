import pandas as pd
from datasets import load_dataset
from pyprojroot import here


def make_dataset():
    dataset_name = "ro_sts"

    dataset = load_dataset("ro_sts")
    df = dataset["train"].to_pandas()

    result = pd.DataFrame()
    result["sentence1"] = df["sentence1"]
    result["sentence1"] = df["sentence2"]
    # TODO document choice of threshold
    result["label"] = (df["score"] >= 4).astype(int)
    result["lang"] = "Romanian"
    result["soruce"] = dataset_name
    result["split"] = "train"

    output_path = here(
        f"data/processed/paraphrase_detection/{dataset_name}/romanian.train.jsonl",
        warn=False,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)


if __name__ == "__main__":
    make_dataset()
