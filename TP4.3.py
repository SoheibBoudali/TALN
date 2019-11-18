from nltk.corpus import brown
cats = brown.categories()
averege_word_list=[]
averege_sent_list=[]
for cat in cats:
	words_length=0
	words=brown.words(categories=cat)
	for word in words:
		words_length+=len(word)
	averege_word_list.append(words_length/len(words))
	sents_length=0
	sents = brown.sents(categories=cat)
	for sent in sents:
		sents_length+=len(sent)
	averege_sent_list.append(sents_length/len(sents))
Uw=[(cats[i] , averege_word_list[i]) for i in range(0,len(cats))]
Us=[(cats[i] , averege_sent_list[i]) for i in range(0,len(cats))]
UwUsARI=[(cats[i],'Uw :', averege_word_list[i] , 'Us :' ,averege_sent_list[i], 'ARI :', 4.71*averege_word_list[i]+ 0.5*averege_sent_list[i] - 21.43) for i in range(0,len(cats))]
for uwusari in UwUsARI:
	print(uwusari)
