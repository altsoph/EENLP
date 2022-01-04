import subprocess
import pandas as pd
import os
PREFIX = '_temp/'
subprocess.run(["mkdir", PREFIX])
subprocess.run(["wget", "https://drive.google.com/uc?export=download&id=1-Pr8yp_MHezKN0amAVo6VPjfArtdDAnF", "-O", os.path.join(PREFIX, 'train.json.zip')])
subprocess.run(["unzip",  "-o", os.path.join(PREFIX, 'train.json.zip'), '-d', PREFIX])


import json

with open(os.path.join(PREFIX, 'train.json')) as f:
    data = json.load(f)

df = pd.DataFrame(data)
df = df[['text', 'sentiment']]
df.columns = ['text', 'label']
df['language'] = 'Russian'

subprocess.run(["wget",  "-P", PREFIX, 'https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1342/croatian_sentiment_news_document.tsv'])

import pandas as pd
import requests

df_ = pd.read_csv(os.path.join(PREFIX, 'croatian_sentiment_news_document.tsv'), sep='\t').loc[:]
import re
def get_text(url):
    response = requests.get(url)
    m = re.search('.*"headline": "(.*)"[\s\S]*"articleBody": "(.*)"', response.text)
    return m.group(1) + ' ' + m.group(2)

def get_text_from_html(html_text):
    m = re.search('.*"headline": "(.*)"[\s\S]*"articleBody": "(.*)"', html_text)
    return m.group(1) + '. ' + m.group(2)

from tqdm import tqdm

html_texts = []

for url in tqdm(df_['url']):
    html_texts.append(requests.get(url).text)

texts = []
fails = []
successes = []
for i, html_text in tqdm(enumerate(html_texts), total=len(html_texts)):
    try:
        texts.append(get_text_from_html(html_text))
        successes.append(i)
    except:
        fails.append(i)

df_cleaned = df_.loc[successes].drop('ID', axis=1).drop('url', axis=1)
df_cleaned['text'] = texts
df_cleaned['language'] = 'Croatian'

df_cleaned = df_cleaned[['text', 'label', 'language']]
df = df.append(df_cleaned)


subprocess.run(["git",  "clone", 'https://github.com/19Joey85/Sentiment-annotated-news-corpus-and-sentiment-lexicon-in-Slovene.git', os.path.join(PREFIX, 'git')])
df_ = pd.read_csv(os.path.join(PREFIX,'git', 'Manually sentiment annotated Slovenian news corpus SentiNews 1.0/Annotation_document-level_utf8.txt'), sep='\t')
df_ = df_[['content', 'sentiment']]
df_.columns = ['text', 'label']
df_['language'] = 'Slovenian'
df = df.append(df_)

subprocess.run(["wget",  "https://drive.google.com/uc?export=download&id=1085LNAdhuxjk0JUNWUB5DrvVXgkP4GJO", "-O", os.path.join(PREFIX, 'lith_news.csv')])
df_ = pd.read_csv(os.path.join(PREFIX, 'lith_news.csv'), sep=';', encoding = "ISO-8859-1")
df_ = df_[['Text', 'Class']]
df_.columns = [['text', 'label']]
df_['language'] = 'Lithuanian'
df_.columns = ['text', ('label'), ('language')]
df_.label = df_.label.str.replace('POS', 'positive').str.replace('NEG', 'negative').str.replace('NEU', 'neutral')
df = df.append(df_)
df.to_csv('SENTIMENT_NEWS.csv', index=False)
subprocess.run(['rm', '-rf', PREFIX])
