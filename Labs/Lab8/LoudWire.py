import requests, re
from bs4 import BeautifulSoup

r = requests.get('https://loudwire.com/category/concerts').content
soup = BeautifulSoup(r, "lxml")
print(type(soup))
print(soup.prettify()[:100])
for title in soup.find_all('a', attrs={'class':re.compile("^title")}):
    print(title.text.strip())
                                          
