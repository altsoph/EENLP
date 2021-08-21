# EENLP

<p align="center">
    <img width="357" src="docs/images/EENLP-logo.png">
</p>

## About

This repo contains a collection of NLP (natural language processing) machine learning datasets and models for Eastern
European languages<sup>[1](#footnote-1)</sup>. We plan to add more and more task-specific evaluations and handcrafted
datasets as the project progresses.  
It originally started as a project at [EEML 2021](https://www.eeml.eu/previous-editions)
([Eastern European Machine Learning Summer School](https://www.eeml.eu)), (hence the scope), self-organized by a group
of participants.  
We hope that arranging and publishing these resources could be helpful for the NLP community.

## Resources

### [See datasets](docs/datasets.md)

## <a title='Albanian' href='docs/datasets.md#albania-albanian'>:albania:</a> <a title='Armenian' href='docs/datasets.md#armenia-armenian'>:armenia:</a> <a title='Belarusian' href='docs/datasets.md#belarus-belarusian'>:belarus:</a> <a title='Bosnian' href='docs/datasets.md#bosnia_herzegovina-bosnian'>:bosnia_herzegovina:</a> <a title='Bulgarian' href='docs/datasets.md#bulgaria-bulgarian'>:bulgaria:</a> <a title='Croatian' href='docs/datasets.md#croatia-croatian'>:croatia:</a> <a title='Czech' href='docs/datasets.md#czech_republic-czech'>:czech_republic:</a> <a title='Estonian' href='docs/datasets.md#estonia-estonian'>:estonia:</a> <a title='Georgian' href='docs/datasets.md#georgia-georgian'>:georgia:</a> <a title='Hungarian' href='docs/datasets.md#hungary-hungarian'>:hungary:</a> <a title='Kazakh' href='docs/datasets.md#kazakhstan-kazakh'>:kazakhstan:</a> <a title='Latvian' href='docs/datasets.md#latvia-latvian'>:latvia:</a> <a title='Lithuanian' href='docs/datasets.md#lithuania-lithuanian'>:lithuania:</a> <a title='Macedonian' href='docs/datasets.md#macedonia-macedonian'>:macedonia:</a> <a title='Moldovan' href='docs/datasets.md#moldova-moldovan'>:moldova:</a> <a title='Montenegrin' href='docs/datasets.md#montenegro-montenegrin'>:montenegro:</a> <a title='Polish' href='docs/datasets.md#poland-polish'>:poland:</a> <a title='Romanian' href='docs/datasets.md#romania-romanian'>:romania:</a> <a title='Russian' href='docs/datasets.md#ru-russian'>:ru:</a> <a title='Serbian' href='docs/datasets.md#serbia-serbian'>:serbia:</a> <a title='Slovakian' href='docs/datasets.md#slovakia-slovakian'>:slovakia:</a> <a title='Slovenian' href='docs/datasets.md#slovenia-slovenian'>:slovenia:</a> <a title='Ukrainian' href='docs/datasets.md#ukraine-ukrainian'>:ukraine:</a>

### [See models](docs/models.md)

## <a title='Albanian' href='docs/models.md#albania-albanian'>:albania:</a> <a title='Armenian' href='docs/models.md#armenia-armenian'>:armenia:</a> <a title='Belarusian' href='docs/models.md#belarus-belarusian'>:belarus:</a> <a title='Bosnian' href='docs/models.md#bosnia_herzegovina-bosnian'>:bosnia_herzegovina:</a> <a title='Bulgarian' href='docs/models.md#bulgaria-bulgarian'>:bulgaria:</a> <a title='Croatian' href='docs/models.md#croatia-croatian'>:croatia:</a> <a title='Czech' href='docs/models.md#czech_republic-czech'>:czech_republic:</a> <a title='Estonian' href='docs/models.md#estonia-estonian'>:estonia:</a> <a title='Georgian' href='docs/models.md#georgia-georgian'>:georgia:</a> <a title='Hungarian' href='docs/models.md#hungary-hungarian'>:hungary:</a> <a title='Kazakh' href='docs/models.md#kazakhstan-kazakh'>:kazakhstan:</a> <a title='Latvian' href='docs/models.md#latvia-latvian'>:latvia:</a> <a title='Lithuanian' href='docs/models.md#lithuania-lithuanian'>:lithuania:</a> <a title='Macedonian' href='docs/models.md#macedonia-macedonian'>:macedonia:</a> <a title='Moldovan' href='docs/models.md#moldova-moldovan'>:moldova:</a> <a title='Montenegrin' href='docs/models.md#montenegro-montenegrin'>:montenegro:</a> <a title='Polish' href='docs/models.md#poland-polish'>:poland:</a> <a title='Romanian' href='docs/models.md#romania-romanian'>:romania:</a> <a title='Russian' href='docs/models.md#ru-russian'>:ru:</a> <a title='Serbian' href='docs/models.md#serbia-serbian'>:serbia:</a> <a title='Slovakian' href='docs/models.md#slovakia-slovakian'>:slovakia:</a> <a title='Slovenian' href='docs/models.md#slovenia-slovenian'>:slovenia:</a> <a title='Ukrainian' href='docs/models.md#ukraine-ukrainian'>:ukraine:</a>

## Details

- <span id="footnote-1"></span>What counts as Eastern European language?
    - It's hard to exactly define. We took our initial list
      from [here](https://www.languagescientific.com/translation-and-localization-of-eastern-european-languages/).

- The collection seems to miss entire categories.
    - We were focusing on datasets and models especially suitable for the evaluation part of the project (e.g.
      cross-lingual transfer learning and sequence classification), but that doesn't mean this collection should be
      limited. Feel free to contribute.

## Contribution

Feel free to contribute. The details are in our [contributing guidelines](CONTRIBUTING.md).

## Citation

```
@misc{tikhonov2021eenlp,
      title={EENLP: Cross-lingual Eastern European NLP Index}, 
      author={Alexey Tikhonov and Alex Malkhasov and Andrey Manoshin and George Dima and Réka Cserháti and Md. Sadek Hossain Asif and Matt Sárdi},
      year={2021},
      eprint={2108.02605},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Development

This is mostly internal documentation for us.

See [developing this repository](docs/developer.md).
