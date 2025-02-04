function prepareGifts(gifts: string[]): string[] {
    const uniqueGifts = Array.from(new Set(gifts));
    return uniqueGifts.sort();
}