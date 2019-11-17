def Load(file_name):
	file= open(file_name,"r")
	return file.read()

def PuncTokenizer(text , reg_exp):
	from nltk.tokenize import RegexpTokenizer
	tokenizer =  RegexpTokenizer(reg_exp)
	return tokenizer.tokenize(text)
from re import VERBOSE
regex_punct=r"""(?x)
 [^\w\s]+  # poctuation 
""" 
print(PuncTokenizer(Load("Corpus.txt"), regex_punct))
