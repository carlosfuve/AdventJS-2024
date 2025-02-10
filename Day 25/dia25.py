def execute(code: str) -> int:
    resultado = 0
    i = 0
    n = len(code)
    op = {'+': 1, '-': -1}
    brackets = {'[':']','{':'}'}

    while i < n:
        car = code[i]

        if car in op:
            resultado += op[car]
        elif car in brackets:
            id_next = code[i:].index(brackets[car])
            if resultado == 0:
                i += id_next+1
                continue
            
            if car == '[':
                eval_code = code[i+1:i+id_next]
                i_eval = 0
                n_eval = id_next-1

                while i_eval < n_eval:
                    car_eval = eval_code[i_eval]
                    if car_eval in op:
                        resultado += op[car_eval]
                    elif car_eval == '{':
                        idx_eval_next = eval_code[i_eval:].index('}')
                        if resultado == 0:
                            i_eval += idx_eval_next
                    i_eval += 1

                
                if resultado == 0:
                    i += n_eval
                else:
                    i -= 1

        
        i+=1

    return resultado


print(execute('+++')) #3
print(execute('+--')) #-1
print(execute('>+++[-]')) #0
print(execute('>>>+{++}')) #3
print(execute('+{[-]+}+')) #2
print(execute('{+}{+}{+}')) #0
print(execute('-----[+]++')) #2
print(execute('-[++{-}]+{++++}')) #5