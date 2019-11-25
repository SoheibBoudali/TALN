from nltk import ConditionalFreqDist
from nltk.corpus import brown
import matplotlib
words=['The', 'Fulton', 'County', 'Grand', 'Jury', 'said']
CondFreqDist=ConditionalFreqDist((categorie,word) for categorie in brown.categories() for word in brown.words(categories=categorie))
CondFreqDist.tabulate(samples=words)