from nltk.corpus import brown
from nltk import ConditionalFreqDist

CondFreqDist=ConditionalFreqDist((categorie,word) for categorie in brown.categories() for word in brown.words(categories=categorie))
for categorie in CondFreqDist:
    total=0
    for word in CondFreqDist[categorie]:
        total+=CondFreqDist[categorie][word]
    print(categorie+" ===> "+str(total/len(CondFreqDist[categorie])))