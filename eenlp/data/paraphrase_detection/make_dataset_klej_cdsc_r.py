import pandas as pd
from datasets import load_dataset
from pyprojroot import here


def make_dataset():
    dataset_name = "klej_cdsc_r"

    dataset = load_dataset("cdsc", "cdsc-r")
    df = dataset["train"].to_pandas()

    result = pd.DataFrame()
    result["sentence1"] = df["sentence_A"]
    result["sentence2"] = df["sentence_B"]
    # TODO document choice of threshold
    result["label"] = (df["relatedness_score"] >= 4).astype(int)
    result["lang"] = "Polish"
    result["source"] = dataset_name
    result["split"] = "train"

    output_path = here(
        f"data/processed/paraphrase_detection/{dataset_name}/polish.train.jsonl",
        warn=False,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)


if __name__ == "__main__":
    make_dataset()
