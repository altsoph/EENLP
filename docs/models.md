# Models x Languages Matrix

|                    | multilingual | multilingual | multilingual | multilingual | several languages | several languages | several languages | several languages | several languages | single language models | single language models | single language models | single language models | single language models |
| ------------------ | :----------: | :----------: | :----------: | :----------: | :---------------: | :---------------: | :---------------: | :---------------: | :---------------: | :--------------------: | :--------------------: | :--------------------: | :--------------------: | :--------------------: |
| Albanian           |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |                        |       AL-RoBERTa       |                        |                        |                        |
| Armenian           |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |                        |                        |                        |                        |                        |
| Belarusian         |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |                        |                        |                        |                        |                        |
| Bosnian            |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |      BERTić       |                   |                   |                   |                        |       BA-RoBERTa       |                        |                        |                        |
| Bulgarian          |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |    SlavicBERT     |                   |                   |                        | RoBERTa-base-bulgarian |                        |                        |                        |
| Croatian           |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |   CroSloEngual    |      BERTić       |                   |                   |                   |                        |                        |                        |                        |                        |
| Czech              |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |    SlavicBERT     |                   |                   |         CZERT          |       RobeCzech        |                        |                        |      Czech ALBERT      |
| Estonian           |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |      FinEst       |        EstBERT         |      est-roberta       |                        |                        |                        |
| Georgian           |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |                        |                        |                        |                        |                        |
| Hungarian          |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |         huBERT         |                        |                        |                        |                        |
| Kazakh             |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |                        |                        |                        |                        |                        |
| Latvian            |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |    LitLat BERT    |                   |        LV-BERT         |                        |                        |                        |                        |
| Lithuanian         |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |    LitLat BERT    |                   |                        |                        |                        |                        |                        |
| Macedonian         |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |    Macedonian BERT     |       MK-RoBERTa       | Macedonian DistilBERT  |   Macedonian Electra   |                        |
| Moldovan/Moldovian |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |                        |                        |                        |                        |                        |
| Montenegrin        |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |      BERTić       |                   |                   |                   |                        |                        |                        |                        |                        |
| Polish             |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |    SlavicBERT     |                   |                   |    Polbert /HerBERT    |     Polish RoBERTa     |                        |                        |                        |
| Romanian           |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |  RoBERT/Romanian BERT  |                        |  Romanian DistilBERT   |                        |                        |
| Russian            |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |    SlavicBERT     |                   |                   |         RuBERT         |    Russian RoBERTa     |                        |                        |                        |
| Serbian            |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |      BERTić       |                   |                   |                   |                        |                        |                        |                        |                        |
| Slovakian/Slovak   |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |                        |                        |                        |                        |                        |
| Slovenian          |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |   CroSloEngual    |                   |                   |                   |                   |                        |        SloBERTa        |                        |                        |                        |
| Ukrainian          |    mBERT     |    XLM-R     |    LaBSE     | mDistilBERT  |                   |                   |                   |                   |                   |                        |    ukr-roberta-base    |                        |   Ukrainian Electra    |                        |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Bosnian

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Bulgarian

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Croatian

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Czech

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Estonian

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Latvian

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Lithuanian

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Montenegrin

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Polish

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Russian

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Serbian

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

## Slovenian

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

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

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |

### other

| name | description | huggingface card | type | paper | citation | case | pre-trained on | comments |
| ---- | ----------- | ---------------- | ---- | ----- | -------- | ---- | -------------- | -------- |
