def calculate_price(ornaments: str) -> int | None:
  item_to_int = {'*':1, 'o': 5, '^': 10, '#':50, '@':100}
  suma = 0
  n = len(ornaments) - 1
  i = 0
  while i < n:

    if not ornaments[i+1] in item_to_int:
        return None
    
    int_item = item_to_int[ornaments[i]]
    next_item = item_to_int[ornaments[i+1]]
    if next_item > int_item:
        suma -= int_item
    else:
        suma += int_item
    
    i += 1

  return suma + item_to_int[ornaments[n]]