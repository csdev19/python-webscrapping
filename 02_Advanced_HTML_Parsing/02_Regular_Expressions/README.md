# Regular Expressions (REGEX)

Un chiste de **REGEX** : “Let’s say you have a problem, and you decide to solve it with regular expressions. Well, now you have two problems.”

## Porque REGEX es util ?

Nos permite **parsear** cadenas de texto complejas, siguiendo patrones predefinidos.
La manera mas facil de descomponer una cadena de texto compleja (complex string) es **generalizando la cadena en un patron y luego escribir una REGEX que describe dicho patron**.


## Pasos para usarla

1. Generalizar un ejemplo.
    ```python
    (nombre del ingrediente) : (digitos de cantidad)  (palabras unidades)
    ```
   - Hemos reemplazado el **texto literal** con un resumen de dso partes: **lo que significa** y **como es representados**. Por ejemplo: **ingredientes** : por palabras , **monto** : como digitos.
2. Reescribimos el patron en notacion **REGEX**:
    ```python
    >> import re
    >> pattern_text = r'(?P<ingrediente>\w+):\s+(?P<monto>\d+)\s+(?P<unidad>\w+)'
    ```
    - Hemos reemplazado sugerencias de representaciones como **palabras** con **\w+**.
    - Los **digitos** con **\d+**.
    - Y los **espacios en blanco** con **\s+** para permitir 1 o mas espacios para ser usados como puntuacion.
    - Dejamos el simbolo **":"** porque en **REGEX** se empareja consigo misma.
    - Para cada uno de los campos, usamos **?P<nombre>** para darle un nombre a los datos que queremos identificar. No pusimos identificadores en los espacios o en los dos puntos, porque no queremos guardar estos caracteres.
    - **REGEX** usa mucho los caracteres **"\"**. Para hacer que esto funcione bien en **Python**. Debemos usar **"raws"** strings (cadenas brutas). Usando el **prefijo** **r''** esto le dice a **Python** que no vea el caracter **\** y los reemplaze con caracteres especiales que no estan en el teclado convencional.
3. Compilar el patron:
    ```python
    >>> pattern = re.compile(pattern_text)
    ```
4. Emparejar el patron con el texto de entrada. Y si el texto de entrada **concuerda**(match) con el patron. Recibiremos el **math object** el cual muestra los detalles del **matching**:
    ```python
    >>> match = pattern.match(ingrediente)
    >> match is None # esta vacio ?
    False
    >>> match.groups()
    ('platanos', '2', 'manos')
    ```
    - Esto por si solo es muy util. Tener una **tupla** de diferentes campos dentro de strings.
5. Extraer los grupos de caracteres nombrados del objeto coindicidente:
    ```python
    >>> match.group('ingrediente')
    'platanos'
    >>> match.group('monto')
    '2'
    >>> match.group('unidad')
    'manos'
    ```
    - Dicho grupo es identificado por el nombre que usamos en **(?P<nombre>..)** como parte de **REGEX**.

## Como funciona

Hay varios tipos diferentes de patrones que podemos describir con **REGEX**:

- Hemos mostrado una serie de clases de caracteres:
    - \w : Coincide con cualquier caracter alfanumerico (A-Z, a-z, 0-9
    - \d : Coincide con cualquier digito decimal
    - \s : Coincide con cualquier espacio o tabulacion
- Y estas tienen inversos:
    - \W : Coincide con cualquier caracter que no sea letra o digito
    - \D : Coincide con cualquier caracter que no sea un digito
    - \S : Coincide con cualquier caracter que no sea un espacio o tabulacion
- Varios caracteres coinciden consigo mismos al momento de ser interpretados por **REGEX**. Algunos caracteres tienes significados especiales y debemos usar **\** para evitar que eso pase.
    - Vimos el sufijo **+** que indica, que coincide con uno o mas de los precedentes **patrones**. **\d+** coincide con uno o mas digitos. Para hacer que coincida con un simple **+** necesitamos usar **\+**.
    - Tambien tenemos el sufijo ** * ** que coincide con ninguno o muchos de los patrones que los preceden. ** \w* ** coincide con 0 o varios caracteres. Para hacer que coincida un ** * ** debemos usar ** \* ** .
    - Tenemos el sufijo **?** que coincide con cero o uno de las expresiones precedentes. Este caracter es usado en otros lugares, y tiene diferentes significados. Lo vimos en **(?<nombre>..)** donde estuvo dentro de **()** para definir propiedades especiales en el grupo.
    - El **.** coincide con cualquier caracter individual. Para coincidir con **.** en especifico usamos **\.**

- Podemos crear nuestro propios conjuntos de caracteres unicos usando **[]** para encerrar los elementos en el grupo. tendremos algo como esto.
    ```python
    (?P<nombre>\w+)\s*[=:]\s*(?P<valor>.*)
    ```
    - Lo podemos usar para parsear cadenas como estas -> "size = 12" , "weight : 14".
    - Nos permite ser flexible con la puntuacion y asi tener un programa mas robusto con menos cambios.
