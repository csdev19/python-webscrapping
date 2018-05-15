# Funciones de BeautifulSoup

- **find**
    ```python
    find(tag, attributes, recursive, text, keywords)
    ```
- **findAll**: Una funcion que extrae valores dentro de una lista de **nombres propios del HTML**. Es una funcion que usaremos mucho.
    ```python
    findAll(tag, tag-attributes, recursive, text, limit, keywords)
    # <tag-attributes> es un diccionario

    # example
    .findAll({"h1","h2","h3","h4","h5","h6"})
    .findAll("span", {"class":"green", "class":"red"})

    # estas dos lineas son identicas
    bsObj.findAll(id="text")
    bsObj.findAll("", {"id":"text"})
    ```
- **tagName**
- **get_text**
-


