import mdformat
import pandas as pd
import yaml
from pyprojroot import here

from eenlp.docs.languages import languages
from eenlp.docs.tasks import tasks

categories = [
    "named-entity-recognition-ner",
    "sentiment-analysis",
    "paraphrase-identification",
    "word-sense-disambiguation",
    "text-classification",
    "other",
]

columns = [
    "name",
    "description",
    "category",
    "languages",
    "links",
    "edit",
]


if __name__ == "__main__":
    df = []
    for dataset in here("docs/data/datasets/").glob("*.yml"):
        df.append(yaml.safe_load(dataset.read_text()))
        df[-1]["filename"] = dataset.name
    df = pd.DataFrame(df)

    with open(here("docs/datasets.md"), "w") as f:
        f.write("# Datasets\n\n")

        f.write("| | ")
        for category in categories:
            if category == "other":
                f.write("other |")
            else:
                f.write(
                    f" {tasks[category]['emoji']}<br>{tasks[category]['display_name']} |"
                )
        f.write("\n")
        f.write("| - | :-: | :-: | :-: | :-: | :-: | :-: |\n")
        for i, language in enumerate(languages):
            emoji_name = language["emoji_name"]
            language = language["name"]

            f.write(
                f"| **[:{emoji_name}:&nbsp;{language}](#{emoji_name}-{language.lower().replace('/', '')})** |"
            )
            for category in categories:
                if category == "other":
                    dff = df[
                        df["languages"].apply(lambda x: language in x)
                        & ~df["tasks"].apply(lambda x: any(y in categories for y in x))
                    ]
                else:
                    dff = df[
                        (df["languages"].apply(lambda x: language in x))
                        & (df["tasks"].apply(lambda x: category in x))
                    ]
                if len(dff):
                    f.write(f" [{len(dff)}](#{language.lower()}-{category})")
                f.write(" |")
            f.write("\n")
        f.write("\n")

        f.write("## :world_map: Legend\n")
        f.write(
            "- **Links**\n"
            "  - 🌐 URL\n"
            "  - 📄 paper\n"
            "  - ❞ citation\n"
            "  - ⬇️ download link\n"
            "  - 🤗️ huggingface datasets link\n"
            "- **Tasks**\n"
        )
        for task in tasks.values():
            f.write(f"  - **{task['emoji']} {task['display_name']}**\n")
            if "paperswithcode" in task:
                f.write(f"    - [Papers with Code]({task['paperswithcode']})")
            if "paperswithcode" in task and "wikipedia" in task:
                f.write(", ")
            if "wikipedia" in task:
                f.write(f"[Wikipedia]({task['wikipedia']})")
            if "paperswithcode" in task or "wikipedia" in task:
                f.write("\n")
            if len(task["description"]):
                f.write(f"    - {task['description']}\n")

        f.write("# Languages\n")

        for language in languages:
            emoji_name = language["emoji_name"]
            language = language["name"]

            f.write(f"## :{emoji_name}: {language}\n\n")

            f.write(
                f'<table width="100%"><thead><tr>'
                f'<th width="66%">name</th>'
                f'<th width="33%">description</th>'
                f"<th>tasks</th>"
                f"<th>languages</th>"
                f"<th>&nbsp;links&nbsp;&nbsp;</th>"
                f"<th>edit</th>"
                f"</tr></thead><tbody>"
            )
            for category in categories:
                if category == "other":
                    dff = df[
                        df["languages"].apply(lambda x: language in x)
                        & ~df["tasks"].apply(lambda x: any(y in categories for y in x))
                    ].sort_values("name", key=lambda x: x.str.lower())
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
                    ].sort_values("name", key=lambda x: x.str.lower())
                for i, (_, row) in enumerate(dff.iterrows()):
                    f.write("<tr>")
                    for column in columns:
                        if column == "name":
                            f.write(f"<td")
                            if i == 0:
                                f.write(f' id="{language.lower()}-{category}"')
                            f.write(f'><a href="{row["URL"]}">{row[column]}</a></td>')
                        elif column == "category":
                            f.write("<td><ul>")
                            for x in sorted(row["tasks"]):
                                if x in tasks:
                                    f.write(
                                        f'<li title="{tasks[x]["display_name"]}">{tasks[x]["emoji"]}</li>'
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
                            f.write("<td>")
                            if row["URL"] and row["URL"] != "?":
                                f.write(
                                    f'<div title="url"><a href="{row["URL"]}">🌐</a></div>'
                                )
                            if row["paper"] and row["paper"] != "?":
                                f.write(
                                    f'<div title="paper"><a href="{row["paper"]}">📄</a></div>'
                                )
                            if row["citation"] and row["citation"] != "?":
                                f.write(
                                    f'<div title="citation"><a href="{row["citation"]}">❞</a></div>'
                                )
                            if row["download link"] and row["download link"] != "?":
                                f.write(
                                    f'<div title="download link"><a href="{row["download link"]}">⬇️</a></div>'
                                )
                            if not pd.isna(row["huggingface"]):
                                f.write(
                                    f"<div>"
                                    f'<a title="huggingface dataset" href="{row["huggingface"]}">🤗️</a> '
                                    f'<a title="preview" href="https://huggingface.co/datasets/viewer/?dataset={row["huggingface"].split("/")[-1]}">🤗️</a>'
                                    f"</div>"
                                )
                            f.write("</td>")
                        elif column == "edit":
                            f.write(
                                f'<td><a href="https://github.com/altsoph/EENLP/edit/resources_page/docs/data/datasets/{row["filename"]}">edit</a></td>'
                            )
                        else:
                            f.write(f"<td>{row[column]}</td>")
                    f.write("</tr>\n")
            f.write("</tbody></table>\n\n")

    f = here("docs/datasets.md")
    mdformat.file(f, extensions={"gfm"})
