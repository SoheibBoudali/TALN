from nltk.corpus import brown
words =[word for word in brown.words() if brown.words().count(word)>2]
print(words)
