from typing import Dict, TypedDict


class Common(TypedDict):
    emoji: str
    image: str


types: Dict[str, Common] = {
    "BERT": {
        "image": "/docs/images/icons/bert.jpg",
    },
    "RoBERTa": {
        "emoji": "🤖",
    },
    "ELMo": {
        "image": "/docs/images/icons/elmo.jpg",
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

corpora: Dict[str, Common] = {
    "common crawl": {
        "emoji": "🕷",
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
