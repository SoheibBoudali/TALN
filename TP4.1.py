def Load(file_name):
	file= open(file_name,"r")
	return file.read()

def PuncTokenizer(text):
	from re import VERBOSE
	regex_punct=r"""(?x)
 	[^\w\s]+  # poctuation 
	""" 
	from nltk.tokenize import RegexpTokenizer
	tokenizer =  RegexpTokenizer(regex_punct)
	return tokenizer.tokenize(text)
print(PuncTokenizer(Load("Corpus.txt")))

def Tokenizer(text):
	from  nltk.tokenize import RegexpTokenizer
	from re import VERBOSE
	reg_ex=r"""(?x)
	\$\d+(?:\.\d+)? #sommes monétaires en dollar
	|\£\d+(?:\.\d+)? #sommes monétaires en euro
	|\d{1,2}.\d{1,2}.\d{4} #date format dd X mm X yyyy month format numeric
	|\d{1,2}.(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).\d{4} #date format dd X mm X yyyy month format string
	"""
	tokenizer = RegexpTokenizer(reg_ex)
	return tokenizer.tokenize(text)
print(Tokenizer(Load("Corpus.txt")))


#ussuse