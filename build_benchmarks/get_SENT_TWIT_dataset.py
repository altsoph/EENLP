import pandas as pd
import subprocess
import pandas as pd
import os

PREFIX = '_temp/'
subprocess.run(['mkdir', PREFIX])
subprocess.run(["wget",  "https://drive.google.com/uc?export=download&id=1uzN9zBdNj8S3WsqESS6hgqzf2n1E968w", "-O", os.path.join(PREFIX, 'russian_twitter.csv')])
df = pd.read_csv(os.path.join(PREFIX, 'russian_twitter.csv'))

subprocess.run(["git",  "clone", 'https://github.com/FnTm/latvian-tweet-sentiment-corpus.git', os.path.join(PREFIX, 'git')])

import json
with open(os.path.join(PREFIX, 'git', 'tweet_corpus.json'), 'r') as f:
    data = f.readlines()

from copy import deepcopy
datadicts = []
data_=deepcopy(data)
data_[0] = data_[0][1:]
fails = []
for i, datastring in enumerate(data_):
    try:
        datadicts.append(json.loads(datastring.strip()[:-1]))
    except:
        fails.append(i)

import pandas as pd

df_ = pd.DataFrame(datadicts)

df_ = df_[['text', 'sentiment']]

df_.columns = ['text', 'label']
df_['language'] = 'Latvian'
df_ = df_.replace('NEU', 'neutral').replace('NEG', 'negative').replace('POZ', 'positive')
df = df.append(df_)
subprocess.run(["git",  "clone", 'https://github.com/kysely/sentiment-analysis-czech.git', os.path.join(PREFIX, 'git2')])
labels_path = os.path.join(PREFIX, 'git2', 'data/facebook/gold-labels.txt')
posts_path = os.path.join(PREFIX, 'git2','data/facebook/gold-posts.txt')

with open(labels_path) as f:
    labels = [s.strip() for s in f.readlines()]
with open(posts_path) as f:
    posts = [s.strip() for s in f.readlines()]
df_ = pd.DataFrame([posts, labels,]).transpose()
df_.columns = ['text', 'label']
df_['language'] = 'Czech'
df_.label = df_.label.str.replace('0', 'neutral').str.replace('p', 'positive').str.replace('n', 'negative')
df = df.append(df_)
import pandas as pd
subprocess.run(["wget",  "https://drive.google.com/uc?export=download&id=1uZZE1Hhc1Xwms5U0AZg87Zi1Ar50ksQZ", "-O", os.path.join(PREFIX, 'slovak_twitter.csv')])
df_ = pd.read_csv(os.path.join(PREFIX, 'slovak_twitter.csv'))
df = df.append(df_)
df.to_csv('SENTIMENT_TWITTER.csv', index=False)
subprocess.run(['rm', '-rf', PREFIX])
