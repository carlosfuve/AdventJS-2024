def organize_shoes(shoes:list[dict]) -> list[int]:
  result = []
  dict_aux = {}
  for shoe in shoes:
    tipo, size = shoe['type'], shoe['size']
    dict_aux.setdefault(size,'')

    reverse_par = 'R' if tipo == 'I' else 'I'
    if reverse_par in dict_aux[size]:
      dict_aux[size] = dict_aux[size].replace(reverse_par, '')
      result.append(size)
    else:
      dict_aux[size] = dict_aux[size] + tipo
 
  return result