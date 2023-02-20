# 7569 토마토

"""
# 2차원 배열로 입력받아 처리, 위 아래는 n, -n으로 이동한다.

import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, h):
    global cnt_0
    while queue:
        si, sj = queue.popleft()
        for di, dj in ((n, 0), (-n, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):  # 움직임처리 n, -n에 주목 (2차원으로 받음)
            if (di == 1 and si%n == n-1) or (di == -1 and si%n == 0):
                continue
            ni, nj = si + di, sj + dj
            if 0 <= ni < n * h and 0 <= nj < m and tomato[ni][nj] == 0:
                tomato[ni][nj] = tomato[si][sj] + 1     # 익은 토마토를 날짜로 쓴다.
                cnt_0 -= 1
                queue.append((ni, nj))

    if cnt_0 == 0:
        return tomato[si][sj] - 1       # 익은 토마토는 1로 입력받아 1씩 증가시키며 날짜로도 쓴다.
    else:
        return -1

m, n, h = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n*h)]

cnt_0, queue = 0, deque()
for i in range(n*h):
    for j in range(m):
        if tomato[i][j] == 0:
            cnt_0 += 1
        elif tomato[i][j] == 1:
            queue.append((i, j))

print(bfs(n, h))
"""

"""
    아이디어 : 7576과 같다. 단지, 위 아래만 추가해주면 된다. 
                초기 익은 토마토는 deque에 저장하고 안 익은 토마토는 갯수를 세둔다.
                deque가 빌 때까지(더 이상 반복해도 변화가 없을 때) 반복하며 위 아래, 상하좌우를 익힌다.
                새로이 deque에 저장된 토마토를 빼서 반복하며, 토마토를 새로 익힐 떄마다 nomato를 1씩 감소시킨다.
                deque가 비게되면, nomato의 갯수에 따라 -1 또는 iteration의 횟수를 출력한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

move = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

M, N, H = map(int, input().split())
tomato = list(list(list(map(int, input().split())) for _ in range(N)) for _ in range(H))

jmt = deque()
nomato = 0  # 안 익은 토마토
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[h][r][c] == 0:
                nomato += 1
            elif tomato[h][r][c] == 1:
                jmt.append((h, r, c))

ans = -1
while jmt:
    length = len(jmt)
    for _ in range(length):
        h, r, c = jmt.popleft()
        for z, y, x in move:
            nh = h + z
            nr = r + y
            nc = c + x

            if nh < 0 or nh >= H or nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if tomato[nh][nr][nc] == 0:
                tomato[nh][nr][nc] = 1
                nomato -= 1
                jmt.append((nh, nr, nc))

    ans += 1

print(ans if nomato == 0 else -1)


