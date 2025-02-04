function drawRace(indices: number[], length: number): string{
    const n = indices.length;
    const resultado: string[] = [];

    for (let i = 0; i < n; i++){
        const idx = indices[i]
        let carril = '~'.repeat(length)

        if (idx > 0) {carril = '~'.repeat(idx) + 'r' + '~'.repeat(length-idx-1);}
        else if (idx < 0) {
            const idxN = length+idx;
            carril = '~'.repeat(idxN) + 'r' + '~'.repeat(-idx-1);
        }

        const fiCarr = ' /' + (i+1).toString();
        resultado.push(' '.repeat(n - i+1) + carril + fiCarr);
    }


    return resultado.join("\n");
}