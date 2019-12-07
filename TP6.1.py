import nltk
from nltk import FreqDist
from operator import itemgetter



word_tag_liste=nltk.corpus.brown.tagged_words()
sing_word=[word for word in word_tag_liste if word[1]=="NN"]
plur_word=[word for word in word_tag_liste if word[1]=="NNS"]
liste=[]
sing_freqdist=FreqDist(sing_word)
plur_freqdist=FreqDist(plur_word)
for sing in sing_freqdist.items():
	s_to_p=sing[0][0]+'s'
	for plur in plur_freqdist.items():
		if s_to_p==plur[0][0] and plur[1] > sing[1]:
			liste.append(s_to_p)
			break
print(liste)
