function createFrame(names: string[]): string {
    const maxLen = Math.max(...names.map(name => name.length)) + 4;

    let res = '*'.repeat(maxLen) + "\n";
    for (const name of names){
        const paddedName = `* ${name}`;
        const spaces = ' '.repeat(maxLen - 1 - paddedName.length);
        res += paddedName + spaces + "\n";
    }

    res += '*'.repeat(maxLen);
    return res;
}