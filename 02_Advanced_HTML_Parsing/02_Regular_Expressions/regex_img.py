from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")

bsObj = BeautifulSoup(html, "html.parser")

images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})

fichero = open("regex_img.txt", "w")

for image in images:
    print(image["src"])
    fichero.write(str(image["src"]))
    fichero.write("\n")

fichero.close()