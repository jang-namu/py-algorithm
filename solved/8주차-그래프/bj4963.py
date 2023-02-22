# 4963 섬의 개수
"""
    간선이 아닌 move를 이용한 bfs 통해 컴포넌트의 갯수를 구한다.
"""
import sys
input = sys.stdin.readline

move = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ans = []

def bfs(row, column):
    queue = [(row, column)]
    while queue:
        row, column = queue.pop()
        for dx, dy in move:
            nx = column + dx
            ny = row + dy
            if 0 <= nx < w and 0 <= ny < h:
                if island[ny][nx]:
                    island[ny][nx] = 0
                    queue.append((ny, nx))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    ans.append(0)
    island = list(list(map(int, input().split())) for _ in range(h))
    for i in range(h):
        for j in range(w):
            if island[i][j]:
                bfs(i, j)
                ans[-1] += 1

print("\n".join(map(str, ans)))