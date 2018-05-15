# Lambda Expressions

Es una opcion a usar **REGEX**, la cual se basa en usar **funciones anonimas** cuando quieras hacer una busqueda con **BS4**.
Porque esta nos permite pasar estos tipos de funciones como parametros a la funcion **findAll()**. Y la unica restriccion en estas funciones es tomar un **objeto etiqueta(tag)** y pasarlo como argumento y que retorne un valor booleano.
En **BS4** todo **objeto etiqueta** que encuentre sera evaluado en esa funcion y las **etiquetas** que sean valuadas como **true** y seran retornadas. Mientras el resto seran descartadas.

Por ejemplo:
```python
# por ejemplo esta funcion devuelve todos los tags con 2 atributos
soup.findAll(lambda tag: len(tag.attrs) == 2)
```

```html
<div class="body" id="content"></div>
<span style="color:red" class="title"></span>
```


