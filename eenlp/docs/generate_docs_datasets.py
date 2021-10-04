import mdformat
import pandas as pd
import yaml
from pyprojroot import here

from eenlp.docs.dataset_tasks import tasks
from eenlp.docs.languages import languages

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
    # "description",
    "category",
    "languages",
    "links",
    "edit",
]


def generate():
    df = []
    for dataset in here("docs/data/datasets/").glob("*.yml"):
        df.append(
            {
                **yaml.safe_load(dataset.read_text()),
                "filename": dataset.name,
            }
        )
    df = pd.DataFrame(df)

    with open(here("docs/datasets.md"), "w") as f:
        f.write("# Datasets\n\n")
        f.write(f"total: {len(df)}\n\n")
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

            if not len(df[df["languages"].apply(lambda x: language in x)]):
                continue

            f.write(
                f"| **[{language}](#{emoji_name}-{language.lower().replace('/', '')})** |"
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
        for task_name, task in tasks.items():
            f.write(
                f'  - <b id="{task_name}">{task["emoji"]} {task["display_name"]}</b>\n'
            )
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

            if not len(df[df["languages"].apply(lambda x: language in x)]):
                continue

            f.write(f"## :{emoji_name}: {language}\n\n")

            f.write(
                f'<table width="100%"><thead><tr>'
                f'<th width="66%">name</th>'
                # f'<th width="33%">description</th>'
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
                            f.write(f'><a href="{row["URL"]}">{row[column]}')
                            if not pd.isna(row["full name"]):
                                f.write(f" ({row['full name']})")
                            f.write(f"</a></td>")
                        elif column == "category":
                            f.write("<td><ul>")
                            for x in sorted(row["tasks"]):
                                if x in tasks:
                                    f.write(
                                        f'<li title="{tasks[x]["display_name"]}"><a href="#{x}">{tasks[x]["emoji"]}</a></li>'
                                    )
                                else:
                                    f.write(f'<li title="{x}">{x}</li>')
                            f.write("</ul></td>")
                        elif column == "languages":
                            f.write("<td>")
                            for x in sorted(row["languages"]):
                                y = next(y for y in languages if y["name"] == x)
                                f.write(
                                    f'<span title="{x}"><a href="#{y["emoji_name"]}-{y["name"]}">:{y["emoji_name"]}:</a></span> '
                                )
                            f.write("</td>")
                        elif column == "links":
                            links_used = set()
                            f.write("<td>")
                            if (
                                row["URL"]
                                and row["URL"] != "?"
                                and row["URL"] not in links_used
                            ):
                                links_used.add(row["URL"])
                                f.write(
                                    f'<div title="url"><a href="{row["URL"]}">🌐</a></div>'
                                )
                            if (
                                row["paper"]
                                and row["paper"] != "?"
                                and row["paper"] not in links_used
                            ):
                                links_used.add(row["paper"])
                                f.write(
                                    f'<div title="paper"><a href="{row["paper"]}">📄</a></div>'
                                )
                            if (
                                row["citation"]
                                and row["citation"] != "?"
                                and row["citation"] not in links_used
                            ):
                                links_used.add(row["citation"])
                                f.write(
                                    f'<div title="citation"><a href="{row["citation"]}">❞</a></div>'
                                )
                            if (
                                row["download link"]
                                and row["download link"] != "?"
                                and row["download link"] not in links_used
                            ):
                                links_used.add(row["download link"])
                                f.write(
                                    f'<div title="download link"><a href="{row["download link"]}">⬇️</a></div>'
                                )
                            if (
                                not pd.isna(row["huggingface"])
                                and row["huggingface"] not in links_used
                            ):
                                links_used.add(row["huggingface"])
                                f.write(
                                    f"<div>"
                                    f'<a title="huggingface dataset" href="{row["huggingface"]}">🤗️</a> '
                                    f'<a title="preview" href="https://huggingface.co/datasets/viewer/?dataset={row["huggingface"].split("/")[-1]}">🤗️</a>'
                                    f"</div>"
                                )
                            f.write("</td>")
                        elif column == "edit":
                            f.write(
                                f'<td><a href="https://github.com/altsoph/EENLP/edit/main/docs/data/datasets/{row["filename"]}">edit</a></td>'
                            )
                        else:
                            f.write(f"<td>{row[column]}</td>")
                    f.write("</tr>\n")
            f.write("</tbody></table>\n\n")

    f = here("docs/datasets.md")
    mdformat.file(f, extensions={"gfm"})


if __name__ == "__main__":
    generate()
