# 2573 빙산
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
Deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))
snow = set()
ice = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(1, M-1):
        if row[j]:
            snow.add((i, j))
    ice.append(row)


def melt(snow):
    for y, x in snow:
        for dy, dx in Deltas:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if ice[ny][nx] == 0 and (ny, nx) not in snow:
                    if not ice[y][x]:
                        break
                    ice[y][x] -= 1



def bfs(y, x):
    pq = []
    heappush(pq, (y, x))
    while pq:
        y, x = heappop(pq)
        for dy, dx in Deltas:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if (ny, nx) in snow:
                    visited[ny][nx] = 1
                    heappush(pq, (ny, nx))


ans = 0
while snow:
    melt(snow)
    ans += 1
    visited = [[0] * M for _ in range(N)]

    for y, x in snow:
        if ice[y][x]:
            bfs(list(snow)[0][0], list(snow)[0][1])
            break

    new_snow = set()
    for i, j in snow:
        if not visited[i][j]:
            print(ans)
            exit(0)
        new_snow.add((i, j))

    snow = new_snow
print(0)