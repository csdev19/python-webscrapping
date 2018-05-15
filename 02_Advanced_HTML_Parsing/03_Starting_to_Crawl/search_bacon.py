from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")

bsObj = BeautifulSoup(html, "html.parser")

contador = 0

fichero = open("links_bacon_wiki.txt", "w")

for link in bsObj.findAll("a"):
    print(link)
    if 'href' in link.attrs:
        contador += 1
        cadena = (str(contador)+ ".- " + link.attrs['href']+"\n")
        fichero.write(cadena)


fichero.close()
print("hay {} links".format(contador))
