function execute(code: string): number {
    let resultado = 0;
    let i = 0;
    const n = code.length;
    const op: Record<string, number> = { '+': 1, '-': -1 };
    const brackets: Record<string, string> = { '[': ']', '{': '}' };

    while (i < n) {
        const car = code[i];

        if (op[car] !== undefined) {
            resultado += op[car];
        } else if (brackets[car]) {
            const idNext = code.slice(i).indexOf(brackets[car]);
            if (idNext === -1) break;
            
            if (resultado === 0) {
                i += idNext + 1;
                continue;
            }

            if (car === '[') {
                const evalCode = code.slice(i + 1, i + idNext);
                let iEval = 0;
                const nEval = idNext - 1;

                while (iEval < nEval) {
                    const carEval = evalCode[iEval];
                    if (op[carEval] !== undefined) {
                        resultado += op[carEval];
                    } else if (carEval === '{') {
                        const idxEvalNext = evalCode.slice(iEval).indexOf('}');
                        if (idxEvalNext === -1) break;
                        if (resultado === 0) {
                            iEval += idxEvalNext;
                        }
                    }
                    iEval += 1;
                }

                if (resultado === 0) {
                    i += nEval;
                } else {
                    i -= 1;
                }
            }
        }
        i += 1;
    }
    return resultado;
}
