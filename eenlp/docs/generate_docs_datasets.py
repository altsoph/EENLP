from typing import Dict, Optional, TypedDict

import mdformat
import pandas as pd
import yaml
from pyprojroot import here

from eenlp.docs.generate_docs_models import languages

categories = [
    "named-entity-recognition-ner",
    "sentiment-analysis",
    "paraphrase-identification",
    "word-sense-disambiguation",
    "text-classification",
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

columns = [
    "name",
    "description",
    "task",
    "category",
    "languages",
    "links",
]

category_icons = {
    "ner": "📛",
    "sentiment": "😄",
    "paraphrase": "💬",
    "wsd": "🐁🖱",
    "category": "📰",
    "other": "🦦",
}


class Task(TypedDict):
    name: str
    display_name: str
    paperswithcode: str
    description: Optional[str]
    emoji: str


tasks: Dict[str, Task] = {
    "named-entity-recognition-ner": {
        "name": "named-entity-recognition-ner",
        "display_name": "NER",
        "paperswithcode": "https://paperswithcode.com/task/named-entity-recognition-ner",
        "description": "",
        "emoji": "📛",
    },
    "sentiment-analysis": {
        "name": "sentiment-analysis",
        "display_name": "sentiment",
        "emoji": "😄",
    },
    "paraphrase-identification": {
        "name": "paraphrase-identification",
        "display_name": "paraphrase",
        "emoji": "💬",
    },
    "word-sense-disambiguation": {
        "name": "word-sense-disambiguation",
        "display_name": "WSD",
        "emoji": "🐁🖱",
    },
    "text-classification": {
        "name": "text-classification",
        "display_name": "category",
        "emoji": "📰",
    },
    "part-of-speech-tagging": {
        "name": "other",
        "emoji": "🦦",
        "display_name": "other",
    },
    "wordnet": {
        "name": "other",
        "emoji": "🦦",
        "display_name": "other",
    },
    "other": {
        "emoji": "🦦",
        "display_name": "other",
    },
}

if __name__ == "__main__":
    df = []
    for dataset in here("docs/data/datasets/").glob("*.yml"):
        df.append(yaml.safe_load(dataset.read_text()))
    df = pd.DataFrame(df)

    # df = df.explode("category").explode("languages")

    with open(here("docs/datasets.md"), "w") as f:
        f.write("# Datasets\n\n")

        f.write(
            "| | NER<br>(named-entity recognition) | sentiment analysis | paraphrase detection | WSD<br>(word-sense disambiguation) | category prediction |\n"
        )
        f.write("| - | :-: | :-: | :-: | :-: | :-: |\n")
        for i, language in enumerate(languages):
            emoji_name = language["emoji_name"]
            language = language["name"]

            f.write(
                f"| **[:{emoji_name}:&nbsp;{language}](#{emoji_name}-{language.lower().replace('/', '')})** |"
            )
            for category in categories:
                if category == "other":
                    continue
                dff = df[
                    (df["languages"].apply(lambda x: language in x))
                    & (df["tasks"].apply(lambda x: category in x))
                ]
                if len(dff):
                    f.write(f" [{len(dff)}](#{language.lower()}-{category})")
                f.write(" |")
            f.write("\n")
        f.write("\n")

        for language in languages:
            emoji_name = language["emoji_name"]
            language = language["name"]

            f.write(f"## :{emoji_name}: {language}\n\n")

            f.write(
                f'<table width="100%"><thead><tr>'
                f'<th width="66%">name</th>'
                f'<th width="33%">description</th>'
                f"<th>task</th>"
                f"<th>category</th>"
                f"<th>languages</th>"
                f"<th>links</th>"
                f"</tr></thead><tbody>"
            )
            for category in categories:
                if category == "other":
                    dff = df[
                        df["languages"].apply(lambda x: language in x)
                        & ~df["tasks"].apply(lambda x: any(y in categories for y in x))
                    ].sort_values("name")
                else:
                    dff = df[
                        (df["languages"].apply(lambda x: language in x))
                        & (
                            df["tasks"].apply(
                                # TODO probably could be written simpler
                                lambda x: category in x
                                and [y for y in x if y in categories][0] == category
                            )
                        )
                    ].sort_values("name")
                for i, (_, row) in enumerate(dff.iterrows()):
                    f.write("<tr>")
                    for column in columns:
                        if column == "name":
                            f.write(f"<td")
                            if i == 0:
                                f.write(f' id="{language.lower()}-{category}"')
                            f.write(f'><a href="{row["URL"]}">{row[column]}</a></td>')
                        elif column == "category":
                            # f.write(
                            #     f'<td><ul><li title="{category}">{tasks[category]["emoji"]}</li></ul></td>'
                            # )
                            f.write("<td><ul>")
                            for x in sorted(row["tasks"]):
                                if x in tasks:
                                    f.write(
                                        f'<li title="{tasks[x]["name"]}">{tasks[x]["emoji"]}</li>'
                                    )
                                else:
                                    f.write(f'<li title="{x}">{x}</li>')
                            f.write("</ul></td>")
                        elif column == "languages":
                            f.write("<td>")
                            for x in sorted(row["languages"]):
                                f.write(
                                    f'<span title="{x}">:{next(y["emoji_name"] for y in languages if y["name"] == x)}:</span> '
                                )
                            f.write("</td>")
                        elif column == "links":
                            f.write("<td><ul>")
                            if row["URL"] and row["URL"] != "?":
                                f.write(
                                    f'<li title="url"><a href="{row["URL"]}">🌐</a></li>'
                                )
                            if row["paper"] and row["paper"] != "?":
                                f.write(
                                    f'<li title="paper"><a href="{row["paper"]}">📄</a></li>'
                                )
                            if row["citation"] and row["citation"] != "?":
                                f.write(
                                    f'<li title="citation"><a href="{row["citation"]}">❞</a></li>'
                                )
                            if row["download link"] and row["download link"] != "?":
                                f.write(
                                    f'<li title="download link"><a href="{row["download link"]}">⬇️</a></li>'
                                )
                            # if not pd.isna(row["huggingface"]):
                            #     f.write(
                            #         f"<li>"
                            #         f'<a title="huggingface dataset" href="{row["huggingface"]}">🤗️</a> '
                            #         f'<a title="preview" href="https://huggingface.co/datasets/viewer/?dataset={row["huggingface"].split("/")[-1]}">🤗️</a>'
                            #         f"</li>"
                            #     )
                            f.write("</ul></td>")
                        else:
                            f.write(f"<td>{row[column]}</td>")
                    f.write("</tr>\n")
            f.write("</tbody></table>\n\n")

    f = here("docs/datasets.md")

    f.write_text(
        f.read_text()
        .replace("named-entity-recognition-ner", "ner")
        .replace("sentiment-analysis", "sentiment")
        .replace("paraphrase-identification", "paraphrase")
        .replace("word-sense-disambiguation", "wsd")
        .replace("text-classification", "category")
    )

    mdformat.file(f, extensions={"gfm"})
