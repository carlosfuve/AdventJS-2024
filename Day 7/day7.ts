function fixPackages(packages:string): string {

    while (packages.includes('(')){
        const idxIni = packages.lastIndexOf('(');
        const idxFi  = packages.lastIndexOf(')', idxIni) + 1;

        const reversed_word = packages.slice(idxIni+1, idxFi).split('').reverse().join('');
        const word_parentesis = packages.slice(idxIni, idxFi);
        packages = packages.replace(word_parentesis,reversed_word);
    }

    return packages;
}