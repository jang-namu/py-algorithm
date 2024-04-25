"""조건: 오른쪽과 아래쪽으로만 움직여"""


def solution(m, n, puddles):
    move = [[0, -1], [-1, 0]]
    matrix = [[0] * (m + 1) for _ in range(n + 1)]
    matrix[1][1] = 1

    for x, y in puddles:
        matrix[y][x] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j] == -1: continue
            for dx, dy in move:
                if matrix[i + dx][j + dy] == -1: continue
                matrix[i][j] += matrix[i + dx][j + dy]
                matrix[i][j] %= 1000000007

    return matrix[-1][-1] % 1000000007
