# paraphrase_detection

## Datasets

- [x] tapaco
    - https://huggingface.co/datasets/tapaco
    - :page_facing_up: [TaPaCo: A Corpus of Sentential Paraphrases for 73 Languages](https://aclanthology.org/2020.lrec-1.848/)
    - :balance_scale: cc-by-2.0
- [x] arpa
    - https://github.com/ivannikov-lab/arpa-paraphrase-corpus
    - :page_facing_up: [ARPA: Armenian Paraphrase Detection Corpus and Models](https://arxiv.org/abs/2009.12615)
    - :balance_scale: apache 2.0
- [x] klej_cdsc_r
    - https://klejbenchmark.com/tasks/
    - :page_facing_up: [KLEJ: Comprehensive Benchmark for Polish Language Understanding](https://arxiv.org/abs/2005.00630)
    - :balance_scale: GNU GPL v3
- [x] ro_sts
    - https://github.com/dumitrescustefan/RO-STS
    - :balance_scale: CC BY-SA 4.0
- [x] paraphrase_sr
    - https://github.com/vukbatanovic/paraphrase.sr
    - :page_facing_up: [Semantic similarity of short texts in languages with a deficient natural language processing support](https://www.sciencedirect.com/science/article/abs/pii/S0167923613000614)
    - :balance_scale: CC BY-NC-SA 4.0

## Columns

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

## Details

### Generate dataset

The environment should be set up, see [docs/developer.md](../../../docs/developer.md).

```bash
conda activate eenlp

python eenlp/data/paraphrase_detection/make_dataset.py
```

This script generates every paraphrase detection dataset by running the corresponding scripts, then aggregates all of
them into `data/processed/paraphrase_detection/`.

The script for the tapaco dataset is slow, it can take ~30 mins to run.

### Construction details

We describe here how the dataset was constructed. First, the input datasets were brought to the same format, then they
were merged into one.

Depending on the dataset, more or less transformations were required to get to the same format (which is, one sentence
pair per row, with the label "paraphrase" or "not paraphrase"), these are described in this section.

We use "train" sets, unless noted otherwise.

#### Arpa

See [make_dataset_arpa.py](make_dataset_arpa.py)

"labelled as either paraphrase, near paraphrase or non-paraphrase (with 1, 0, -1 labels respectively)"

https://github.com/ivannikov-lab/arpa-paraphrase-corpus/blob/02fcbc70a36fdd3d8e8eefb226d41e2cb9519aa7/README.md

We treat "1" as paraphrases, and "0" and "-1" as not paraphrases.

#### Glue_mrpc

See [make_dataset_glue_mrpc.py](make_dataset_glue_mrpc.py)

It's already in the common format.

#### Glue_qqp

See [make_dataset_glue_qqp.py](make_dataset_glue_qqp.py)

It's already in the common format.

#### Glue_stsb

See [make_dataset_glue_stsb.py](make_dataset_glue_stsb.py)

Similarity scores

| Score | Explanation |
|---|---|
|5|The two sentences are completely equivalent, as they mean the same thing.|
|4|The two sentences are mostly equivalent, but some unimportant details differ.|
|3|The two sentences are roughly equivalent, but some important information differs/missing.|
|2|The two sentences are not equivalent, but share some details.|
|1|The two sentences are not equivalent, but are on the same topic.|
|0|The two sentences are completely dissimilar.|

[SemEval-2017 Task 1: Semantic Textual Similarity - Multilingual and Cross-lingual Focused Evaluation](https://arxiv.org/abs/1708.00055)
, Table 1

Transcription rule, "4" and "5": paraphrases, <4: not paraphrases.

#### Klej_cdsc_r

See [make_dataset_klej_cdsc_r.py](make_dataset_klej_cdsc_r.py)

- 5 (very related)
- 1–4 (more or less related)
- 0 (unrelated)

[Polish evaluation dataset for compositional distributional semantics models](https://aclanthology.org/P17-1073/),
Section 3.1

Transcription rule, "4" and "5": paraphrases, <4: not paraphrases.

We assume that the thresholds are similar to [Glue_stsb](#Glue_stsb).

See [make_dataset_paraphrase_sr.py](make_dataset_paraphrase_sr.py)

It's already in the common format.

#### Ro_sts

See [make_dataset_ro_sts.py](make_dataset_ro_sts.py)

Labels mean the same as in [Glue_stsb](#Glue_stsb).

Transcription rule, "4" and "5": paraphrases, <4: not paraphrases.

#### Tapaco

See [make_dataset_tapaco.py](make_dataset_tapaco.py)

TaPaCo doesn't have a "pairs of examples" format (like in GLUE), but a "sets of paraphrases" kind of format (
similar to WordNet synsets).

We need to generate example pairs somehow.  
As of the current version of the code, 50% of the generated examples are true paraphrases (label = 1),  
25% are chosen from the most similar non-paraphrases (by fuzzywuzzy library Levenshtein distance) (label = 0),  
and 25% is random negative examples (label = 0).

To put it differently, the script processes the dataset, and for every sentence, it samples 2 positive examples (from
the same paraphrase set), one similar negative, and one random negative examples, and insert these to the output in this
order.