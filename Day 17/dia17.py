def detect_bombs(grid: list[list[bool]]) -> list[list[int]]:
    n, m = len(grid), len(grid[0])
    suma_pos = [(1,0),(-1,0),(0,1),(0,-1), (-1,-1),(1,1),(-1,1),(1,-1)]

    result = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                for dx,dy in suma_pos:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < n and 0 <= ny < m:
                        result[nx][ny] += 1

    return result

print(
detect_bombs([
  [True, False, False],
  [False, True, False],
  [False, False, False]
])
)