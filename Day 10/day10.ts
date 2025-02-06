function compile(instructions:string[]): number | null{
    const registros:Record<string, number> = {};
    let i:number = 0;

    while (i < instructions.length){
        const instr = instructions[i].split(' ')
        const f = instr[0];
        const arg = instr.slice(1);

        if (f === 'MOV'){
            const x = arg[0];
            const y = arg[1];
            registros[y] = isNaN(Number(x)) ? registros[x] : Number(x);
        }
        else if (f === 'INC'){
            registros[arg[0]] = (registros[arg[0]] || 0) + 1
        }
        else if (f === 'DEC'){
            registros[arg[0]] = (registros[arg[0]] || 0) - 1
        }
        else if (f === 'JMP'){
            const x = arg[0];
            const y = arg[1];

            if ((registros[x] || 0) === 0){ 
                i = Number(y) - 1;
            }
        }

        i++;
    }

    return 'A' in registros ? registros['A'] : null;
}