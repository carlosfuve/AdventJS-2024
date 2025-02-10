function distributeWeight(weight: number): string {
    const boxRepresentations: Record<number, string[]> = {
        1: [" _ ", "|_|"] ,
        2: [" ___ ", "|___|"],
        5: [" _____ ", "|     |", "|_____|"],
        10: [" _________ ", "|         |", "|_________|"]
    };
    
    if (boxRepresentations[weight]) {
        return boxRepresentations[weight].join("\n");
    }

    let listaPesos: number[] = [];
    while (weight > 0) {
        const nextW = Object.keys(boxRepresentations).map(Number).filter(num => num <= weight).pop()!;
        listaPesos.push(nextW);
        weight -= nextW;
    }

    const revLista = listaPesos.reverse();
    const n = revLista.length - 1;
    let resultado = "";

    for (let i = 0; i < n; i++) {
        const num = revLista[i];
        const nNum = boxRepresentations[num][0].length;
        const nBase = boxRepresentations[revLista[i + 1]][0].length;
        const guiones = '_'.repeat(Math.max(0, (nBase - nNum - 1))) + "\n";
        
        if (i !== 0) {
            resultado += boxRepresentations[num].slice(1).join("\n") + guiones;
        } else {
            resultado += boxRepresentations[num].join("\n") + guiones;
        }
    }

    resultado += boxRepresentations[revLista[n]].slice(1).join("\n");
    return resultado;
}