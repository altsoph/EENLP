import json
from collections import defaultdict
from glob import glob
import subprocess
import os

PREFIX = '_temp/'

subprocess.run(["wget",  "-P", PREFIX, "-c", 'https://xglue.blob.core.windows.net/xglue/xglue_full_dataset.tar.gz'])
subprocess.run(["tar",  "--overwrite", '-xf', PREFIX + 'xglue_full_dataset.tar.gz', '-C', PREFIX])


subprocess.run(["wget",  "-P", PREFIX, "-c", 'https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1408/ee_articles_2015-2019.zip'])
subprocess.run(["unzip",  "-o", PREFIX+'ee_articles_2015-2019.zip', '-d', PREFIX])
subprocess.run(["wget",  "-P", PREFIX, "-c", 'https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1409/lv_articles_entire_collection.zip'])
subprocess.run(["unzip",  "-o", PREFIX+'lv_articles_entire_collection.zip', '-d', PREFIX])
subprocess.run(["wget",  "-P", PREFIX, "-c", 'https://files.kemt.fei.tuke.sk/nlpstatic/files/scnc1.zip'])
subprocess.run(["unzip",  "-o", PREFIX+'scnc1.zip', '-d', PREFIX])

subprocess.run(["git",  "clone", 'https://github.com/ispras-texterra/word-embeddings-eval-hy', os.path.join(PREFIX, 'am.git')])
subprocess.run(["git",  "clone", 'https://github.com/butnaruandrei/MOROCO', os.path.join(PREFIX, 'mr.git')])

def mapcat(data, markers):
    if data['category'] not in markers: return None
    data['category'] = markers[data['category']]
    return data

def resplit(split, split_resolve, idx):
    if split_resolve[split] in ('test', 'train'): return split_resolve[split]
    if not idx%split_resolve[split]: return 'test'
    return 'train'

from os import listdir, makedirs
from os.path import isfile, join, splitext, exists

# Assume the data set is in the below subfolder
inputDataPrefix = "_temp/mr.git/MOROCO/preprocessed/"

# Loads the samples in the train, validation, or test set
def loadMOROCODataSamples(subsetName):
    inputSamplesFilePath = (inputDataPrefix + "%s/samples.txt") % (subsetName)
    inputDialectLabelsFilePath = (inputDataPrefix + "%s/dialect_labels.txt") % (subsetName)
    inputCategoryLabelsFilePath = (inputDataPrefix + "%s/category_labels.txt") % (subsetName)
    IDs = []
    samples = []
    dialectLabels = []
    categoryLabels = []
    # Loading the data samples
    inputSamplesFile = open(inputSamplesFilePath, 'r', encoding='utf-8')
    sampleRows = inputSamplesFile.readlines()
    inputSamplesFile.close()

    for row in sampleRows:
        components = row.split("\t")
        IDs += [components[0]]
        samples += [" ".join(components[1:])]

    # Loading the dialect labels
    inputDialectLabelsFile = open(inputDialectLabelsFilePath, 'r', encoding='utf-8')
    dialectRows = inputDialectLabelsFile.readlines()
    inputDialectLabelsFile.close()
    
    for row in dialectRows:
        components = row.split("\t")
        dialectLabels += [int(components[1])]
    
    # Loading the category labels
    inputCategoryLabelsFile = open(inputCategoryLabelsFilePath, 'r', encoding='utf-8')
    categoryRows = inputCategoryLabelsFile.readlines()
    inputCategoryLabelsFile.close()
    
    for row in categoryRows:
        components = row.split("\t")
        categoryLabels += [int(components[1])]

    # IDs[i] is the ID of the sample samples[i] with the dialect label dialectLabels[i] and the category label categoryLabels[i]
    return IDs, samples, dialectLabels, categoryLabels

def get_scnc1_text(fn):
    words = []
    with open(fn, encoding='utf-8') as f:
        for l2 in f:
            tokens = l2.rstrip().split()
            for token in tokens:
                annots = token.split("|")
                word = annots[0]
                words.append( word )
    text = " ".join(words)
    return text


ofn = f'CAT_NEWS.jsonl'
with open(ofn, 'w', encoding='utf-8') as ofh:

    # Armenian
    source_title = 'iLur.am News Texts Dataset'
    markers = {'culture': 'entertainment/culture', 'economy': 'finance/business/economy', 'accidents': 'news/accidents', 'sport': 'sports', 'society': 'lifestyle'}
    language = 'Armenian'
    title = None
    split_resolve = {'test':'test', 'train':'train'}

    for split in split_resolve:
        idx = 0
        for fn in glob(f'_temp/am.git/ilur-news-corpus/{split}/*/*txt'):
            _,_,_,_,cat,fn_short = fn.split('/')
            text = open(fn, encoding='utf-8').read()
            item = {'lang':language, 'title':title, 'text':text, 'category':cat, 'source':source_title, 'split':split}
            item = mapcat(item, markers)
            if item:
                item['split'] = resplit(split, split_resolve, idx)
                print(json.dumps(item), file=ofh)
                idx += 1

    # Estonian
    source_title = 'Estonian article dataset'
    language = 'Estonian'
    split_resolve = {'full':5}
    markers = {'Auto': 'auto/tech', 'Kultuur': 'entertainment/culture', 'Muusika': 'entertainment/culture', 'Teater': 'entertainment/culture', 'Maamajandus': 'finance/business/economy', 'Tervis': 'health', 'Mood ja ilu': 'lifestyle', 'Sisustus ja disain': 'lifestyle', 'Eesti': 'news/accidents', 'Reisiuudised': 'travel', 'Äpid ja nett': 'auto/tech', 'Tehnika': 'auto/tech'}

    for split in split_resolve:
        idx = 0
        for fn in glob('_temp/ee_*.json'):
            data = open(fn, encoding='utf-8').read()
            data = json.loads(data)
            for item in data:
                try:
                    title = item['title']
                    cat = item['categoryPrimary']['categoryName']
                    llang = item['channelLanguage']
                    text = item['bodyText']
                    if llang != 'nat': continue

                    item = {'lang':language, 'title':title, 'text':text, 'category':cat, 'source':source_title, 'split':split}
                    item = mapcat(item, markers)
                    if item:
                        item['split'] = resplit(split, split_resolve, idx)
                        print(json.dumps(item), file=ofh)
                        idx += 1
                except:
                    pass

    # Latvian
    source_title = 'Latvian articles dataset'
    language = 'Latvian'
    split_resolve = {'full':5}
    markers = {'Kultūrvide': 'entertainment/culture', 'Bankas un finanses': 'finance/business/economy', 'Vesela un laimīga': 'health', 'VESELĪBAS CEĻVEDIS': 'health', 'Stila ziņas': 'lifestyle', 'Stils': 'lifestyle', 'Ziņas': 'news/accidents', 'Futbols': 'sports', 'Sportacentrs.com "Ārpus kadra"': 'sports', 'Es ceļoju': 'travel', 'Tehnoloģijas': 'auto/tech'}

    for split in split_resolve:
        idx = 0
        for fn in glob('_temp/lv_*.json'):
            data = open(fn, encoding='utf-8').read()
            data = json.loads(data)
            for item in data:
                try:
                    title = item['title']
                    cat = item['categoryPrimary']['categoryName']
                    llang = item['channelLanguage']
                    text = item['bodyText']
                    if llang != 'nat': continue

                    item = {'lang':language, 'title':title, 'text':text, 'category':cat, 'source':source_title, 'split':split}
                    item = mapcat(item, markers)
                    if item:
                        item['split'] = resplit(split, split_resolve, idx)
                        print(json.dumps(item), file=ofh)
                        idx += 1
                except:
                    pass

    # English
    source_title = 'XGLUE'
    language = 'English'
    split_resolve = {'train':'train','test':'test','dev':'test'}
    markers = {'entertainment': 'entertainment/culture', 'finance': 'finance/business/economy', 'news': 'news/accidents', 'sports': 'sports', 'lifestyle': 'lifestyle', 'autos': 'auto/tech', 'health': 'health', 'travel': 'travel'}

    for split in split_resolve:
        idx = 0
        inf = f'_temp/xglue_full_dataset/NC/xglue.nc.en.{split}'
        for line in open(inf, encoding='utf-8'):
            chunks = line.strip().split('\t')
            title, text, cat = chunks

            item = {'lang':language, 'title':title, 'text':text, 'category':cat, 'source':source_title, 'split':split}
            item = mapcat(item, markers)
            if item:
                item['split'] = resplit(split, split_resolve, idx)
                print(json.dumps(item), file=ofh)
                idx += 1

    # Russian
    source_title = 'XGLUE'
    language = 'Russian'
    split_resolve = {'test':5,'dev':5}
    markers = {'entertainment': 'entertainment/culture', 'finance': 'finance/business/economy', 'news': 'news/accidents', 'sports': 'sports', 'lifestyle': 'lifestyle', 'autos': 'auto/tech', 'health': 'health', 'travel': 'travel'}

    for split in split_resolve:
        idx = 0
        inf = f'_temp/xglue_full_dataset/NC/xglue.nc.ru.{split}'
        for line in open(inf, encoding='utf-8'):
            chunks = line.strip().split('\t')
            title, text, cat = chunks

            item = {'lang':language, 'title':title, 'text':text, 'category':cat, 'source':source_title, 'split':split}
            item = mapcat(item, markers)
            if item:
                item['split'] = resplit(split, split_resolve, idx)
                print(json.dumps(item), file=ofh)
                idx += 1

    # MOROCO
    cats = { 1 : "culture", 2 : "finance", 3 : "politics", 4 : "science", 5 : "sports", 6 : "tech" }
    lngs = { 1 : "Moldavian", 2 : "Romanian" }
    source_title = 'MOROCO'
    split_resolve = {'train':'train','test':'test','validation':'train'}
    markers = {'culture': 'entertainment/culture', 'finance': 'finance/business/economy', 'news': 'news/accidents', 'sports': 'sports', 'lifestyle': 'lifestyle', 'tech': 'auto/tech', 'health': 'health'}
    title = None

    for split in ('train', 'test', 'validation'):
        idx = 0
        trainIDs, trainSamples, trainDialectLabels, trainCategoryLabels = loadMOROCODataSamples(split)
        for _,text,dia,cat in zip(trainIDs, trainSamples, trainDialectLabels, trainCategoryLabels):
            language = lngs[dia]
            cat  = cats[cat]

            item = {'lang':language, 'title':title, 'text':text, 'category':cat, 'source':source_title, 'split':split}
            item = mapcat(item, markers)
            if item:
                item['split'] = resplit(split, split_resolve, idx)
                print(json.dumps(item), file=ofh)
                idx += 1

    # Slovak
    source_title = 'Slovak Categorized News Corpus'
    language = 'Slovak'
    markers = {'Kultúra': 'entertainment/culture', 'Ekonomika_a_firmy': 'finance/business/economy', 'Správy': 'news/accidents', 'Šport': 'sports', 'Svet': 'lifestyle', 'autos': 'auto/tech', 'Zdravotníctvo': 'health', 'travel': 'travel'}
    split_resolve = {'full':5}
    split = 'full'

    fn2title = dict()
    fn2tag = dict()
    for line in open('_temp/scnc1/corpus.list', encoding='utf-8'):
        chunks = line.strip().split('\t')
        _,tag,fn = chunks[0].split('/')
        fn2title[fn] = chunks[1]
        fn2tag[fn] = tag

    idx = 0
    for fn in glob('_temp/scnc1/corpus/*/*txt'):
        fn_short = fn.split('/')[-1]
        text = get_scnc1_text(fn)
        title = fn2title[fn_short]
        cat = fn2tag[fn_short]

        item = {'lang':language, 'title':title, 'text':text, 'category':cat, 'source':source_title, 'split':split}
        item = mapcat(item, markers)
        if item:
            item['split'] = resplit(split, split_resolve, idx)
            print(json.dumps(item), file=ofh)
            idx += 1


# Print out final stats
stats = defaultdict(int)
with open(ofn, 'r', encoding='utf-8') as ifh:
    for item in ifh:
        item = json.loads(item)
        stats[(item['lang'],item['split'])] += 1

for k in stats:
    print(k, '\t', stats[k])

print()

subprocess.run(['rm', '-rf', PREFIX])
