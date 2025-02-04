function orginzeShoes(shoes: {type: string, size: number}[]): number[]{
    const result: number[] = [];
    const dictAux: Record<number, string> = {};

    for (const shoe of shoes){
        const {type, size} = shoe;

        if (!(size in dictAux)){ dictAux[size] = '';}

        const reversePar = type === 'I'? 'R' : 'I';

        if (dictAux[size].includes(reversePar)){
            dictAux[size] = dictAux[size].replace(reversePar,'')
            result.push(size)
        }
        else {dictAux[size] += type;}
    }

    return result
}