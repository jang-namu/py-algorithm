# 4179 불!
from collections import deque
n, m = map(int, input().split())
miro = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]

q = deque()     # 불과 지훈이를 같은 큐에 저장한다.
for i in range(n):
    for j in range(m):
        if miro[i][j] == 'J':
            q.append((i, j, 'J'))
            visited[i][j] = 1
        elif miro[i][j] == 'F':
            q.appendleft((i, j, 'F'))       # 불을 먼저 움직이기 위해, 'left'로 추가한다
            visited[i][j] = 1

while q:
    x, y, state = q.popleft()
    if state == 'J' and (x == n-1 or x == 0 or y == m-1 or y == 0): # 탈출
        print(visited[x][y])
        break
    for i in range(4):  # 불과 지훈이를 이동한다.
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and miro[nx][ny] != '#':
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny, state))       # state를 이용해 불은 불대로, 지훈이는 지훈이대로 이동시킬 수 있다.
else: print("IMPOSSIBLE")

"""
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))
maze = list(list(input().rstrip()) for _ in range(r))


def solve():
    fire = list()
    jihoon = list()
    for i, row in enumerate(maze):
        for j, elem in enumerate(row):
            if elem == 'F':
                fire.append((i, j))
            elif elem == 'J':
                jihoon.append((i, j))


    count = 0
    while jihoon:
        count += 1

        next_fire = list()
        for y, x in fire:
            for dy, dx in DELTAS:
                ny = y + dy
                nx = x + dx
                if 0 <= nx < c and 0 <= ny < r and maze[ny][nx] == '.':
                    maze[ny][nx] = 'F'
                    next_fire.append((ny, nx))
        fire = next_fire

        next_jihoon = list()
        for y, x in jihoon:
            for dy, dx in DELTAS:
                ny = y + dy
                nx = x + dx
                if 0 <= nx < c and 0 <= ny < r:
                    if maze[ny][nx] == '.':
                        maze[ny][nx] = 'J'      # visited를 만들어 따로 관리하지 않고, maze에서 상태를 바꾼다.
                        next_jihoon.append((ny, nx))
                else:
                    return count
        jihoon = next_jihoon

    return "IMPOSSIBLE"


print(solve())
"""



