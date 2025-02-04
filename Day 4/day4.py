def create_xmas_tree(height: int, ornament: str) -> str:
  longitudes  = [2*n+1 for n in range(height)]
  ancho = longitudes[-1]
  res = ""
  for lon in longitudes:
    n_guion = (ancho - lon) // 2
    guiones = '_'*n_guion
    linea = guiones + ornament*lon + guiones
    res = res + linea + "\n"

  n_tronco = (ancho - 1) // 2
  tronco = '_'*n_tronco 
  linea_tronco = tronco + '#' + tronco

  res += linea_tronco + "\n"
  res += linea_tronco 
  return res 