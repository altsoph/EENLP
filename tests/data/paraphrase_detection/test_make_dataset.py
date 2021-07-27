import pandas as pd
import pytest
from pyprojroot import here


@pytest.mark.parametrize(
    "filename",
    map(str, here("data/processed/paraphrase_detection").glob("**/*.jsonl")),
)
def test_datatest_valid_format(filename):
    expected = [
        "sentence1",
        "sentence2",
        "label",
        "lang",
        "source",
        "split",
    ]

    df = pd.read_json(filename, lines=True)
    actual = list(df)

    assert set(actual) == set(expected)
    assert not df.iloc[0].isna().any()
