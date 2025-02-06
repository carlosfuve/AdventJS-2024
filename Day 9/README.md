# Reto 9: 🚂 El tren mágico

Los elfos están jugando con un tren 🚂 mágico que transporta regalos. Este tren se mueve en un tablero representado por un array de strings.

El tren está compuesto por una locomotora (@), seguida de sus vagones (o), y debe recoger frutas mágicas (*) que le sirve de combustible. El movimiento del tren sigue las siguientes reglas:

Recibirás dos parámetros board y mov.

board es un array de strings que representa el tablero:
- @ es la locomotora del tren.
- o son los vagones del tren.
- * es una fruta mágica.
- · son espacios vacíos.

mov es un string que indica el próximo movimiento del tren desde la cabeza del tren @:
- 'L': izquierda
- 'R': derecha
- 'U': arriba
- 'D': abajo.

Con esta información, debes devolver una cadena de texto:
- 'crash': Si el tren choca contra los bordes del tablero o contra sí mismo.
- 'eat': Si el tren recoge una fruta mágica (*).
- 'none': Si avanza sin chocar ni recoger ninguna fruta mágica.

```python
board = [
  '·····',
  '*····',
  '@····',
  'o····',
  'o····'
]

move_train(board,'U') # eat
move_train(board,'D') # crash
move_train(board,'L') # crash
move_train(board,'R') # none
```