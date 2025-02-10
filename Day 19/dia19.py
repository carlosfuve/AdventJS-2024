def distribute_weight(weight: int) -> str:
    boxRepresentations = {
        1: [" _ ", "|_|"],
        2: [" ___ ", "|___|"],
        5: [" _____ ", "|     |", "|_____|"],
        10: [" _________ ", "|         |", "|_________|"]
    }

    if weight in boxRepresentations:
        return '\n'.join(boxRepresentations[weight])
        
    lista_pesos = []
    while weight > 0:
        next_w = [num for num in boxRepresentations if num <= weight][-1]
        lista_pesos += [next_w]
        weight -= next_w

    rev_lista = lista_pesos[::-1]
    n = len(rev_lista)-1
    resultado = ""
    
    for i in range(n):
        num = rev_lista[i]
        n_num = len(boxRepresentations[num][0])
        n_base = len(boxRepresentations[rev_lista[i+1]][0])
        guiones = '_' * max(0, (n_base - n_num - 1)) + '\n'
        
        if i != 0:
            resultado += '\n'.join(boxRepresentations[num][1:]) + guiones
        else:
            resultado += '\n'.join(boxRepresentations[num]) + guiones
    
    resultado += '\n'.join(boxRepresentations[rev_lista[n]][1:])
    return resultado




print(distribute_weight(1))


print(distribute_weight(2))


print(distribute_weight(18))




