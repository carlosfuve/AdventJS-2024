# Reto 19: 📦 Apila cajas mágicas para repartir regalos

¡Se acerca el día para repartir regalos! Necesitamos apilar los regalos que transportaremos en el trineo 🛷 y para eso los vamos a meter en cajas 📦.

Los regalos se pueden meter en 4 cajas distintas, donde cada caja soporta 1, 2, 5, 10 de peso y se representan así:

```python
"""
    _
1: |_|
    _____
2: |_____|
    _____
5: |     |
   |_____|
     _________
10: |         |
    |_________|
""""

boxRepresentations = {
  1: [" _ ", "|_|"] ,
  2: [" ___ ", "|___|"],
  5: [" _____ ", "|     |", "|_____|"],
  10: [" _________ ", "|         |", "|_________|"]
}
```

Tu misión es que al recibir el peso de los regalos, uses las mínimas cajas posibles y que, además, las apiles de menos peso (arriba) a más peso (abajo). Siempre alineadas a la izquierda.

Además, ten en cuenta que al apilarlas, se reusa el borde inferior de la caja.

```python
distribute_weight(1)
# Devuelve:
#  _
# |_|

distribute_weight(2)
# Devuelve:
#  ___
# |___|

distribute_weight(3)
# Devuelve:
#  _
# |_|_
# |___|

distribute_weight(4)
# Devuelve:
#  ___
# |___|
# |___|

distribute_weight(5)
# Devuelve:
#  _____
# |     |
# |_____|

distribute_weight(6)
# Devuelve:
#  _
# |_|___
# |     |
# |_____|
```
**Nota: ¡Ten cuidado con los espacios en blanco! No añadas espacios en blanco a la derecha de una caja si no son necesarios.**
