from typing import List, TypedDict


class Language(TypedDict):
    name: str
    emoji_name: str


languages: List[Language] = [
    {"name": "Albanian", "emoji_name": "albania"},
    {"name": "Armenian", "emoji_name": "armenia"},
    {"name": "Belarusian", "emoji_name": "belarus"},
    {"name": "Bosnian", "emoji_name": "bosnia_herzegovina"},
    {"name": "Bulgarian", "emoji_name": "bulgaria"},
    {"name": "Croatian", "emoji_name": "croatia"},
    {"name": "Czech", "emoji_name": "czech_republic"},
    {"name": "Estonian", "emoji_name": "estonia"},
    {"name": "Georgian", "emoji_name": "georgia"},
    {"name": "Hungarian", "emoji_name": "hungary"},
    {"name": "Kazakh", "emoji_name": "kazakhstan"},
    {"name": "Latvian", "emoji_name": "latvia"},
    {"name": "Lithuanian", "emoji_name": "lithuania"},
    {"name": "Macedonian", "emoji_name": "macedonia"},
    {"name": "Moldovan", "emoji_name": "moldova"},
    {"name": "Montenegrin", "emoji_name": "montenegro"},
    {"name": "Polish", "emoji_name": "poland"},
    {"name": "Romanian", "emoji_name": "romania"},
    {"name": "Russian", "emoji_name": "ru"},
    {"name": "Serbian", "emoji_name": "serbia"},
    {"name": "Slovakian", "emoji_name": "slovakia"},
    {"name": "Slovenian", "emoji_name": "slovenia"},
    {"name": "Ukrainian", "emoji_name": "ukraine"},
]
