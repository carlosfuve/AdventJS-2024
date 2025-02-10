

function robotIsBack(moves: string[]): boolean | number[]{
    const sumaMov:Record<string, number[]> = {
        'L': [-1,0],
        'R': [1,0],
        'U': [0,1],
        'D': [0,-1]
    }
    const movimientoHecho: Record<string,boolean> = {
        'L': false,'R': false, 'U': false,'D': false
    }
    const inverseMov: Record<string,string> = {
        'U':'D',
        'D':'U',
        'R':'L',
        'L':'R'
    }

    let iniX: number = 0, iniY: number = 0;
    let i: number = 0;
    const n: number = moves.length;

    while (i < n) {
        const mov = moves[i];

        if (mov in sumaMov){
            iniX += sumaMov[mov][0];
            iniY += sumaMov[mov][1];
            movimientoHecho[mov] = true;
        }
        else if (mov === '*'){
            const nextMov = moves[i+1];
            iniX += sumaMov[nextMov][0];
            iniY += sumaMov[nextMov][1];
            movimientoHecho[nextMov] = true;
        }
        else if (mov === '!'){
            const nextMov = inverseMov[moves[i+1]];
            iniX += sumaMov[nextMov][0];
            iniY += sumaMov[nextMov][1];
            movimientoHecho[nextMov] = true;
            i+=1;
        }
        else if (mov === '?'){
            const nextMov = moves[i+1];
            if (!movimientoHecho[nextMov]){
                iniX += sumaMov[nextMov][0];
                iniY += sumaMov[nextMov][1];
                movimientoHecho[nextMov] = true;
            }
            i+= 1;
        }
        i += 1;
    }



    return iniX === 0 && iniY === 0? true : [iniX, iniY];
}