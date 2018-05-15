from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.facebook.com/")
bsObj = BeautifulSoup(html.read(), "html.parser")

dom = open('facebook.html', "w")

dom.write(bsObj.prettify())
#print(bsObj.h1)
print(bsObj.prettify())
