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

columns = [
    "name",
    "description",
    "task",
    "category",
    "languages",
    "links",
]

flags = {
    "Albanian": "🇦🇱",
    "Armenian": "🇦🇲",
    "Belarusian": "🇧🇾",
    "Bosnian": "🇧🇦",
    "Bulgarian": "🇧🇬",
    "Croatian": "🇭🇷",
    "Czech": "🇨🇿",
    "Estonian": "🇪🇪",
    "Georgian": "🇬🇪",
    "Hungarian": "🇭🇺",
    "Kazakh": "🇰🇿",
    "Latvian": "🇱🇻",
    "Lithuanian": "🇱🇹",
    "Macedonian": "🇲🇰",
    "Moldovan/Moldovian": "🇲🇩",
    "Montenegrin": "🇲🇪",
    "Polish": "🇵🇱",
    "Romanian": "🇷🇴",
    "Russian": "🇷🇺",
    "Serbian": "🇷🇸",
    "Slovakian/Slovak": "🇸🇰",
    "Slovenian": "🇸🇮",
    "Ukrainian": "🇺🇦",
}

category_icons = {
    "ner": "📛",
    "sentiment": "😄",
    "paraphrase": "💬",
    "wsd": "🐁🖱",
    "category": "📰",
    "other": "🦦",
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
            f.write(
                f"| **[{flags[language]}&nbsp;{language}](#-{language.lower().replace('/', '')})** |"
            )
            for category in categories:
                if category == "other":
                    continue
                dff = df[(df["languages"] == language) & (df["category"] == category)]
                if len(dff):
                    f.write(f" [{len(dff)}](#{language.lower()}-{category})")
                f.write(" |")
            f.write("\n")
        f.write("\n")

        for language in languages:
            # lang_stuff = pycountry.countries.search_fuzzy(language)
            f.write(f"## {flags[language]} {language}\n\n")

            f.write(
                f'<table width="100%"><thead><tr>'
                f'<th width="66%">name</th>'
                f'<th width="33%">description</th>'
                f"<th>task</th>"
                f"<th>category</th>"
                f'<th>languages</th>'
                f"<th>links</th>"
                f"</tr></thead><tbody>"
            )
            for category in categories:
                # f.write(f"### {category_captions[category]}\n\n")
                # f.write(f"| {' | '.join(columns)} |\n|{'-|' * len(columns)}\n")
                dff = df[
                    (df["languages"] == language) & (df["category"] == category)
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
                            f.write(
                                f'<td><ul><li title="{category}">{category_icons[category]}</li></ul></td>'
                            )
                        elif column == "languages":
                            f.write("<td>")
                            for x in sorted(
                                df[(df["name"] == row["name"])]["languages"].unique()
                            ):
                                f.write(f'<span title="{x}">{flags[x]}</span> ')
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
                            if not pd.isna(row["huggingface"]):
                                f.write(
                                    f"<li>"
                                    f'<a title="huggingface dataset" href="{row["huggingface"]}">🤗️</a> '
                                    f'<a title="preview" href="https://huggingface.co/datasets/viewer/?dataset={row["huggingface"].split("/")[-1]}">🤗️</a>'
                                    f"</li>"
                                )
                            f.write("</ul></td>")
                        else:
                            f.write(f"<td>{row[column]}</td>")
                    f.write("</tr>\n")
            f.write("</tbody></table>\n\n")

    mdformat.file(here("docs/datasets.md"), extensions={"gfm"})
