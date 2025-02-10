function findMissingNumbers(nums: number[]): number[] {
    if (nums.length === 0) return [];
    
    const maxNum = Math.max(...nums);
    return Array.from({ length: maxNum }, (_, i) => i + 1).filter(num => !nums.includes(num));
}