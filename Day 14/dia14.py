def min_moves_to_stables(reindeer: list[int], stables: list[int]) -> int:
  movimientos = 0
  for reno in reindeer:
    movimientos_reno = [abs(establo - reno) for establo in stables]
    min_mov_reno = min(movimientos_reno)
    idx_min_mov = movimientos_reno.index(min_mov_reno)
    stables.pop(idx_min_mov)
    movimientos += min_mov_reno

  return movimientos


