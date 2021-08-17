from typing import Dict, TypedDict


class Common(TypedDict):
    emoji: str
    image: str


types: Dict[str, Common] = {
    "BERT": {
        "image": "/docs/images/icons/bert.png",
    },
    "RoBERTa": {
        "emoji": "🤖",
    },
    "ELMo": {
        "emoji": "🔥",
    },
    "GPT2": {
        "emoji": "🦄",
    },
    "DistilBERT": {
        "emoji": "💧",
    },
    "Electra": {
        "emoji": "⚡️",
    },
    "static word embeddings": {
        "emoji": "🧤",
    },
}

cases: Dict[str, Common] = {
    "cased": {
        "emoji": "🔠",
    },
    "uncased": {
        "emoji": "🔡",
    },
    "both": {
        "emoji": "🔡🔠",
    },
}

# TODO use aliases
corpora: Dict[str, Common] = {
    "cc": {
        "emoji": "🕷",
    },
    "common crawl": {
        "emoji": "🕷",
    },
    "wiki": {
        "emoji": "🌐",
    },
    "wikipedia": {
        "emoji": "🌐",
    },
    "news": {
        "emoji": "📰",
    },
    "subtitles": {
        "emoji": "🎞",
    },
}
