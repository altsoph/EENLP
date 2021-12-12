import traceback
import warnings

import numpy as np
import pandas as pd
import pycountry
from datasets import load_dataset
from pyprojroot import here
from rapidfuzz import process
from tqdm.auto import tqdm

# DATASET_ONLY_FIRST_N = 20_000
DATASET_ONLY_FIRST_N = 10_000


def make_dataset():
    dataset_name = "tapaco"

    dataset = load_dataset("tapaco", "all_languages")
    df = dataset["train"].to_pandas()

    df["paraphrase_set_id"] = df["paraphrase_set_id"].astype(int)

    languages_to_keep = [
        "be",  # Belarusian
        "bg",  # Bulgarian
        "cs",  # Czech
        "en",  # English
        "et",  # Estonian
        "hr",  # Croatian
        "hu",  # Hungarian
        "hy",  # Armenian
        "lt",  # Lithuanian
        "mk",  # Macedonian
        "pl",  # Polish
        "ro",  # Romanian
        "ru",  # Russian
        "sl",  # Slovenian
        "sr",  # Serbian
        "uk",  # Ukrainian
    ]

    df = df[df["language"].isin(languages_to_keep)]
    assert len(languages_to_keep) == len(
        df["language"].unique()
    ), "Count of filtered languages doesn't match, probably a typo in 'languages_to_keep'?"

    # paraphrase_set_id = 0 seems to mean "unassigned".
    df = df[df["paraphrase_set_id"] != 0].copy()

    # We need to generate example pairs somehow.
    # As of the current version of the code, 50% of the generated examples are true paraphrases (label = 1),
    # 25% are chosen from the most similar non-paraphrases (by fuzzywuzzy library Levenshtein distance) (label = 0),
    # and 25% is random negative examples (label = 0).

    result = []
    np.random.seed(0)
    for language, df_language in tqdm(df.groupby("language"), "language", position=0):
        try:
            language_name = pycountry.languages.get(alpha_2=language).name

            df_language = df_language[:DATASET_ONLY_FIRST_N]

            for paraphrase_set_id, df_set in tqdm(
                df_language.groupby("paraphrase_set_id"),
                "paraphrase_set_id",
                position=1,
            ):
                if len(df_set) <= 1:
                    continue

                df_negatives = df_language[
                    df_language["paraphrase_set_id"] != paraphrase_set_id
                ]

                for row in df_set.itertuples():
                    result.append(
                        {
                            "sentence1": row.paraphrase,
                            "sentence2": np.random.choice(
                                df_set[df_set.index != row.Index]["paraphrase"]
                            ),
                            "label": 1,
                            "lang": language_name,
                        }
                    )

                    # TODO this can sample the same pair twice, consider fixing it
                    result.append(
                        {
                            "sentence1": row.paraphrase,
                            "sentence2": np.random.choice(
                                df_set[df_set.index != row.Index]["paraphrase"]
                            ),
                            "label": 1,
                            "lang": language_name,
                        }
                    )

                    # similar negative
                    similar_negatives = process.extract(
                        row.paraphrase,
                        df_negatives["paraphrase"],
                        limit=10,
                    )
                    result.append(
                        {
                            "sentence1": row.paraphrase,
                            "sentence2": np.random.choice(
                                np.array(similar_negatives)[:, 0]
                            ),
                            "label": 0,
                            "lang": language_name,
                        }
                    )

                    # random negative
                    result.append(
                        {
                            "sentence1": row.paraphrase,
                            "sentence2": np.random.choice(df_negatives["paraphrase"]),
                            "label": 0,
                            "lang": language_name,
                        }
                    )
        except KeyboardInterrupt:
            raise
        except:
            warnings.warn(traceback.format_exc())
            continue

    result = pd.DataFrame(result)
    result["source"] = dataset_name
    result["split"] = "train"

    output_dir = here(f"data/processed/paraphrase_detection/{dataset_name}", warn=False)
    output_dir.mkdir(parents=True, exist_ok=True)
    for lang in sorted(result["lang"].unique()):
        result[result["lang"] == lang].to_json(
            output_dir / f"{lang.lower()}.jsonl",
            orient="records",
            lines=True,
        )


if __name__ == "__main__":
    make_dataset()
