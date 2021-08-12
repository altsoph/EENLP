import mdformat
import pandas as pd
import yaml
from pyprojroot import here

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
    "multilingual-global",
    "multilingual-local",
    "single-language",
    "other",
]

category_captions = {
    "multilingual-global": "multilingual",
    "multilingual-local": "several languages",
    "single-language": "single language models",
    "other": "other",
}

columns = [
    "name",
    "description",
    "huggingface",
    "type",
    "paper",
    "citation",
    "cased",
    "pre-trained on",
    "comments",
]

if __name__ == "__main__":
    df = []
    for dataset in here("docs/data/models/").glob("*.yml"):
        df.append(yaml.safe_load(dataset.read_text()))
    df = pd.DataFrame(df)

    df = df.explode("languages")

    with open(here("docs/models.md"), "w") as f:
        f.write("# Models\n\n")

        for language in languages:
            f.write(f"## {language}\n\n")
            for category in categories:
                f.write(f"### {category_captions[category]}\n\n")
                f.write(
                    f"| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |\n|{'-|' * len(columns)}\n"
                )
                dff = df[
                    (df["languages"] == language) & (df["category"] == category)
                ].sort_values("name")
                for i, (_, row) in enumerate(dff.iterrows()):
                    f.write("| ")
                    for column in columns:
                        f.write(row[column] + " |")
                    f.write("\n")
                f.write("\n\n")

    mdformat.file(here("docs/models.md"), extensions={"gfm"})
