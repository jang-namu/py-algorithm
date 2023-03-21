# 3187 양치기 꿍
# 3187과 같다.
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

yard = [[char for char in input().rstrip()] for _ in range(r)]
visited = [[False] * c for _ in range(r)]
sheep = 0
wolf = 0


def bfs(row, column):
    global wolf, sheep
    queue = deque()
    queue.append((row, column))
    visited[row][column] = True

    t_sheep = 0
    t_wolf = 0

    while queue:
        row, column = queue.popleft()
        if yard[row][column] == 'v':
            t_wolf += 1
        elif yard[row][column] == 'k':
            t_sheep += 1
        for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            nx = column + dx
            ny = row + dy
            if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx]:
                visited[ny][nx] = True
                if yard[ny][nx] == '#':
                    continue
                queue.append((ny, nx))

    if t_wolf >= t_sheep:
        wolf += t_wolf
    else:
        sheep += t_sheep



for i in range(r):
    for j in range(c):
        if not visited[i][j] and yard[i][j] != '#':
            bfs(i, j)

print(sheep, wolf)
