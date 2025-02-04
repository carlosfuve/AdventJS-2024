function createXmasTree(height: number, ornament: string): string {
    const longitudes = Array.from({length: height}, (_, n) => 2*n + 1);
    const ancho = longitudes[longitudes.length-1];

    let res = ""
    for (const long of longitudes){
        const nGuion = (ancho - long) / 2;
        const guiones = '-'.repeat(nGuion);
        const linea = guiones + ornament.repeat(long) + guiones;
        res += linea + "\n";
    }

    const nTronco = (ancho - 1) / 2;
    const tronco = '_'.repeat(nTronco);
    const lineaTronco = tronco + '#' + tronco

    res += lineaTronco + "\n";
    res += lineaTronco;
    return res
}