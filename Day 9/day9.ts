type Move = 'U' | 'D' | 'R' | 'L';
type Result = 'none' | 'crash' | 'eat';

function moveTrain(board: string[], mov: Move): Result {
    const sumaMov: Record<Move, [number, number]> = {
        'U': [-1, 0],
        'D': [1, 0],
        'R': [0, 1],
        'L': [0, -1]
    };

    const resultado: Record<string, Result> = {
        '*': 'eat',
        'o': 'crash',
        '·': 'none'
    };

    const [m_i, m_j] = sumaMov[mov];
    let nx: number = -1, ny: number = -1;

    for(let i = 0; i < board.length; i++){
        const linea = board[i];

        if (linea.includes('@')){
            nx = i + m_i;
            ny = linea.indexOf('@') + m_j;
        }
    }

    if (!(0 <= nx && nx < board.length && 0 <= ny && ny < board[0].length)) {
        return 'crash';
    }

    return resultado[board[nx][ny]]
}