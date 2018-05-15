from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

file_selectors = open("example-file.txt", "w")

bsObj = BeautifulSoup(html.read(), "html.parser")
#nameList = bsObj.find_all("span", {"class":"green"})
#nameList = bsObj.findAll({"h1","h2","h3","h4","h5","h6"})
nameList = bsObj.findAll("span", {"class" : "green", "class" : "red"})

#print(bsObj.prettify())

for name in nameList:
    print(name)
    file_selectors.write(name.get_text())

# hay una diferencia entre name y name.get_text()
# el primero devuelve los tags <>
# y el segundo devuelve el contenido
file_selectors.close()
