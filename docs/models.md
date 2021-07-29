# Models x Languages Matrix

|                                              |       multilingual        |                           |                           |                                 |           several languages           |                                 |                                     |                                      |                                |                single language models                |                                                     |                                                     |                                                  |                                           |
| -------------------------------------------- | :-----------------------: | :-----------------------: | :-----------------------: | :-----------------------------: | :-----------------------------------: | :-----------------------------: | :---------------------------------: | :----------------------------------: | :----------------------------: | :--------------------------------------------------: | :-------------------------------------------------: | :-------------------------------------------------: | :----------------------------------------------: | :---------------------------------------: |
|                                              |           mBERT           |           XLM-R           |           LaBSE           |           mDistilBERT           |             CroSloEngual              |             BERTić              |             SlavicBERT              |             LitLat BERT              |             FinEst             |                         BERT                         |                       RoBERTa                       |                     DistilBERT                      |                     Electra                      |                  ALBERT                   |
| **[Albanian](#albanian)**                    |  [mBERT](#multilingual)   |  [XLM-R](#multilingual)   |  [LaBSE](#multilingual)   |  [mDistilBERT](#multilingual)   |                                       |                                 |                                     |                                      |                                |                                                      |        [AL-RoBERTa](#single-language-models)        |                                                     |                                                  |                                           |
| **[Armenian](#armenian)**                    | [mBERT](#multilingual-1)  | [XLM-R](#multilingual-1)  | [LaBSE](#multilingual-1)  | [mDistilBERT](#multilingual-1)  |                                       |                                 |                                     |                                      |                                |                                                      |                                                     |                                                     |                                                  |                                           |
| **[Belarusian](#belarusian)**                | [mBERT](#multilingual-2)  | [XLM-R](#multilingual-2)  | [LaBSE](#multilingual-2)  | [mDistilBERT](#multilingual-2)  |                                       |                                 |                                     |                                      |                                |                                                      |                                                     |                                                     |                                                  |                                           |
| **[Bosnian](#bosnian)**                      | [mBERT](#multilingual-3)  | [XLM-R](#multilingual-3)  | [LaBSE](#multilingual-3)  | [mDistilBERT](#multilingual-3)  |                                       | [BERTić](#several-languages-3)  |                                     |                                      |                                |                                                      |       [BA-RoBERTa](#single-language-models-3)       |                                                     |                                                  |                                           |
| **[Bulgarian](#bulgarian)**                  | [mBERT](#multilingual-4)  | [XLM-R](#multilingual-4)  | [LaBSE](#multilingual-4)  | [mDistilBERT](#multilingual-4)  |                                       |                                 | [SlavicBERT](#several-languages-4)  |                                      |                                |                                                      | [RoBERTa-base-bulgarian](#single-language-models-4) |                                                     |                                                  |                                           |
| **[Croatian](#croatian)**                    | [mBERT](#multilingual-5)  | [XLM-R](#multilingual-5)  | [LaBSE](#multilingual-5)  | [mDistilBERT](#multilingual-5)  | [CroSloEngual](#several-languages-5)  | [BERTić](#several-languages-5)  |                                     |                                      |                                |                                                      |                                                     |                                                     |                                                  |                                           |
| **[Czech](#czech)**                          | [mBERT](#multilingual-6)  | [XLM-R](#multilingual-6)  | [LaBSE](#multilingual-6)  | [mDistilBERT](#multilingual-6)  |                                       |                                 | [SlavicBERT](#several-languages-6)  |                                      |                                |          [CZERT](#single-language-models-6)          |       [RobeCzech](#single-language-models-6)        |                                                     |                                                  | [Czech ALBERT](#single-language-models-6) |
| **[Estonian](#estonian)**                    | [mBERT](#multilingual-7)  | [XLM-R](#multilingual-7)  | [LaBSE](#multilingual-7)  | [mDistilBERT](#multilingual-7)  |                                       |                                 |                                     |                                      | [FinEst](#several-languages-7) |         [EstBERT](#single-language-models-7)         |      [est-roberta](#single-language-models-7)       |                                                     |                                                  |                                           |
| **[Georgian](#georgian)**                    | [mBERT](#multilingual-8)  | [XLM-R](#multilingual-8)  | [LaBSE](#multilingual-8)  | [mDistilBERT](#multilingual-8)  |                                       |                                 |                                     |                                      |                                |                                                      |                                                     |                                                     |                                                  |                                           |
| **[Hungarian](#hungarian)**                  | [mBERT](#multilingual-9)  | [XLM-R](#multilingual-9)  | [LaBSE](#multilingual-9)  | [mDistilBERT](#multilingual-9)  |                                       |                                 |                                     |                                      |                                |         [huBERT](#single-language-models-9)          |                                                     |                                                     |                                                  |                                           |
| **[Kazakh](#kazakh)**                        | [mBERT](#multilingual-10) | [XLM-R](#multilingual-10) | [LaBSE](#multilingual-10) | [mDistilBERT](#multilingual-10) |                                       |                                 |                                     |                                      |                                |                                                      |                                                     |                                                     |                                                  |                                           |
| **[Latvian](#latvian)**                      | [mBERT](#multilingual-11) | [XLM-R](#multilingual-11) | [LaBSE](#multilingual-11) | [mDistilBERT](#multilingual-11) |                                       |                                 |                                     | [LitLat BERT](#several-languages-11) |                                |        [LV-BERT](#single-language-models-11)         |                                                     |                                                     |                                                  |                                           |
| **[Lithuanian](#lithuanian)**                | [mBERT](#multilingual-12) | [XLM-R](#multilingual-12) | [LaBSE](#multilingual-12) | [mDistilBERT](#multilingual-12) |                                       |                                 |                                     | [LitLat BERT](#several-languages-12) |                                |                                                      |                                                     |                                                     |                                                  |                                           |
| **[Macedonian](#macedonian)**                | [mBERT](#multilingual-13) | [XLM-R](#multilingual-13) | [LaBSE](#multilingual-13) | [mDistilBERT](#multilingual-13) |                                       |                                 |                                     |                                      |                                |    [Macedonian BERT](#single-language-models-13)     |      [MK-RoBERTa](#single-language-models-13)       | [Macedonian DistilBERT](#single-language-models-13) | [Macedonian Electra](#single-language-models-13) |                                           |
| **[Moldovan/Moldovian](#moldovanmoldovian)** | [mBERT](#multilingual-14) | [XLM-R](#multilingual-14) | [LaBSE](#multilingual-14) | [mDistilBERT](#multilingual-14) |                                       |                                 |                                     |                                      |                                |                                                      |                                                     |                                                     |                                                  |                                           |
| **[Montenegrin](#montenegrin)**              | [mBERT](#multilingual-15) | [XLM-R](#multilingual-15) | [LaBSE](#multilingual-15) | [mDistilBERT](#multilingual-15) |                                       | [BERTić](#several-languages-15) |                                     |                                      |                                |                                                      |                                                     |                                                     |                                                  |                                           |
| **[Polish](#polish)**                        | [mBERT](#multilingual-16) | [XLM-R](#multilingual-16) | [LaBSE](#multilingual-16) | [mDistilBERT](#multilingual-16) |                                       |                                 | [SlavicBERT](#several-languages-16) |                                      |                                |   [Polbert / HerBERT](#single-language-models-16)    |    [Polish RoBERTa](#single-language-models-16)     |                                                     |                                                  |                                           |
| **[Romanian](#romanian)**                    | [mBERT](#multilingual-17) | [XLM-R](#multilingual-17) | [LaBSE](#multilingual-17) | [mDistilBERT](#multilingual-17) |                                       |                                 |                                     |                                      |                                | [RoBERT / Romanian BERT](#single-language-models-17) |                                                     |  [Romanian DistilBERT](#single-language-models-17)  |                                                  |                                           |
| **[Russian](#russian)**                      | [mBERT](#multilingual-18) | [XLM-R](#multilingual-18) | [LaBSE](#multilingual-18) | [mDistilBERT](#multilingual-18) |                                       |                                 | [SlavicBERT](#several-languages-18) |                                      |                                |         [RuBERT](#single-language-models-18)         |    [Russian RoBERTa](#single-language-models-18)    |                                                     |                                                  |                                           |
| **[Serbian](#serbian)**                      | [mBERT](#multilingual-19) | [XLM-R](#multilingual-19) | [LaBSE](#multilingual-19) | [mDistilBERT](#multilingual-19) |                                       | [BERTić](#several-languages-19) |                                     |                                      |                                |                                                      |                                                     |                                                     |                                                  |                                           |
| **[Slovakian/Slovak](#slovakianslovak)**     | [mBERT](#multilingual-20) | [XLM-R](#multilingual-20) | [LaBSE](#multilingual-20) | [mDistilBERT](#multilingual-20) |                                       |                                 |                                     |                                      |                                |                                                      |                                                     |                                                     |                                                  |                                           |
| **[Slovenian](#slovenian)**                  | [mBERT](#multilingual-21) | [XLM-R](#multilingual-21) | [LaBSE](#multilingual-21) | [mDistilBERT](#multilingual-21) | [CroSloEngual](#several-languages-21) |                                 |                                     |                                      |                                |                                                      |       [SloBERTa](#single-language-models-21)        |                                                     |                                                  |                                           |
| **[Ukrainian](#ukrainian)**                  | [mBERT](#multilingual-22) | [XLM-R](#multilingual-22) | [LaBSE](#multilingual-22) | [mDistilBERT](#multilingual-22) |                                       |                                 |                                     |                                      |                                |                                                      |   [ukr-roberta-base](#single-language-models-22)    |                                                     | [Ukrainian Electra](#single-language-models-22)  |                                           |

## Albanian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name       | description | huggingface card                                   | type    | paper | citation | case  | pre-trained on | comments |
| ---------- | ----------- | -------------------------------------------------- | ------- | ----- | -------- | ----- | -------------- | -------- |
| AL-RoBERTa |             | https://huggingface.co/macedonizer/al-roberta-base | RoBERTa | ?     | ?        | cased |                |          |

### other

| name             | description | huggingface card                                 | type                   | paper                                                        | citation                                                    | case | pre-trained on | comments                               |
| ---------------- | ----------- | ------------------------------------------------ | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- | ---- | -------------- | -------------------------------------- |
| MultiFiT         |             | https://nlp.fast.ai/                             | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                             |      |                | multilingual ULMFiT                    |
| subs2vec         |             | https://github.com/jvparidon/subs2vec/           | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                             |      | subtitles      |                                        |
| fasttext aligned |             | https://fasttext.cc/docs/en/aligned-vectors.html | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references |      |                | original fasttext aligned automaticaly |
| fasttext         |             | https://fasttext.cc/docs/en/crawl-vectors.html   | static word embeddings |                                                              |                                                             |      | cc + wiki      | original fasttext                      |

## Armenian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name                                      | description | huggingface card                                           | type                   | paper                                                        | citation | case | pre-trained on | comments            |
| ----------------------------------------- | ----------- | ---------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | -------- | ---- | -------------- | ------------------- |
| MultiFiT                                  |             | https://nlp.fast.ai/                                       | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |          |      |                | multilingual ULMFiT |
| subs2vec                                  |             | https://github.com/jvparidon/subs2vec/                     | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |          |      | subtitles      |                     |
| fasttext                                  |             | https://fasttext.cc/docs/en/crawl-vectors.html             | static word embeddings |                                                              |          |      | cc + wiki      | original fasttext   |
| Word Embeddings for the Armenian Language |             | https://github.com/ispras-texterra/word-embeddings-eval-hy | static word embeddings |                                                              |          |      |                |                     |

## Belarusian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name     | description | huggingface card                               | type                   | paper                                 | citation | case | pre-trained on | comments            |
| -------- | ----------- | ---------------------------------------------- | ---------------------- | ------------------------------------- | -------- | ---- | -------------- | ------------------- |
| MultiFiT |             | https://nlp.fast.ai/                           | ULMFiT                 | https://aclanthology.org/D19-1572.pdf |          |      |                | multilingual ULMFiT |
| fasttext |             | https://fasttext.cc/docs/en/crawl-vectors.html | static word embeddings |                                       |          |      | cc + wiki      | original fasttext   |

## Bosnian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name   | description | huggingface card                           | type            | paper                            | citation                                   | case  | pre-trained on    | comments |
| ------ | ----------- | ------------------------------------------ | --------------- | -------------------------------- | ------------------------------------------ | ----- | ----------------- | -------- |
| BERTić |             | https://huggingface.co/classla/bcms-bertic | BERT/Electra(?) | https://arxiv.org/abs/2104.09243 | https://huggingface.co/classla/bcms-bertic | cased | web crawled texts |          |

### single language models

| name       | description | huggingface card                                   | type    | paper | citation | case  | pre-trained on | comments |
| ---------- | ----------- | -------------------------------------------------- | ------- | ----- | -------- | ----- | -------------- | -------- |
| BA-RoBERTa |             | https://huggingface.co/macedonizer/ba-roberta-base | RoBERTa | ?     | ?        | cased |                |          |

### other

| name             | description | huggingface card                                 | type                   | paper                                                        | citation                                                    | case | pre-trained on | comments                               |
| ---------------- | ----------- | ------------------------------------------------ | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- | ---- | -------------- | -------------------------------------- |
| MultiFiT         |             | https://nlp.fast.ai/                             | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                             |      |                | multilingual ULMFiT                    |
| subs2vec         |             | https://github.com/jvparidon/subs2vec/           | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                             |      | subtitles      |                                        |
| fasttext aligned |             | https://fasttext.cc/docs/en/aligned-vectors.html | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references |      |                | original fasttext aligned automaticaly |
| fasttext         |             | https://fasttext.cc/docs/en/crawl-vectors.html   | static word embeddings |                                                              |                                                             |      | cc + wiki      | original fasttext                      |

## Bulgarian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name       | description | huggingface card                                              | type | paper                              | citation                           | case  | pre-trained on | comments |
| ---------- | ----------- | ------------------------------------------------------------- | ---- | ---------------------------------- | ---------------------------------- | ----- | -------------- | -------- |
| SlavicBERT |             | https://huggingface.co/DeepPavlov/bert-base-bg-cs-pl-ru-cased | BERT | https://aclanthology.org/W19-3712/ | https://aclanthology.org/W19-3712/ | cased | news + wiki    |          |

### single language models

| name                   | description | huggingface card                                        | type    | paper | citation | case | pre-trained on      | comments                                                                 |
| ---------------------- | ----------- | ------------------------------------------------------- | ------- | ----- | -------- | ---- | ------------------- | ------------------------------------------------------------------------ |
| RoBERTa-base-bulgarian |             | https://huggingface.co/iarfmoose/roberta-base-bulgarian | RoBERTa | ?     | ?        | ?    | news + wiki + oscar | smaller version https://huggingface.co/iarfmoose/roberta-small-bulgarian |

### other

| name                                    | description | huggingface card                                                               | type                   | paper                                                        | citation                                                                        | case  | pre-trained on               | comments                               |
| --------------------------------------- | ----------- | ------------------------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ----- | ---------------------------- | -------------------------------------- |
| bert-base-bg-cased                      |             | https://huggingface.co/Geotrend/bert-base-bg-cased                             | DistilBERT             | https://aclanthology.org/2020.sustainlp-1.16.pdf             | https://aclanthology.org/2020.sustainlp-1.16.pdf                                | cased | mBERT distilled to Bulgarian |                                        |
| Macedonian + Bulgarian BERT             |             | https://huggingface.co/anon-submission-mk/bert-base-macedonian-bulgarian-cased | BERT                   |                                                              |                                                                                 |       |                              |                                        |
| MultiFiT                                |             | https://nlp.fast.ai/                                                           | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |       |                              | multilingual ULMFiT                    |
| subs2vec                                |             | https://github.com/jvparidon/subs2vec/                                         | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |       | subtitles                    |                                        |
| fasttext aligned                        |             | https://fasttext.cc/docs/en/aligned-vectors.html                               | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |       |                              | original fasttext aligned automaticaly |
| fasttext aligned supervised             |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings          | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |       | wiki                         | original fasttext aligned supervised   |
| fasttext                                |             | https://fasttext.cc/docs/en/crawl-vectors.html                                 | static word embeddings |                                                              |                                                                                 |       | cc + wiki                    | original fasttext                      |
| ELMo Representations for Many Languages |             | https://github.com/HIT-SCIR/ELMoForManyLangs                                   | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation                           |       |                              |                                        |

## Croatian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name         | description | huggingface card                                  | type            | paper                            | citation                                   | case      | pre-trained on    | comments                         |
| ------------ | ----------- | ------------------------------------------------- | --------------- | -------------------------------- | ------------------------------------------ | --------- | ----------------- | -------------------------------- |
| CroSloEngual |             | https://huggingface.co/EMBEDDIA/crosloengual-bert | BERT            | https://arxiv.org/abs/2006.07890 | https://arxiv.org/abs/2006.07890           | cased (?) | ?                 | project site http://embeddia.eu/ |
| BERTić       |             | https://huggingface.co/classla/bcms-bertic        | BERT/Electra(?) | https://arxiv.org/abs/2104.09243 | https://huggingface.co/classla/bcms-bertic | cased     | web crawled texts |                                  |

### single language models

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name                                       | description | huggingface card                                                      | type                   | paper                                                        | citation                                                                        | case | pre-trained on     | comments                                                              |
| ------------------------------------------ | ----------- | --------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ---- | ------------------ | --------------------------------------------------------------------- |
| ELMo embeddings models for seven languages |             | --                                                                    | ELMo                   | https://arxiv.org/abs/1911.10049                             | https://arxiv.org/abs/1911.10049                                                | ?    | some local corpora | more details https://www.clarin.si/repository/xmlui/handle/11356/1277 |
| MultiFiT                                   |             | https://nlp.fast.ai/                                                  | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |      |                    | multilingual ULMFiT                                                   |
| subs2vec                                   |             | https://github.com/jvparidon/subs2vec/                                | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |      | subtitles          |                                                                       |
| fasttext aligned                           |             | https://fasttext.cc/docs/en/aligned-vectors.html                      | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |      |                    | original fasttext aligned automaticaly                                |
| fasttext aligned supervised                |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |      | wiki               | original fasttext aligned supervised                                  |
| fasttext                                   |             | https://fasttext.cc/docs/en/crawl-vectors.html                        | static word embeddings |                                                              |                                                                                 |      | cc + wiki          | original fasttext                                                     |
| ELMo Representations for Many Languages    |             | https://github.com/HIT-SCIR/ELMoForManyLangs                          | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation                           |      |                    |                                                                       |

## Czech

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name       | description | huggingface card                                              | type | paper                              | citation                           | case  | pre-trained on | comments |
| ---------- | ----------- | ------------------------------------------------------------- | ---- | ---------------------------------- | ---------------------------------- | ----- | -------------- | -------- |
| SlavicBERT |             | https://huggingface.co/DeepPavlov/bert-base-bg-cs-pl-ru-cased | BERT | https://aclanthology.org/W19-3712/ | https://aclanthology.org/W19-3712/ | cased | news + wiki    |          |

### single language models

| name         | description | huggingface card                           | type    | paper                                | citation                                                 | case  | pre-trained on | comments                                   |
| ------------ | ----------- | ------------------------------------------ | ------- | ------------------------------------ | -------------------------------------------------------- | ----- | -------------- | ------------------------------------------ |
| CZERT        |             | --                                         | BERT    | https://arxiv.org/abs/2103.13031     | https://github.com/kiv-air/Czert#how-should-i-cite-czert |       | ?              | github: https://github.com/kiv-air/Czert   |
| RobeCzech    |             | https://huggingface.co/ufal/robeczech-base | RoBERTa | https://arxiv.org/abs/2105.11314     | https://arxiv.org/abs/2105.11314                         | cased | ?              |                                            |
| Czech ALBERT |             | --                                         | ALBERT  | https://is.muni.cz/th/t946b/?lang=en | ?                                                        | ?     | ?              | github: https://github.com/zepzep/csalbert |

### other

| name                                    | description | huggingface card                                 | type                   | paper                                                        | citation                                                    | case | pre-trained on     | comments                               |
| --------------------------------------- | ----------- | ------------------------------------------------ | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- | ---- | ------------------ | -------------------------------------- |
| MultiFiT                                |             | https://nlp.fast.ai/                             | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                             |      |                    | multilingual ULMFiT                    |
| subs2vec                                |             | https://github.com/jvparidon/subs2vec/           | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                             |      | subtitles          |                                        |
| fasttext aligned                        |             | https://fasttext.cc/docs/en/aligned-vectors.html | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references |      |                    | original fasttext aligned automaticaly |
| ULMFiT for Czech                        |             | https://github.com/simecek/Czech-ULMFiT          | ULMFiT                 |                                                              |                                                             |      | CSFD movie dataset |                                        |
| fasttext                                |             | https://fasttext.cc/docs/en/crawl-vectors.html   | static word embeddings |                                                              |                                                             |      | cc + wiki          | original fasttext                      |
| ELMo Representations for Many Languages |             | https://github.com/HIT-SCIR/ELMoForManyLangs     | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation       |      |                    |                                        |

## Estonian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name   | description | huggingface card                            | type | paper                            | citation                         | case      | pre-trained on | comments                         |
| ------ | ----------- | ------------------------------------------- | ---- | -------------------------------- | -------------------------------- | --------- | -------------- | -------------------------------- |
| FinEst |             | https://huggingface.co/EMBEDDIA/finest-bert | BERT | https://arxiv.org/abs/2006.07890 | https://arxiv.org/abs/2006.07890 | cased (?) | ?              | project site http://embeddia.eu/ |

### single language models

| name        | description | huggingface card                            | type    | paper                            | citation                         | case  | pre-trained on                | comments |
| ----------- | ----------- | ------------------------------------------- | ------- | -------------------------------- | -------------------------------- | ----- | ----------------------------- | -------- |
| EstBERT     |             | https://huggingface.co/tartuNLP/EstBERT     | BERT    | https://arxiv.org/abs/2011.04784 | https://arxiv.org/abs/2011.04784 | cased | Estonian National Corpus 2017 |          |
| est-roberta |             | https://huggingface.co/EMBEDDIA/est-roberta | RoBERTa | ?                                | ?                                | cased | ?                             |          |

### other

| name                                                    | description | huggingface card                                                      | type                   | paper                                                        | citation                                                                        | case | pre-trained on     | comments                                                              |
| ------------------------------------------------------- | ----------- | --------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ---- | ------------------ | --------------------------------------------------------------------- |
| ELMo embeddings models for seven languages              |             | --                                                                    | ELMo                   | https://arxiv.org/abs/1911.10049                             | https://arxiv.org/abs/1911.10049                                                | ?    | some local corpora | more details https://www.clarin.si/repository/xmlui/handle/11356/1277 |
| MultiFiT                                                |             | https://nlp.fast.ai/                                                  | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |      |                    | multilingual ULMFiT                                                   |
| subs2vec                                                |             | https://github.com/jvparidon/subs2vec/                                | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |      | subtitles          |                                                                       |
| fasttext aligned                                        |             | https://fasttext.cc/docs/en/aligned-vectors.html                      | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |      |                    | original fasttext aligned automaticaly                                |
| fasttext aligned supervised                             |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |      | wiki               | original fasttext aligned supervised                                  |
| fasttext                                                |             | https://fasttext.cc/docs/en/crawl-vectors.html                        | static word embeddings |                                                              |                                                                                 |      | cc + wiki          | original fasttext                                                     |
| ELMo Representations for Many Languages                 |             | https://github.com/HIT-SCIR/ELMoForManyLangs                          | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation                           |      |                    |                                                                       |
| Pretrained word and multi-sense embeddings for Estonian |             | https://github.com/eleriaedmaa/embeddings                             | static word embeddings |                                                              |                                                                                 |      |                    |                                                                       |

## Georgian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name     | description | huggingface card                               | type                   | paper                                                        | citation | case | pre-trained on | comments            |
| -------- | ----------- | ---------------------------------------------- | ---------------------- | ------------------------------------------------------------ | -------- | ---- | -------------- | ------------------- |
| MultiFiT |             | https://nlp.fast.ai/                           | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |          |      |                | multilingual ULMFiT |
| subs2vec |             | https://github.com/jvparidon/subs2vec/         | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |          |      | subtitles      |                     |
| fasttext |             | https://fasttext.cc/docs/en/crawl-vectors.html | static word embeddings |                                                              |          |      | cc + wiki      | original fasttext   |

## Hungarian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name   | description | huggingface card                                 | type | paper                                   | citation                                                                        | case  | pre-trained on      | comments |
| ------ | ----------- | ------------------------------------------------ | ---- | --------------------------------------- | ------------------------------------------------------------------------------- | ----- | ------------------- | -------- |
| huBERT |             | https://huggingface.co/SZTAKI-HLT/hubert-base-cc | BERT | https://hlt.bme.hu/media/pdf/huBERT.pdf | https://huggingface.co/SZTAKI-HLT/hubert-base-cc#bibtex-entry-and-citation-info | cased | common crawl + wiki |          |

### other

| name                                    | description | huggingface card                                                      | type                   | paper                                                        | citation                                                                        | case | pre-trained on | comments                               |
| --------------------------------------- | ----------- | --------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ---- | -------------- | -------------------------------------- |
| MultiFiT                                |             | https://nlp.fast.ai/                                                  | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |      |                | multilingual ULMFiT                    |
| subs2vec                                |             | https://github.com/jvparidon/subs2vec/                                | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |      | subtitles      |                                        |
| fasttext aligned                        |             | https://fasttext.cc/docs/en/aligned-vectors.html                      | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |      |                | original fasttext aligned automaticaly |
| fasttext aligned supervised             |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |      | wiki           | original fasttext aligned supervised   |
| fasttext                                |             | https://fasttext.cc/docs/en/crawl-vectors.html                        | static word embeddings |                                                              |                                                                                 |      | cc + wiki      | original fasttext                      |
| ELMo Representations for Many Languages |             | https://github.com/HIT-SCIR/ELMoForManyLangs                          | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation                           |      |                |                                        |

## Kazakh

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name     | description | huggingface card                               | type                   | paper                                 | citation | case | pre-trained on | comments            |
| -------- | ----------- | ---------------------------------------------- | ---------------------- | ------------------------------------- | -------- | ---- | -------------- | ------------------- |
| MultiFiT |             | https://nlp.fast.ai/                           | ULMFiT                 | https://aclanthology.org/D19-1572.pdf |          |      |                | multilingual ULMFiT |
| fasttext |             | https://fasttext.cc/docs/en/crawl-vectors.html | static word embeddings |                                       |          |      | cc + wiki      | original fasttext   |

## Latvian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name        | description | huggingface card                            | type        | paper | citation | case  | pre-trained on | comments |
| ----------- | ----------- | ------------------------------------------- | ----------- | ----- | -------- | ----- | -------------- | -------- |
| LitLat BERT |             | https://huggingface.co/EMBEDDIA/litlat-bert | XLM-RoBERTa | ?     | ?        | cased | ?              |          |

### single language models

| name   | description | huggingface card | type | paper                                                                          | citation                                       | case | pre-trained on | comments                              |
| ------ | ----------- | ---------------- | ---- | ------------------------------------------------------------------------------ | ---------------------------------------------- | ---- | -------------- | ------------------------------------- |
| LVBERT |             | ?                | BERT | https://pdfs.semanticscholar.org/d5f0/cf6f006f954316ce43aa945d6786808e8715.pdf | https://ebooks.iospress.nl/volumearticle/55531 | ?    | wiki + LVK2018 | https://github.com/LUMII-AILab/LVBERT |

### other

| name                                       | description | huggingface card                                 | type                   | paper                                                        | citation                                                    | case | pre-trained on     | comments                                                              |
| ------------------------------------------ | ----------- | ------------------------------------------------ | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- | ---- | ------------------ | --------------------------------------------------------------------- |
| ELMo embeddings models for seven languages |             | --                                               | ELMo                   | https://arxiv.org/abs/1911.10049                             | https://arxiv.org/abs/1911.10049                            | ?    | some local corpora | more details https://www.clarin.si/repository/xmlui/handle/11356/1277 |
| MultiFiT                                   |             | https://nlp.fast.ai/                             | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                             |      |                    | multilingual ULMFiT                                                   |
| subs2vec                                   |             | https://github.com/jvparidon/subs2vec/           | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                             |      | subtitles          |                                                                       |
| fasttext aligned                           |             | https://fasttext.cc/docs/en/aligned-vectors.html | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references |      |                    | original fasttext aligned automaticaly                                |
| fasttext                                   |             | https://fasttext.cc/docs/en/crawl-vectors.html   | static word embeddings |                                                              |                                                             |      | cc + wiki          | original fasttext                                                     |
| ELMo Representations for Many Languages    |             | https://github.com/HIT-SCIR/ELMoForManyLangs     | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation       |      |                    |                                                                       |

## Lithuanian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name        | description | huggingface card                            | type        | paper | citation | case  | pre-trained on | comments |
| ----------- | ----------- | ------------------------------------------- | ----------- | ----- | -------- | ----- | -------------- | -------- |
| LitLat BERT |             | https://huggingface.co/EMBEDDIA/litlat-bert | XLM-RoBERTa | ?     | ?        | cased | ?              |          |

### single language models

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name                                       | description | huggingface card                                                               | type                   | paper                                                        | citation                                                    | case | pre-trained on         | comments                                                                                                                                  |
| ------------------------------------------ | ----------- | ------------------------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- | ---- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| ELMo embeddings models for seven languages |             | --                                                                             | ELMo                   | https://arxiv.org/abs/1911.10049                             | https://arxiv.org/abs/1911.10049                            | ?    | some local corpora     | more details https://www.clarin.si/repository/xmlui/handle/11356/1277                                                                     |
| Lithuanian T5 summaries                    |             | https://huggingface.co/LukasStankevicius/t5-base-lithuanian-news-summaries-175 | T5 summaries           |                                                              |                                                             |      |                        | https://www.researchgate.net/publication/351448762_Generating_abstractive_summaries_of_Lithuanian_news_articles_using_a_transformer_model |
| MultiFiT                                   |             | https://nlp.fast.ai/                                                           | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                             |      |                        | multilingual ULMFiT                                                                                                                       |
| subs2vec                                   |             | https://github.com/jvparidon/subs2vec/                                         | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                             |      | subtitles              |                                                                                                                                           |
| Lithuanian Word embeddings                 |             | https://clarin.vdu.lt/xmlui/handle/20.500.11821/26                             | static word embeddings |                                                              |                                                             |      | Delfi.lt + StanfordNLP | GloVe                                                                                                                                     |
| fasttext aligned                           |             | https://fasttext.cc/docs/en/aligned-vectors.html                               | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references |      |                        | original fasttext aligned automaticaly                                                                                                    |
| fasttext                                   |             | https://fasttext.cc/docs/en/crawl-vectors.html                                 | static word embeddings |                                                              |                                                             |      | cc + wiki              | original fasttext                                                                                                                         |

## Macedonian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name                  | description | huggingface card                                                                  | type       | paper | citation | case  | pre-trained on | comments |
| --------------------- | ----------- | --------------------------------------------------------------------------------- | ---------- | ----- | -------- | ----- | -------------- | -------- |
| Macedonian BERT       |             | https://huggingface.co/anon-submission-mk/bert-base-macedonian-cased              | BERT       |       |          |       |                |          |
| MK-RoBERTa            |             | https://huggingface.co/macedonizer/mk-roberta-base                                | RoBERTa    | ?     | ?        | cased |                |          |
| Macedonian DistilBERT |             | https://huggingface.co/anon-submission-mk/distilbert-base-macedonian-cased        | DistilBERT |       |          |       |                |          |
| Macedonian Electra    |             | https://huggingface.co/anon-submission-mk/electra-base-macedonian-cased-generator | Electra    |       |          |       |                |          |

### other

| name                        | description | huggingface card                                                               | type                   | paper                                                        | citation                                                                        | case  | pre-trained on | comments                               |
| --------------------------- | ----------- | ------------------------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ----- | -------------- | -------------------------------------- |
| Macedonian + Bulgarian BERT |             | https://huggingface.co/anon-submission-mk/bert-base-macedonian-bulgarian-cased | BERT                   |                                                              |                                                                                 |       |                |                                        |
| mk-gpt2                     |             | https://huggingface.co/macedonizer/mk-gpt2                                     | GPT2                   | ?                                                            | ?                                                                               | cased |                |                                        |
| MultiFiT                    |             | https://nlp.fast.ai/                                                           | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |       |                | multilingual ULMFiT                    |
| subs2vec                    |             | https://github.com/jvparidon/subs2vec/                                         | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |       | subtitles      |                                        |
| fasttext aligned            |             | https://fasttext.cc/docs/en/aligned-vectors.html                               | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |       |                | original fasttext aligned automaticaly |
| fasttext aligned supervised |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings          | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |       | wiki           | original fasttext aligned supervised   |
| fasttext                    |             | https://fasttext.cc/docs/en/crawl-vectors.html                                 | static word embeddings |                                                              |                                                                                 |       | cc + wiki      | original fasttext                      |

## Moldovan/Moldovian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name     | description | huggingface card                               | type                   | paper                                 | citation | case | pre-trained on | comments            |
| -------- | ----------- | ---------------------------------------------- | ---------------------- | ------------------------------------- | -------- | ---- | -------------- | ------------------- |
| MultiFiT |             | https://nlp.fast.ai/                           | ULMFiT                 | https://aclanthology.org/D19-1572.pdf |          |      |                | multilingual ULMFiT |
| fasttext |             | https://fasttext.cc/docs/en/crawl-vectors.html | static word embeddings |                                       |          |      | cc + wiki      | original fasttext   |

## Montenegrin

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name   | description | huggingface card                           | type            | paper                            | citation                                   | case  | pre-trained on    | comments |
| ------ | ----------- | ------------------------------------------ | --------------- | -------------------------------- | ------------------------------------------ | ----- | ----------------- | -------- |
| BERTić |             | https://huggingface.co/classla/bcms-bertic | BERT/Electra(?) | https://arxiv.org/abs/2104.09243 | https://huggingface.co/classla/bcms-bertic | cased | web crawled texts |          |

### single language models

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name     | description | huggingface card                               | type                   | paper                                 | citation | case | pre-trained on | comments            |
| -------- | ----------- | ---------------------------------------------- | ---------------------- | ------------------------------------- | -------- | ---- | -------------- | ------------------- |
| MultiFiT |             | https://nlp.fast.ai/                           | ULMFiT                 | https://aclanthology.org/D19-1572.pdf |          |      |                | multilingual ULMFiT |
| fasttext |             | https://fasttext.cc/docs/en/crawl-vectors.html | static word embeddings |                                       |          |      | cc + wiki      | original fasttext   |

## Polish

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name       | description | huggingface card                                              | type | paper                              | citation                           | case  | pre-trained on | comments |
| ---------- | ----------- | ------------------------------------------------------------- | ---- | ---------------------------------- | ---------------------------------- | ----- | -------------- | -------- |
| SlavicBERT |             | https://huggingface.co/DeepPavlov/bert-base-bg-cs-pl-ru-cased | BERT | https://aclanthology.org/W19-3712/ | https://aclanthology.org/W19-3712/ | cased | news + wiki    |          |

### single language models

| name           | description | huggingface card                                          | type    | paper                                    | citation                                                | case  | pre-trained on  | comments                                                                       |
| -------------- | ----------- | --------------------------------------------------------- | ------- | ---------------------------------------- | ------------------------------------------------------- | ----- | --------------- | ------------------------------------------------------------------------------ |
| Polbert        |             | https://huggingface.co/dkleczek/bert-base-polish-cased-v1 | BERT    | ?                                        | ?                                                       | both  | cc + wiki + etc | usage examples https://huggingface.co/dkleczek/bert-base-polish-cased-v1#usage |
| HerBERT        |             | https://huggingface.co/allegro/herbert-base-cased         | BERT    | https://aclanthology.org/2021.bsnlp-1.1/ | https://aclanthology.org/2021.bsnlp-1.1/                | cased | ?               |                                                                                |
| Polish RoBERTa |             | --                                                        | RoBERTa | https://arxiv.org/abs/2006.04229         | https://github.com/sdadas/polish-roberta#polish-roberta | cased | ?               | github https://github.com/sdadas/polish-roberta                                |

### other

| name                                    | description | huggingface card                                                                    | type                   | paper                                                        | citation                                                                        | case | pre-trained on | comments                               |
| --------------------------------------- | ----------- | ----------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ---- | -------------- | -------------------------------------- |
| papuGaPT2                               |             | https://huggingface.co/flax-community/papuGaPT2?text=Najsmaczniejszy+polski+owoc+to | GPT2                   |                                                              |                                                                                 |      |                |                                        |
| MultiFiT                                |             | https://nlp.fast.ai/                                                                | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |      |                | multilingual ULMFiT                    |
| subs2vec                                |             | https://github.com/jvparidon/subs2vec/                                              | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |      | subtitles      |                                        |
| wikipedia2vec                           |             | https://wikipedia2vec.github.io/wikipedia2vec/pretrained/                           | static word embeddings |                                                              |                                                                                 |      | wiki           |                                        |
| fasttext aligned                        |             | https://fasttext.cc/docs/en/aligned-vectors.html                                    | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |      |                | original fasttext aligned automaticaly |
| ELMo Embeddings for Polish              |             | https://clarin-pl.eu/dspace/handle/11321/690                                        | ELMo                   |                                                              |                                                                                 |      | KGR10          |                                        |
| fasttext aligned supervised             |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings               | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |      | wiki           | original fasttext aligned supervised   |
| fasttext                                |             | https://fasttext.cc/docs/en/crawl-vectors.html                                      | static word embeddings |                                                              |                                                                                 |      | cc + wiki      | original fasttext                      |
| ELMo Representations for Many Languages |             | https://github.com/HIT-SCIR/ELMoForManyLangs                                        | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation                           |      |                |                                        |
| Word Embeddings for Polish              |             | https://clarin-pl.eu/dspace/handle/11321/442                                        | static word embeddings |                                                              |                                                                                 |      |                |                                        |
| Polish Word embeddings                  |             | https://github.com/sdadas/polish-nlp-resources#word-embeddings-and-language-models  | static word embeddings |                                                              |                                                                                 |      |                |                                        |
| Polish ELMo                             |             | https://github.com/sdadas/polish-nlp-resources#elmo                                 | ELMo                   |                                                              |                                                                                 |      |                |                                        |

## Romanian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name                | description | huggingface card                                                    | type       | paper                                          | citation                                                                      | case  | pre-trained on | comments                                                         |
| ------------------- | ----------- | ------------------------------------------------------------------- | ---------- | ---------------------------------------------- | ----------------------------------------------------------------------------- | ----- | -------------- | ---------------------------------------------------------------- |
| RoBERT              |             | https://huggingface.co/readerbench/RoBERT-base                      | BERT       | https://aclanthology.org/2020.coling-main.581/ | https://huggingface.co/readerbench/RoBERT-base#bibtex-entry-and-citation-info |       |                |                                                                  |
| Romanian BERT       |             | https://huggingface.co/dumitrescustefan/bert-base-romanian-cased-v1 | BERT       | https://arxiv.org/abs/2009.08712               | https://github.com/dumitrescustefan/Romanian-Transformers#cite                | both  | ?              | github https://github.com/dumitrescustefan/Romanian-Transformers |
| Romanian DistilBERT |             | https://huggingface.co/racai/distilbert-base-romanian-cased         | DistilBERT | ?                                              | https://github.com/racai-ai/Romanian-DistilBERT#citation                      | cased | ?              | github https://github.com/racai-ai/Romanian-DistilBERT           |

### other

| name                                    | description | huggingface card                                                      | type                   | paper                                                        | citation                                                                        | case | pre-trained on | comments                               |
| --------------------------------------- | ----------- | --------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ---- | -------------- | -------------------------------------- |
| Romanian GPT2                           |             | https://huggingface.co/mihaitensor/romanian-gpt2                      | GPT2                   |                                                              |                                                                                 |      |                |                                        |
| MultiFiT                                |             | https://nlp.fast.ai/                                                  | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |      |                | multilingual ULMFiT                    |
| subs2vec                                |             | https://github.com/jvparidon/subs2vec/                                | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |      | subtitles      |                                        |
| fasttext aligned                        |             | https://fasttext.cc/docs/en/aligned-vectors.html                      | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |      |                | original fasttext aligned automaticaly |
| fasttext aligned supervised             |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |      | wiki           | original fasttext aligned supervised   |
| fasttext                                |             | https://fasttext.cc/docs/en/crawl-vectors.html                        | static word embeddings |                                                              |                                                                                 |      | cc + wiki      | original fasttext                      |
| ELMo Representations for Many Languages |             | https://github.com/HIT-SCIR/ELMoForManyLangs                          | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation                           |      |                |                                        |
| Romanian static embeddings              |             | https://github.com/senisioi/ro_resources                              | static word embeddings |                                                              |                                                                                 |      |                |                                        |

## Russian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name       | description | huggingface card                                              | type | paper                              | citation                           | case  | pre-trained on | comments |
| ---------- | ----------- | ------------------------------------------------------------- | ---- | ---------------------------------- | ---------------------------------- | ----- | -------------- | -------- |
| SlavicBERT |             | https://huggingface.co/DeepPavlov/bert-base-bg-cs-pl-ru-cased | BERT | https://aclanthology.org/W19-3712/ | https://aclanthology.org/W19-3712/ | cased | news + wiki    |          |

### single language models

| name            | description | huggingface card                                       | type    | paper                            | citation                         | case  | pre-trained on | comments                                                           |
| --------------- | ----------- | ------------------------------------------------------ | ------- | -------------------------------- | -------------------------------- | ----- | -------------- | ------------------------------------------------------------------ |
| RuBERT          |             | https://huggingface.co/DeepPavlov/rubert-base-cased    | BERT    | https://arxiv.org/abs/1905.07213 | https://arxiv.org/abs/1905.07213 | cased | ?              | also: https://huggingface.co/DeepPavlov/rubert-base-cased-sentence |
| Russian RoBERTa |             | https://huggingface.co/blinoff/roberta-base-russian-v0 | RoBERTa |                                  |                                  |       |                |                                                                    |

### other

| name                                    | description | huggingface card                                                              | type                   | paper                                                        | citation                                                                        | case | pre-trained on | comments                                    |
| --------------------------------------- | ----------- | ----------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ---- | -------------- | ------------------------------------------- |
| ru-gpts                                 |             |                                                                               | GPT2                   |                                                              |                                                                                 |      |                | https://github.com/sberbank-ai/ru-gpts      |
| ru_transformers                         |             |                                                                               | GPT2                   |                                                              |                                                                                 |      |                | https://github.com/mgrankin/ru_transformers |
| MultiFiT                                |             | https://nlp.fast.ai/                                                          | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |      |                | multilingual ULMFiT                         |
| subs2vec                                |             | https://github.com/jvparidon/subs2vec/                                        | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |      | subtitles      |                                             |
| wikipedia2vec                           |             | https://wikipedia2vec.github.io/wikipedia2vec/pretrained/                     | static word embeddings |                                                              |                                                                                 |      | wiki           |                                             |
| fasttext aligned                        |             | https://fasttext.cc/docs/en/aligned-vectors.html                              | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |      |                | original fasttext aligned automaticaly      |
| fasttext aligned supervised             |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings         | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |      | wiki           | original fasttext aligned supervised        |
| fasttext                                |             | https://fasttext.cc/docs/en/crawl-vectors.html                                | static word embeddings |                                                              |                                                                                 |      | cc + wiki      | original fasttext                           |
| ELMo Representations for Many Languages |             | https://github.com/HIT-SCIR/ELMoForManyLangs                                  | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation                           |      |                |                                             |
| Russian language ELMo embeddings model  |             | http://docs.deeppavlov.ai/en/master/features/pretrained_vectors.html#elmo     | ELMo                   |                                                              |                                                                                 |      |                |                                             |
| Russian fasttext from DeepPavlov        |             | http://docs.deeppavlov.ai/en/master/features/pretrained_vectors.html#fasttext | static word embeddings |                                                              |                                                                                 |      |                |                                             |
| Russian fasttext from natasha project   |             | https://github.com/natasha/navec                                              | static word embeddings |                                                              |                                                                                 |      |                |                                             |
| RuVectores static                       |             | https://rusvectores.org/en/models/                                            | static word embeddings |                                                              |                                                                                 |      |                |                                             |
| RuVectores ELMo                         |             | https://rusvectores.org/en/models/                                            | ELMo                   |                                                              |                                                                                 |      |                |                                             |

## Serbian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name   | description | huggingface card                           | type            | paper                            | citation                                   | case  | pre-trained on    | comments |
| ------ | ----------- | ------------------------------------------ | --------------- | -------------------------------- | ------------------------------------------ | ----- | ----------------- | -------- |
| BERTić |             | https://huggingface.co/classla/bcms-bertic | BERT/Electra(?) | https://arxiv.org/abs/2104.09243 | https://huggingface.co/classla/bcms-bertic | cased | web crawled texts |          |

### single language models

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name             | description | huggingface card                               | type                   | paper                                                        | citation | case | pre-trained on | comments            |
| ---------------- | ----------- | ---------------------------------------------- | ---------------------- | ------------------------------------------------------------ | -------- | ---- | -------------- | ------------------- |
| MultiFiT         |             | https://nlp.fast.ai/                           | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |          |      |                | multilingual ULMFiT |
| subs2vec         |             | https://github.com/jvparidon/subs2vec/         | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |          |      | subtitles      |                     |
| ULMFIT - Serbian |             | https://forums.fast.ai/t/ulmfit-serbian/40316  | ULMFiT                 |                                                              |          |      | wiki           | unfinished?         |
| fasttext         |             | https://fasttext.cc/docs/en/crawl-vectors.html | static word embeddings |                                                              |          |      | cc + wiki      | original fasttext   |

## Slovakian/Slovak

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name                                    | description | huggingface card                                                      | type                   | paper                                                        | citation                                                                        | case | pre-trained on | comments                               |
| --------------------------------------- | ----------- | --------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ---- | -------------- | -------------------------------------- |
| MultiFiT                                |             | https://nlp.fast.ai/                                                  | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |      |                | multilingual ULMFiT                    |
| subs2vec                                |             | https://github.com/jvparidon/subs2vec/                                | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |      | subtitles      |                                        |
| fasttext aligned                        |             | https://fasttext.cc/docs/en/aligned-vectors.html                      | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |      |                | original fasttext aligned automaticaly |
| fasttext aligned supervised             |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |      | wiki           | original fasttext aligned supervised   |
| fasttext                                |             | https://fasttext.cc/docs/en/crawl-vectors.html                        | static word embeddings |                                                              |                                                                                 |      | cc + wiki      | original fasttext                      |
| ELMo Representations for Many Languages |             | https://github.com/HIT-SCIR/ELMoForManyLangs                          | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation                           |      |                |                                        |

## Slovenian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name         | description | huggingface card                                  | type | paper                            | citation                         | case      | pre-trained on | comments                         |
| ------------ | ----------- | ------------------------------------------------- | ---- | -------------------------------- | -------------------------------- | --------- | -------------- | -------------------------------- |
| CroSloEngual |             | https://huggingface.co/EMBEDDIA/crosloengual-bert | BERT | https://arxiv.org/abs/2006.07890 | https://arxiv.org/abs/2006.07890 | cased (?) | ?              | project site http://embeddia.eu/ |

### single language models

| name     | description | huggingface card                         | type    | paper | citation | case  | pre-trained on            | comments                                                   |
| -------- | ----------- | ---------------------------------------- | ------- | ----- | -------- | ----- | ------------------------- | ---------------------------------------------------------- |
| SloBERTa |             | https://huggingface.co/EMBEDDIA/sloberta | RoBERTa | ?     | ?        | cased | several Slovenian corpora | more details https://github.com/clarinsi/Slovene-BERT-Tool |

### other

| name                                       | description | huggingface card                                                      | type                   | paper                                                        | citation                                                                        | case | pre-trained on     | comments                                                              |
| ------------------------------------------ | ----------- | --------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ---- | ------------------ | --------------------------------------------------------------------- |
| ELMo embeddings models for seven languages |             | --                                                                    | ELMo                   | https://arxiv.org/abs/1911.10049                             | https://arxiv.org/abs/1911.10049                                                | ?    | some local corpora | more details https://www.clarin.si/repository/xmlui/handle/11356/1277 |
| MultiFiT                                   |             | https://nlp.fast.ai/                                                  | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |      |                    | multilingual ULMFiT                                                   |
| subs2vec                                   |             | https://github.com/jvparidon/subs2vec/                                | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |      | subtitles          |                                                                       |
| fasttext aligned                           |             | https://fasttext.cc/docs/en/aligned-vectors.html                      | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |      |                    | original fasttext aligned automaticaly                                |
| fasttext aligned supervised                |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |      | wiki               | original fasttext aligned supervised                                  |
| fasttext                                   |             | https://fasttext.cc/docs/en/crawl-vectors.html                        | static word embeddings |                                                              |                                                                                 |      | cc + wiki          | original fasttext                                                     |
| ELMo Representations for Many Languages    |             | https://github.com/HIT-SCIR/ELMoForManyLangs                          | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation                           |      |                    |                                                                       |
| Slovenské sémantické vektory pre word2vec  |             | https://github.com/essential-data/word2vec-sk                         | static word embeddings |                                                              |                                                                                 |      |                    |                                                                       |

## Ukrainian

### multilingual

| name        | description | huggingface card                                          | type        | paper                            | citation                                                                                 | case  | pre-trained on                 | comments |
| ----------- | ----------- | --------------------------------------------------------- | ----------- | -------------------------------- | ---------------------------------------------------------------------------------------- | ----- | ------------------------------ | -------- |
| mBERT       |             | https://huggingface.co/bert-base-multilingual-cased       | BERT        | https://arxiv.org/abs/1810.04805 | https://arxiv.org/abs/1810.04805                                                         | both  | multilingual, wiki             |          |
| XLM-R       |             | https://huggingface.co/xlm-roberta-base                   | XLM-RoBERTa | https://arxiv.org/abs/1911.02116 | https://arxiv.org/abs/1911.02116                                                         | cased | multilingual, CommonCrawl      |          |
| LaBSE       |             | https://huggingface.co/setu4993/LaBSE                     | BERT        | https://arxiv.org/abs/2007.01852 | https://huggingface.co/setu4993/LaBSE                                                    | cased | multilingual, translation task |          |
| mDistilBERT |             | https://huggingface.co/distilbert-base-multilingual-cased | DistilBERT  | https://arxiv.org/abs/1910.01108 | https://huggingface.co/distilbert-base-multilingual-cased#bibtex-entry-and-citation-info | both  | multilingual, wiki             |          |

### several languages

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### single language models

| name              | description | huggingface card                                                    | type    | paper | citation | case | pre-trained on | comments                                                                                                      |
| ----------------- | ----------- | ------------------------------------------------------------------- | ------- | ----- | -------- | ---- | -------------- | ------------------------------------------------------------------------------------------------------------- |
| ukr-roberta-base  |             | https://huggingface.co/youscan/ukr-roberta-base                     | RoBERTa | ?     | ?        | ?    | wiki + oscar   | github: https://github.com/youscan/language-models + descr: https://youscan.io/blog/ukrainian-language-model/ |
| Ukrainian Electra |             | https://huggingface.co/dbmdz/electra-base-ukrainian-cased-generator | Electra | ?     | ?        | ?    | wiki + oscar   | github https://github.com/stefan-it/ukrainian-electra                                                         |

### other

| name                                    | description | huggingface card                                                      | type                   | paper                                                        | citation                                                                        | case  | pre-trained on               | comments                               |
| --------------------------------------- | ----------- | --------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------- | ----- | ---------------------------- | -------------------------------------- |
| bert-base-uk-cased                      |             | https://huggingface.co/Geotrend/bert-base-uk-cased                    | DistilBERT             | https://aclanthology.org/2020.sustainlp-1.16.pdf             | https://aclanthology.org/2020.sustainlp-1.16.pdf                                | cased | mBERT distilled to Ukrainian |                                        |
| MultiFiT                                |             | https://nlp.fast.ai/                                                  | ULMFiT                 | https://aclanthology.org/D19-1572.pdf                        |                                                                                 |       |                              | multilingual ULMFiT                    |
| subs2vec                                |             | https://github.com/jvparidon/subs2vec/                                | static word embeddings | https://link.springer.com/article/10.3758/s13428-020-01406-3 |                                                                                 |       | subtitles                    |                                        |
| fasttext aligned                        |             | https://fasttext.cc/docs/en/aligned-vectors.html                      | static word embeddings | https://arxiv.org/abs/1804.07745                             | https://fasttext.cc/docs/en/aligned-vectors.html#references                     |       |                              | original fasttext aligned automaticaly |
| fasttext aligned supervised             |             | https://github.com/facebookresearch/MUSE#multilingual-word-embeddings | static word embeddings |                                                              | https://github.com/facebookresearch/MUSE#word-translation-without-parallel-data |       | wiki                         | original fasttext aligned supervised   |
| fasttext                                |             | https://fasttext.cc/docs/en/crawl-vectors.html                        | static word embeddings |                                                              |                                                                                 |       | cc + wiki                    | original fasttext                      |
| ELMo Representations for Many Languages |             | https://github.com/HIT-SCIR/ELMoForManyLangs                          | ELMo                   |                                                              | https://github.com/HIT-SCIR/ELMoForManyLangs#citation                           |       |                              |                                        |
| Ukrainian word embeddings               |             | https://lang.org.ua/en/models/                                        | static word embeddings |                                                              |                                                                                 |       |                              |                                        |
