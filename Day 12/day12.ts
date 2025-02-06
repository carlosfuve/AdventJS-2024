function calculatePrice(ornaments: string): number | null{
    const itemInt: Record<string,number> = {
        '*':1, 
        'o': 5, 
        '^': 10, 
        '#':50, 
        '@':100
    }

    let suma:number = 0;
    const n:number = ornaments.length - 1;
    let i:number = 0

    while (i < n){
        if (!(ornaments[i+1] in itemInt)){
            return null
        }

        const intItem = itemInt[ornaments[i]];
        const nextItem = itemInt[ornaments[i+1]];

        if (nextItem > intItem){ suma -= intItem;}
        else suma += intItem;

        i++;
    }


    return suma + itemInt[ornaments[n]];
}