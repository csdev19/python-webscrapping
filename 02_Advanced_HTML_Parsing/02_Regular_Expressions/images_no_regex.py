# without REGEX
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.pythonscraping.com/pages/page3.html")

bsObj = BeautifulSoup(html.read(), "html.parser")

find_table = bsObj.find("table", {'id': 'giftList'})

children_table = find_table.children
#print(bsObj)
#print(find_table)


fichero = open("no_regex.txt", "w")

#img_table = children_table.findAll("img", {})

for i in children_table:
    img = i.find("img")
    print(img)
    fichero.write(str(img))


fichero.close()
