import nltk 
file = nltk.corpus.gutenberg.words('austen-emma.txt')
list=[]
for word in file:
	if word.startswith('wh'):
		list.append(word)
l=set(list)
print('there is', len(l) ,'word ')