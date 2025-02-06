def compile(instructions:list[str]) -> int:
  registros = {}
  i = 0
  while i < len(instructions):
    inst = instructions[i].split()
    f, args = inst[0], inst[1:]

    if f == 'MOV':
        x,y = args[0], args[1]
        registros[y] =  registros[x] if x.isalpha() else int(x)

    elif f == 'INC':
        registros[args[0]] = registros.get(args[0],0) + 1
    
    elif f == 'DEC':
        registros[args[0]] = registros.get(args[0],0) - 1
    
    elif f == 'JMP':
        x,y = args[0], args[1]
        if registros.get(x,0) == 0:
            i = int(y) - 1

    i+=1

  return registros.get('A') if 'A' in registros else None