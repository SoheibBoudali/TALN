def Load(file_name):
	file= open(file_name,"r")
	return file.read()
text=Load("Corpus.txt")
print(text)