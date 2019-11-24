def tf(word , categorie):
    freqdist= FreqDist(brown.words(categories=categorie))
    print("la frequence du mot: "+word+" dans le text: "+categorie+" est ",freqdist[word])

from nltk.corpus import brown
from nltk import FreqDist

tf("the" , "adventure")
