from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd
from datasets import load_dataset

with TemporaryDirectory() as tempdir:

    # eenlp/data/paraphrase_detection/make_dataset_paraphrase_sr.py

    dataset_name = "paraphrase_sr"

    commit_hash = "d2ef63657e34028978bf2a4a1662deef42c6ab91"
    df = pd.read_csv(
        f"https://raw.githubusercontent.com/vukbatanovic/paraphrase.sr/{commit_hash}/paraphrase.sr.train.txt",
        sep="\t",
        names=["label", "sentence1", "sentence2"],
    )

    # fix data, remove this non-printing character
    df["label"] = df["label"].str.replace("\ufeff", "").astype(int)

    result = pd.DataFrame()
    result["sentence1"] = df["sentence1"]
    result["sentence2"] = df["sentence2"]
    result["label"] = df["label"]
    result["lang"] = "Serbian"
    result["source"] = dataset_name
    result["split"] = "train"

    output_path = Path(tempdir) / f"{dataset_name}/serbian.train.jsonl"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)

    # eenlp/data/paraphrase_detection/make_dataset_glue_qqp.py

    dataset_name = "glue_qqp"

    dataset = load_dataset("glue", "qqp")
    df = dataset["train"].to_pandas()

    result = pd.DataFrame()
    result["sentence1"] = df["question1"]
    result["sentence2"] = df["question2"]
    result["label"] = df["label"]
    result["lang"] = "English"
    result["source"] = dataset_name
    result["split"] = "train"

    output_path = Path(tempdir) / f"{dataset_name}/english.train.jsonl"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)

    # eenlp/data/paraphrase_detection/make_dataset_ro_sts.py

    dataset_name = "ro_sts"

    dataset = load_dataset("ro_sts")
    df = dataset["train"].to_pandas()

    result = pd.DataFrame()
    result["sentence1"] = df["sentence1"]
    result["sentence2"] = df["sentence2"]
    result["label"] = (df["score"] >= 4).astype(int)
    result["lang"] = "Romanian"
    result["source"] = dataset_name
    result["split"] = "train"

    output_path = Path(tempdir) / f"{dataset_name}/romanian.train.jsonl"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)

    # eenlp/data/paraphrase_detection/make_dataset_glue_stsb.py

    dataset_name = "glue_stsb"

    dataset = load_dataset("glue", "stsb")
    df = dataset["train"].to_pandas()

    result = pd.DataFrame()
    result["sentence1"] = df["sentence1"]
    result["sentence2"] = df["sentence2"]
    result["label"] = (df["label"] >= 4).astype(int)
    result["lang"] = "English"
    result["source"] = dataset_name
    result["split"] = "train"

    output_path = Path(tempdir) / f"{dataset_name}/english.train.jsonl"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)

    # eenlp/data/paraphrase_detection/make_dataset_glue_mrpc.py

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

    output_path = Path(tempdir) / f"{dataset_name}/english.train.jsonl"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)

    # eenlp/data/paraphrase_detection/make_dataset_klej_cdsc_r.py

    dataset_name = "klej_cdsc_r"

    dataset = load_dataset("cdsc", "cdsc-r")
    df = dataset["train"].to_pandas()

    result = pd.DataFrame()
    result["sentence1"] = df["sentence_A"]
    result["sentence2"] = df["sentence_B"]
    result["label"] = (df["relatedness_score"] >= 4).astype(int)
    result["lang"] = "Polish"
    result["source"] = dataset_name
    result["split"] = "train"

    output_path = Path(tempdir) / f"{dataset_name}/polish.train.jsonl"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)

    # eenlp/data/paraphrase_detection/make_dataset_arpa.py

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

    output_path = Path(tempdir) / f"{dataset_name}/armenian.train.jsonl"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_json(output_path, orient="records", lines=True)

    # aggregate and save dataset
    df = pd.concat(
        pd.read_json(filename, lines=True)
        for filename in Path(tempdir).glob("*/*.jsonl")
    )

    df.to_csv("PARAPHRASE_DETECTION.csv", index=False)
