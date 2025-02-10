def is_robot_back(moves: list[str]) -> bool | list[int]:
    suma_mov = {'L': (-1,0),'R': (1,0), 'U': (0,1),'D': (0,-1)}
    movimiento_hecho = {'L': False,'R': False, 'U': False,'D': False}
    inverse_mov = {'U':'D' ,'D':'U','R':'L','L':'R'}
    ini_x, ini_y = 0,0

    i = 0
    n = len(moves)
    while i < n:
        mov = moves[i]
        if mov in suma_mov:
            ini_x, ini_y = ini_x + suma_mov[mov][0], ini_y + suma_mov[mov][1]
            movimiento_hecho[mov] = True
        elif mov == '*':
            next_mov = moves[i+1]
            ini_x, ini_y = ini_x + suma_mov[next_mov][0], ini_y + suma_mov[next_mov][1]
            movimiento_hecho[next_mov] = True
        elif mov == '!':
            next_mov = inverse_mov[moves[i+1]]
            ini_x, ini_y = ini_x + suma_mov[next_mov][0], ini_y + suma_mov[next_mov][1]
            movimiento_hecho[next_mov] = True
            i+=1
        elif mov == '?':
            next_mov = moves[i+1]
            if not movimiento_hecho[next_mov]:
                ini_x, ini_y = ini_x + suma_mov[next_mov][0], ini_y + suma_mov[next_mov][1]  
                movimiento_hecho[next_mov] = True
            i+=1

        i+=1

    return True if ini_x == 0 and ini_y == 0 else [ini_x,ini_y]