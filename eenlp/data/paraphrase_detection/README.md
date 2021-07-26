# paraphrase_detection

## Datasets

- [ ] tapaco
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

## Setup

The following is a possible way to set up this project, using Anaconda or Miniconda environment manager.

```bash
cd <project dir>
conda create -n eenlp "python==3.8.*"
conda activate eenlp
python -m pip install -r requirements.txt
# this makes the current project importable (as eenlp)
python -m pip install -e .
```
