from typing import List, Literal

def move_train(board: List[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
  suma_mov = {'U': (-1,0),'D': (1,0), 'R': (0,1),'L': (0,-1)}
  resultado = {'*': 'eat', 'o':'crash','·':'none'}

  m_i, m_j = suma_mov[mov]
  for i,linea in enumerate(board):
    if '@' in linea:
      nx,ny = i+m_i, linea.index('@')+m_j

  if not (0 <= nx < len(board) and 0 <= ny < len(board[0])):
    return 'crash'

  return resultado[board[nx][ny]]

