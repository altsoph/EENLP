from typing import Dict

import mdformat
import pandas as pd
import yaml
from pyprojroot import here

from eenlp.docs.languages import Language, languages
from eenlp.docs.model_types import Common, cases, types

columns = [
    "name",
    # "description",
    "type",
    "cased",
    "languages",
    "pre-trained on",
    "links",
    "edit",
]

# Columns for the index table on the top.
# There is filtering for *both* the number of languages and these categories, so that e.g. static word embeddings won't
# show up in the index table.
# currently:
#   - single == 1
#   - 1 < few < 10
#   - 10 <= multi

# multilang_models = [
#     "BERT",
#     "RoBERTa",
#     "DistilBERT",
#     "Electra",
#     "ALBERT",
#     "mBERT",
#     "XLM-RoBERTa",
# ]

few_language_models = [
    "BERT",
    "RoBERTa",
    "DistilBERT",
    "Electra",
    "ALBERT",
    "XLM-RoBERTa",
    "BERT/Electra(?)",
]

single_language_models = [
    "BERT",
    "RoBERTa",
    "DistilBERT",
    "Electra",
    "ALBERT",
]


def image_or_emoji(name: str, base_type: Dict[str, Common]) -> str:
    item = base_type[name]
    if "image" in item:
        return f'<img width="21px" height="21px" title="{name}" src="{item["image"]}">'
    else:
        return item["emoji"]


def is_language_empty(df: pd.DataFrame, language: Language) -> bool:
    return not len(
        df[
            df.apply(
                lambda x: x["languages"] == language["name"]
                and len(df[df.index == x.name]) < 10,
                axis=1,
            )
        ]
    )


def generate():
    df = []
    for dataset in here("docs/data/models/").glob("*.yml"):
        df.append(
            {
                **yaml.safe_load(dataset.read_text()),
                "filename": dataset.name,
            }
        )
    df = pd.DataFrame(df)

    df_o = df

    df = df.explode("languages")

    few_langs_models = [
        x[0]
        for x in df.sort_values("name").groupby(df.index)["languages"].count().items()
        if 1 < x[1] < 10
    ]
    few_langs_models = [
        x for x in few_langs_models if df.loc[x].iloc[0]["type"] in few_language_models
    ]

    with open(here("docs/models.md"), "w") as f:
        f.write("# Models\n\n")
        f.write(f"total: {len(df_o)}\n\n")

        # multilang

        f.write("<table><thead>")
        f.write(
            f'<tr><td align="center"><td width="100%" align="center"><b>multilingual (transformers)</b></td></tr></thead><tbody>\n'
        )
        f.write(
            f'<tr><td><a href="#earth_africa-multilingual"><b>Multilingual</b></a></td><td align="center">'
        )
        dff = df_o[
            (
                df_o.apply(
                    lambda x: 10 <= len(x["languages"]),
                    # and x["type"] in multilang_models,
                    axis=1,
                )
            )
        ]
        f.write(
            " / ".join(
                sorted(
                    f'<a href="#{x.name.lower().replace(" ", "-")}-multilingual">{x.name}</a>'
                    for x in dff.itertuples()
                )
            )
        )
        f.write("</td></tr></tbody></table>\n\n")

        f.write("<table><thead>")
        f.write(
            f'<tr><td align="center"><td width="100%" align="center" colspan="{len(few_langs_models)}"><b>several languages (transformers)</b></td></tr>'
        )
        f.write("<tr><td></td>")

        f.write(
            "".join(
                f'<td align="center"><b>{x}</b></td>'
                for x in df.loc[few_langs_models]["name"].unique()
            )
        )
        f.write("</tr></thead><tbody>\n")

        for i, language in enumerate(languages):
            if is_language_empty(df, language):
                continue

            emoji_name = language["emoji_name"]
            language = language["name"]

            f.write(
                f'<tr><td><a href="#{emoji_name}-{language.lower().replace("/", "")}"><b>{language}</b></a></td>'
            )

            for i in few_langs_models:
                f.write('<td align="center">')
                dff = df[(df.index == i) & (df["languages"] == language)]
                if len(dff):
                    f.write(
                        f'<a href="#{dff["name"].item().lower().replace(" ", "-")}-{language}">{dff["name"].item()}</a>'
                    )
                f.write("</td>")
            f.write("</tr>\n")
        f.write("</tbody></table>\n\n")

        # single lang

        f.write("<table><thead>")
        f.write(
            f'<tr><td></td><td width="100%" align="center" colspan="5"><b>single-language models</b></td></tr>'
        )
        f.write("<tr><td></td>")

        f.write(
            '<td align="center">BERT</td><td align="center"><b>RoBERTa</b></td><td align="center"><b>DistilBERT</b></td><td align="center"><b>Electra</b></td><td align="center"><b>ALBERT</b></td>'
        )
        f.write("</tr></thead><tbody>\n")

        for i, language in enumerate(languages):
            if is_language_empty(df, language):
                continue

            emoji_name = language["emoji_name"]
            language = language["name"]

            f.write(
                f'<tr><td><a href="#{emoji_name}-{language.lower().replace("/", "")}"><b>{language}</b></a></td>'
            )

            for model_name in single_language_models:
                f.write('<td align="center">')
                dff = df[
                    df.apply(
                        lambda x: x["languages"] == language
                        and x["type"] == model_name
                        and len(df[df.index == x.name]) == 1,
                        axis=1,
                    )
                ]
                if len(dff):
                    f.write(
                        " / ".join(
                            sorted(
                                f'<a href="#{x.lower().replace(" ", "-")}-{language}">{x}</a>'
                                for x in dff["name"]
                            )
                        )
                    )
                f.write("</td>")
            f.write("</tr>\n")
        f.write("</tbody></table>\n\n")

        f.write("## :world_map: Legend\n")
        f.write("- **Type**\n")
        for item_name in types:
            f.write(
                f'  - <b id="{item_name}">{image_or_emoji(item_name, types)} {item_name}</b>\n'
            )
        f.write("- **Cased**\n")
        for item_name in cases:
            f.write(
                f'  - <b id="{item_name}">{image_or_emoji(item_name, cases)} {item_name}</b>\n'
            )
        # f.write("- **Pre-training corpora**\n")
        # for item_name in corpora:
        #     f.write(
        #         f'  - <b id="{item_name}">{image_or_emoji(item_name, corpora)} {item_name}</b>\n'
        #     )
        f.write(
            "- **Links**\n"
            "  - 📄 paper\n"
            "  - ❞ citation\n"
            "  - 🤗️ huggingface model card\n"
            "  - 🌐 URL\n"
        )

        f.write("# Languages\n")

        for language in ["Multilingual"] + languages:
            if language == "Multilingual":
                emoji_name = "earth_africa"
            else:
                if is_language_empty(df, language):
                    continue
                emoji_name = language["emoji_name"]
                language = language["name"]

            f.write(f"## :{emoji_name}: {language}\n\n")

            if language == "Multilingual":
                dff = df_o[df_o["languages"].str.len() >= 10]
            else:
                dff = df_o[
                    (df_o["languages"].apply(lambda x: language in x))
                    & (df_o["languages"].str.len() < 10)
                ]

            f.write(
                '<table width="100%"><thead><tr>'
                '<th width="66%">name</th>'
                # '<th width="33%">description</th>'
                "<th>type</th>"
                "<th>cased</th>"
                "<th>languages</th>"
                # "<th>corpora</th>"
                "<th>links</th>"
                "<th>edit</th>"
                "</tr></thead><tbody>\n"
            )
            for _, row in sorted(dff.iterrows(), key=lambda x: x[1]["name"].lower()):
                f.write("<tr>")
                for column in columns:
                    if column == "name":
                        f.write(f"<td")
                        f.write(
                            f' id="{row["name"].lower().replace(" ", "-")}-{language}"'
                        )
                        f.write(f">{row[column]}</td>")
                    elif column == "languages":
                        f.write("<td>")
                        for x in sorted(
                            df[(df["name"] == row["name"])]["languages"].unique()
                        ):
                            y = next(y for y in languages if y["name"] == x)
                            f.write(
                                f'<span title="{x}"><a href="#{y["emoji_name"]}-{y["name"]}">:{y["emoji_name"]}:</a></span> '
                            )
                        f.write("</td>")
                    elif column == "links":
                        links_used = set()
                        f.write("<td>")
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
                            not pd.isna(row["huggingface"])
                            and row["huggingface"] not in links_used
                        ):
                            links_used.add(row["huggingface"])
                            f.write(
                                f"<div>"
                                f'<a title="huggingface model card" href="{row["huggingface"]}">🤗️</a> '
                                f"</div>"
                            )
                        if (
                            not pd.isna(row["URL"])
                            and row["URL"]
                            and row["URL"] != "?"
                            and row["URL"] not in links_used
                        ):
                            links_used.add(row["URL"])
                            f.write(
                                f'<div title="url"><a href="{row["URL"]}">🌐</a></div>'
                            )
                        f.write("</td>")
                    elif column == "pre-trained on":
                        # f.write("<td><ul>")
                        # if isinstance(row["pre-trained on"], list):
                        #     for x in sorted(row["pre-trained on"]):
                        #         if x != "" and x != "?":
                        #             if x in corpora:
                        #                 f.write(
                        #                     f'<li title="{x}"><a href="#{x}">{image_or_emoji(x, corpora)}</a></li>'
                        #                 )
                        #             else:
                        #                 f.write(f'<li title="{x}">{x}</li>')
                        # f.write("</ul></td>")
                        pass
                    elif column == "type":
                        if row["type"] in types:
                            f.write(
                                f'<td align="center"><div title="{row["type"]}"><a href="#{row["type"]}">{image_or_emoji(row["type"], types)}</a></div></td>'
                            )
                        else:
                            f.write(f"<td>{row['type']}</td>")
                    elif column == "cased":
                        if row["cased"] in cases:
                            f.write(
                                f'<td><div title="{row["cased"]}"><a href="#{row["cased"]}">{image_or_emoji(row["cased"], cases)}</a></div></td>'
                            )
                        else:
                            f.write(f"<td>{row['cased']}</td>")
                    elif column == "edit":
                        f.write(
                            f'<td><a href="https://github.com/altsoph/EENLP/edit/main/docs/data/models/{row["filename"]}">edit</a></td>'
                        )
                    else:
                        f.write(f"<td>{row[column]}</td>")
                f.write("</tr>\n")
            f.write("</tbody></table>\n\n")
            if language != "Multilingual":
                f.write(
                    "&nbsp;&nbsp;&nbsp;[+ multilingual](#earth_africa-multilingual)"
                )
            f.write("\n\n")

    mdformat.file(here("docs/models.md"), extensions={"gfm"})


if __name__ == "__main__":
    generate()
