# paraphrase_detection

## Datasets

- [x] tapaco
    - https://huggingface.co/datasets/tapaco
- [x] arpa
    - https://github.com/ivannikov-lab/arpa-paraphrase-corpus
- [x] klej_cdsc_r
    - https://klejbenchmark.com/tasks/
- [x] ro_sts
    - https://github.com/dumitrescustefan/RO-STS
- [x] paraphrase_sr
    - https://github.com/vukbatanovic/paraphrase.sr

## Schema

- columns
    - sentence1
        - Text.
    - sentence2
        - Text.
    - label
        - `0`: not paraphrases.
        - `1`: paraphrases.
    - lang
        - Full name of the language, capitalized, e.g. "English".
    - source
        - Dataset name, from the "Datasets" section above.
    - split
        - E.g. "train", "test".

