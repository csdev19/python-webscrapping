# Encontramos un patron de los links en wiki
#   - Estan siempre dentro de un div con un id = bodyContent
#   - Las URLs no contienen puntos y coma
#   - Las URLs empiezan con /wiki/

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")

# el patron encontrado transformado a regex
pattern_href = "^(/wiki/)((?!:).)*$"
search_id = bsObj.find("div", {"id":"bodyContent"})
links =  search_id.findAll("a", href=re.compile(pattern_href))
#Original
#links =  bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile(pattern_href))

contador = 0
for link in links:
    if 'href' in link.attrs:
        print(link.attrs['href'])
        contador += 1

print("hay {} links".format(contador))
