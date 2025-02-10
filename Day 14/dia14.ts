function minMovesToStables(reeinder: number[], stables: number[]): number{
    let movimientos:number = 0;
    for (const reno of reeinder){
        const movimientosReno = stables.map(establo => Math.abs(establo - reno));
        const minMovReno = Math.min(...movimientosReno);
        const idxMinMov = movimientosReno.indexOf(minMovReno);
        stables.splice(idxMinMov, 1);
        movimientos += minMovReno;
    }

    return movimientos;
}