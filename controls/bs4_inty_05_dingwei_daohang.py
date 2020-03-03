import requests
from bs4 import BeautifulSoup

data=requests.get('http://www.google.com')
print(data)
data=requests.get('http://www.google.com').content
print(data)
soup=BeautifulSoup(data,"html.parser")
print(soup.title)
print(soup.title.text)
print(soup.body)
print(soup.body.div)
print(soup.body.div.attrs)