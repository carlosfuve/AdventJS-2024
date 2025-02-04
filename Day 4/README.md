# Reto 4: 🎄 Decorando el árbol de navidad

¡Es hora de poner el árbol de Navidad en casa! 🎄 Pero este año queremos que sea especial. Vamos a crear una función que recibe la altura del árbol (un entero positivo entre 1 y 100) y un carácter especial para decorarlo.

La función debe devolver un string que represente el árbol de Navidad, construido de la siguiente manera:
- El árbol está compuesto de triángulos de caracteres especiales.
- Los espacios en blanco a los lados del árbol se representan con guiones bajos _.
- Todos los árboles tienen un tronco de dos líneas, representado por el carácter #.
- El árbol siempre debe tener la misma longitud por cada lado.
- Debes asegurarte de que el árbol tenga la forma correcta usando saltos de línea \n para cada línea.


```python
create_xmas_tree(5, '*')
"""
____*____
___***___
__*****__
_*******_
*********
____#____
____#____
"""

create_xmas_tree(3, '+')
""" 
__+__
_+++_
+++++
__#__
__#__
"""

create_xmas_tree(6, '@')
""" 
_____@_____
____@@@____
___@@@@@___
__@@@@@@@__
_@@@@@@@@@_
@@@@@@@@@@@
_____#_____
_____#_____
"""
```