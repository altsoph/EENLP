"""
This script generates every paraphrase detection dataset by running the corresponding scripts, then aggregates all of
them into `data/processed/paraphrase_detection/`.
"""
import importlib

import pandas as pd
from pyprojroot import here

dataset_names = [
    "arpa",
    "glue_mrpc",
    "glue_qqp",
    "glue_stsb",
    "klej_cdsc_r",
    "paraphrase_sr",
    "ro_sts",
]


def make_dataset():
    # generate datasets
    for dataset_name in dataset_names:
        if not here(
            f"data/processed/paraphrase_detection/{dataset_name}", warn=False
        ).exists():
            importlib.import_module(
                f"eenlp.data.paraphrase_detection.make_dataset_{dataset_name}"
            ).make_dataset()

    # aggregate and save dataset
    df = pd.concat(
        pd.read_json(filename, lines=True)
        for filename in here("data/processed/paraphrase_detection").glob("*/*.jsonl")
    )
    for lang in sorted(df["lang"].unique()):
        df[df["lang"] == lang].to_json(
            here(
                f"data/processed/paraphrase_detection/{lang.lower()}.jsonl", warn=False
            ),
            orient="records",
            lines=True,
        )


if __name__ == "__main__":
    make_dataset()
