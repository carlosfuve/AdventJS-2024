function organizeInventory(inventory: {name: string, quantity:number, category:string}[]): Record<string, Record<string,number>> {
    const inventOrg: Record<string, Record<string,number>> = {};


    for (const invent of inventory){
        const {name, quantity, category } = invent;

        if (!inventOrg[category]){ inventOrg[category] = {};}

        inventOrg[category][name] = (inventOrg[category][name] || 0) + quantity;
    }

    return inventOrg;
}