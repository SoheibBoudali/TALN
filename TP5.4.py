from nltk import ConditionalFreqDist
from nltk.corpus import brown

CondFreqDist=ConditionalFreqDist((categorie,word) for categorie in brown.categories() for word in brown.words(categories=categorie))
mots=['The', 'Fulton', 'County', 'Grand', 'Jury', 'said']
CondFreqDist.tabulate(samples=mots)
