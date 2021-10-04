from typing import Dict, Optional, TypedDict


class Task(TypedDict):
    display_name: str
    paperswithcode: Optional[str]
    wikipedia: Optional[str]
    description: Optional[str]
    emoji: str


tasks: Dict[str, Task] = {
    "named-entity-recognition-ner": {
        "display_name": "Named-entity recognition",
        "emoji": ":name_badge:",
        "description": "",
        "paperswithcode": "https://paperswithcode.com/task/named-entity-recognition-ner",
        "wikipedia": "https://en.wikipedia.org/wiki/Named-entity_recognition",
    },
    "sentiment-analysis": {
        "display_name": "Sentiment analysis",
        "emoji": ":smile:",
        "description": "",
        "paperswithcode": "https://paperswithcode.com/task/sentiment-analysis",
    },
    "paraphrase-identification": {
        "display_name": "Paraphrase identification",
        "emoji": ":speech_balloon::speech_balloon:",
        "description": "",
        "paperswithcode": "https://paperswithcode.com/task/paraphrase-identification",
    },
    "word-sense-disambiguation": {
        "display_name": "Word-sense disambiguation",
        "emoji": ":mouse2::computer_mouse:",
        "description": "",
        "paperswithcode": "https://paperswithcode.com/task/word-sense-disambiguation",
    },
    "text-classification": {
        "display_name": "Text classification",
        "emoji": ":newspaper:",
        "description": "",
        "paperswithcode": "https://paperswithcode.com/task/text-classification",
    },
    "part-of-speech-tagging": {
        "display_name": "Part-of-speech tagging",
        "emoji": ":evergreen_tree:",
        "description": "",
        "paperswithcode": "https://paperswithcode.com/task/part-of-speech-tagging",
    },
    "wordnet": {
        "display_name": "Wordnet",
        "emoji": ":book:",
        "description": "",
    },
}
