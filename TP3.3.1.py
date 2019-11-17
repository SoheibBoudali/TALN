import  nltk, re, pprint
f = open('file.txt')
page = f.read()
page = re.sub('<script\s(.*)>(.*)</script>','',page)
"""page = re.sub('<.*>', '\n', page)
page = re.sub('<!--(.|\n)*?-->', '', page)
page = re.sub('<!--(.*?)-->', '', page)
page = re.sub('\s+', ' ', page)
page = re.sub('\n', ' ', page)"""

print(page)
