import requests
from bs4 import BeautifulSoup 
url = "https://www.usthb.dz/fr"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib') 
file=open('file.txt', 'w+')
page = soup.prettify()
file.write(str(page))
file.close()
