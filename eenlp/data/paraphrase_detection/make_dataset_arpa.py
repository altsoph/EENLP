import pandas as pd
from pyprojroot import here


def make_dataset():
    dataset_name = "arpa"

    commit_hash = "02fcbc70a36fdd3d8e8eefb226d41e2cb9519aa7"
    df = pd.read_csv(
        f"https://raw.githubusercontent.com/ivannikov-lab/arpa-paraphrase-corpus/{commit_hash}/train.tsv",
        sep="\t",
    )

    result = pd.DataFrame()
    result["sentence1"] = df["Sentence1"]
    result["sentence2"] = df["Sentence2"]
    # "labelled as either paraphrase, near paraphrase or non-paraphrase (with 1, 0, -1 labels respectively)"
    # https://github.com/ivannikov-lab/arpa-paraphrase-corpus/blob/02fcbc70a36fdd3d8e8eefb226d41e2cb9519aa7/README.md
    result["label"] = (df["Paraphrase"] == 1).astype(int)
    result["lang"] = "Armenian"
    result["source"] = dataset_name
    result["split"] = "train"

    output_path = here(
        f"data/processed/paraphrase_detection/{dataset_name}/armenian.train.jsonl",
        warn=False,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)
