# Reto 1: 🎁 ¡Primer regalo repetido!

Santa Claus 🎅 ha recibido una lista de números mágicos que representan regalos 🎁, pero algunos de ellos están duplicados y deben ser eliminados para evitar confusiones. Además, los regalos deben ser ordenados en orden ascendente antes de entregárselos a los elfos.

Tu tarea es escribir una función que reciba una lista de números enteros (que pueden incluir duplicados) y devuelva una nueva lista sin duplicados, ordenada en orden ascendente.

```python
gifts1 = [3, 1, 2, 3, 4, 2, 5]
prepare_gifts(gifts1) # [1, 2, 3, 4, 5]

gifts1 = [6, 5, 5, 5, 5]
prepare_gifts(gifts1) # [5, 6]

gifts3 = []
prepare_gifts(gifts3) # []
```