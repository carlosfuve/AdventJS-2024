def draw_race(indices: list[int], length: int) -> str:
    n = len(indices)
    resultado = []

    for i, idx in enumerate(indices):
        carril = '~' * length

        if idx > 0:
            carril = '~'*idx + 'r' + '~'*(length-idx-1)
        elif idx < 0:
            idx_n = length + idx
            carril = '~'*idx_n + 'r' + '~'*(-idx-1)

        fi_carr = ' /' + str(i+1)
        resultado.append(' '*(n - i+1) + carril + fi_carr)

    return '\n'.join(resultado)