import pandas as pd
import yaml
from pyprojroot import here

from eenlp.docs.temp_generate_yamls import columns

languages = [
    "Albanian",
    "Armenian",
    "Belarusian",
    "Bosnian",
    "Bulgarian",
    "Croatian",
    "Czech",
    "Estonian",
    "Georgian",
    "Hungarian",
    "Kazakh",
    "Latvian",
    "Lithuanian",
    "Macedonian",
    "Moldovan/Moldovian",
    "Montenegrin",
    "Polish",
    "Romanian",
    "Russian",
    "Serbian",
    "Slovakian/Slovak",
    "Slovenian",
    "Ukrainian",
]

categories = [
    "ner",
    "sentiment",
    "paraphrase",
    "wsd",
    "category",
    "other",
]

category_captions = {
    "ner": "NER",
    "sentiment": "sentiment",
    "paraphrase": "paraphrase detection",
    "wsd": "WSD",
    "category": "category prediction",
    "other": "other",
}

if __name__ == "__main__":
    df = []
    for dataset in here("docs/data/datasets/").glob("*.yml"):
        df.append(yaml.safe_load(dataset.read_text()))
    df = pd.DataFrame(df)

    df = df.explode("category").explode("languages")

    with open(here("docs/datasets.md"), "w") as f:
        f.write("# Datasets x Languages Matrix\n\n")

        f.write(
            "| | NER<br>(named-entity recognition) | sentiment analysis | paraphrase detection | WSD<br>(word-sense disambiguation) | category prediction |\n"
        )
        f.write("| - | :-: | :-: | :-: | :-: | :-: |\n")
        for i, language in enumerate(languages):
            f.write(f"| **[{language}](#{language.lower().replace('/', '')})** | ")
            for category in categories:
                if category == "other":
                    break
                dff = df[(df["languages"] == language) & (df["category"] == category)]
                if len(dff):
                    f.write(
                        f" [{len(dff)}](#{category_captions[category].lower().replace(' ', '-')}{'-' + str(i) if i else ''})"
                    )
                f.write(" |")
            f.write("\n")
        f.write("\n")

        for language in languages:
            f.write(f"## {language}\n\n")
            for category in categories:
                f.write(f"### {category_captions[category]}\n\n")
                f.write(
                    "| name | description | task | URL | license | paper | citation | download link | comments |\n"
                )
                f.write("| - | - | - | - | - | - | - | - | - |\n")
                dff = df[
                    (df["languages"] == language) & (df["category"] == category)
                ].sort_values("name")
                for _, row in dff.iterrows():
                    f.write("|")
                    for column in columns:
                        f.write(f" {row[column]} |")
                    f.write("\n")
                f.write("\n")
