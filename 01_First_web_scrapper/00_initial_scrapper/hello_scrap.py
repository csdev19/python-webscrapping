from urllib.request import urlopen
html = urlopen("https://www.facebook.com/")

file_dom = open("example.html", "w")

dom = str(html.read())
file_dom.write(dom)

print(dom)
