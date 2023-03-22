# 6593 상범 빌딩
import sys
from collections import deque
input = sys.stdin.readline

Deltas = [(1, 0, 0), (0, 1, 0),  (0, 0, 1),  (-1, 0, 0),  (0, -1, 0),  (0, 0, -1)]


def bfs():
    queue = deque()
    s_z, s_y, s_x = start
    queue.append(start)
    visited[s_z][s_y][s_x] = 1

    time = 0
    while queue:
        time += 1
        for _ in range(len(queue)):
            z, y, x = queue.popleft()
            for dz, dy, dx in Deltas:
                nz = z + dz
                ny = y + dy
                nx = x + dx
                if 0 <= nz < n and 0 <= ny < r and 0 <= nx < c and not visited[nz][ny][nx]:
                    if building[nz][ny][nx] == '#':
                        continue
                    if building[nz][ny][nx] == '.':
                        visited[nz][ny][nx] = 1
                        queue.append((nz, ny, nx))
                    else:
                        return time
    return -1


while True:
    n, r, c = map(int, input().split())
    if (n and r and c) == 0:
        break

    visited = [[[0] * c for _ in range(r)] for _ in range(n)]

    building = [[] for _ in range(n)]
    for i in range(n):
        for j in range(r):
            tmp = input().rstrip()
            building[i].append(tmp)
            for k, ele in enumerate(tmp):
                if ele == 'S':
                    start = (i, j, k)
                elif ele == 'E':
                    end = (i, j, k)
        input()

    ans = bfs()
    if ans == -1:
        print("Trapped!")
    else:
        print("Escaped in", ans, "minute(s).")


