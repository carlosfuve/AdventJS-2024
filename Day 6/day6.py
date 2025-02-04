def in_box(box:list[str]) -> bool:
  if not (box[0].replace('#','') == '' and box[-1].replace('#','') == ''): 
    return False

  for line in box[1:-1]:
    if '*' in line[1:-1]:
      return True
    
  return False