def fix_gift_list(received: list[str], expected: list[str]) -> dict[str, int]:
    res_miss = {}
    res_ext = {}

    agrupar_reg_recividos = {reg: received.count(reg) for reg in received}
    agrupar_reg_esperados = {reg_e: expected.count(reg_e) for reg_e in expected}
    
    for regalo, n_reg in agrupar_reg_recividos.items():
        n_hay = expected.count(regalo)
        resta = n_reg - n_hay
        if resta > 0:
            res_ext[regalo] = resta
        
        if resta >= 0:
            del agrupar_reg_esperados[regalo]
        else:
            agrupar_reg_esperados[regalo] = abs(resta)


    for regalo_e, n_reg_e in agrupar_reg_esperados.items():
        res_miss[regalo_e] = n_reg_e


    return {
        "missing": res_miss,
        "extra": res_ext
    }







  


#print(fix_gift_list(['bear', 'bear', 'car'], ['bear', 'bear', 'car']))
#print(fix_gift_list(['bear', 'car'], ['bear', 'bear', 'car']))
print(fix_gift_list(['bear','bear','bear', 'car'], ['bear', 'bear', 'car']))


#  missing: { ball: 1 },
#  extra: { car: 1 }