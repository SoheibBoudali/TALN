def Token(file_name):
	from nltk.tokenize import word_tokenize
	file= open(file_name,"r")
	words =word_tokenize(file.read())
	return words	
def PorStem(words):
	stemmer = nltk.PorterStemmer()
	stems=[stemmer.stem(word) for word in words]
	return stems
def LancStem(words):
	stemmer = nltk.LancasterStemmer()
	stems=[stemmer.stem(word) for word in words]
	return stems
import nltk
PorterStemmerList = PorStem(Token("Corpus.txt"))
LancasterStemmerList= LancStem(Token("Corpus.txt"))
diff=[]
for index in range(1,len(PorterStemmerList)):
	if PorterStemmerList[index]!=LancasterStemmerList[index]:
		diff.append((PorterStemmerList[index],'==>',LancasterStemmerList[index]))
print(diff)
print(len(diff))