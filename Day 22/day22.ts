function generateGiftSets(gifts: string[]): string[][] {
    function generateAllCombinations(items: string[]): string[][] {
        if (items.length === 0) {
            return [[]];
        }
        
        const [first, ...rest] = items;
        const withoutFirst = generateAllCombinations(rest);
        const withFirst = withoutFirst.map(combination => [first, ...combination]);
        
        return [...withFirst, ...withoutFirst];
    }
    
    const result = generateAllCombinations(gifts);
    result.splice(result.findIndex(subset => subset.length === 0), 1);
    
    return result.sort((a, b) => a.length - b.length);
}