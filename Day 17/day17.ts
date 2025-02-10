function detectBombs(grid: boolean[][]): number[][] {
    const n:number = grid.length, m:number = grid[0].length;
    const sumaPos = [
        [1, 0], [-1, 0], [0, 1], [0, -1],
        [-1, -1], [1, 1], [-1, 1], [1, -1]
    ];
    const result: number[][] = Array.from({length:n}, () => Array(m).fill(0));
    for (let i = 0; i < n; i++){
        for (let j = 0; j < m; j++){
            if (grid[i][j]){
                for (const [dx, dy] of sumaPos){
                    const nx = i+dx;
                    const ny = j+dy;
                    if (nx >= 0 && nx < n && ny >= 0 && ny < m){
                        result[nx][ny] += 1;
                    }
                }
            }
        }
    }

    return result
}