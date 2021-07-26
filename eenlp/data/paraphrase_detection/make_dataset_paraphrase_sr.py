import pandas as pd
from pyprojroot import here


def make_dataset():
    dataset_name = "paraphrase_sr"

    commit_hash = "d2ef63657e34028978bf2a4a1662deef42c6ab91"
    df = pd.read_csv(
        f"https://raw.githubusercontent.com/vukbatanovic/paraphrase.sr/{commit_hash}/paraphrase.sr.train.txt",
        sep="\t",
        names=["label", "sentence1", "sentence2"],
    )

    result = pd.DataFrame()
    result["sentence1"] = df["sentence1"]
    result["sentence2"] = df["sentence2"]
    result["label"] = df["label"]
    result["lang"] = "Serbian"
    result["source"] = dataset_name
    result["split"] = "train"

    output_path = here(
        f"data/processed/paraphrase_detection/{dataset_name}/serbian.train.jsonl",
        warn=False,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)
