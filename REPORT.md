<p align="center">
    <img width="357" src="docs/images/EENLP-logo.png">
</p>

Here are the results of the EENLP project, done as a part of EEML 2021 summer school. It presents a broad index of NLP resources for Eastern European languages, which, we hope, could be helpful for the NLP community; several new hand-crafted cross-lingual datasets focused on Eastern European languages, and a sketch evaluation of cross-lingual transfer learning abilities of several modern multilingual Transformer-based models.

# Brief description

## Motivation
As being in EEML, we decided to concentrate on Eastern European languages and build a comprehensive picture of the current NLP state across them.
We hope this broad index of NLP resources for Eastern European languages could help:
* to facilitate the synergy of Eastern European NLP research communities;
* to highlight the underrepresented languages of Eastern Europe;
* to understand cross-cultural and cross-linguistic differences;
* to decrease the digital divide.

## Resources enumeration
First, we focused on indexing existing Eastern European language resources – both datasets and models. We were able to collect 92 relevant datasets and at least 45 relevant Transformer-based models.

As the result of this stage, we made a comprehensive list of Eastern European NLP resources and published it in our github repository. We believe it would be a small but valuable step in building the generalized NLP field of Eastern Europe.
The results of this stage are presented in the [index of datasets page](https://github.com/altsoph/EENLP/blob/main/docs/datasets.md) and the [index of models page](https://github.com/altsoph/EENLP/blob/main/docs/models.md).

## Composing cross-lingual datasets
Next, we select four different semantic tasks, namely paraphrase detection, sentiment detection, word-in-context disambiguation, text categorization, and manually preprocessed the data from various sources into the same format, opening room for evaluation scenarios such as zero-shot cross-lingual transfer.
Partially, the results of this stage are presented [here](https://github.com/altsoph/EENLP/tree/main/data).

## Models evaluation
Finally, we performed several experiments with the several existing multilingual models on our datasets to define the performance baselines.
You can find the ipython notebooks we used [here](https://github.com/altsoph/EENLP/tree/main/notebooks).

## Results
Complete results of this project can be found in [our project report](https://arxiv.org/abs/2108.02605).
