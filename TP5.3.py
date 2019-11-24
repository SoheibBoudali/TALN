from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist
from nltk import bigrams
from operator import itemgetter

words= RegexpTokenizer(r'\w+').tokenize(open("Corpus.txt","r",encoding='utf-8').read())
stop_words= open("stopwords_fr.txt","r",encoding='utf-8').read().split()
words=[word for word in words if word not in stop_words]
bigrams= bigrams(words)
freqdist= FreqDist(bigrams)
for item in sorted(freqdist.items(), key=itemgetter(1), reverse=True)[:10]:
    print(item)