# 2638 치즈
"""
    리팩토링.
    visited 와 queue를 함수 외부로 빼서 초기화.
    함수 내부에서 new_queue를 만들고 이번 턴에 녹은 치즈를 추가한다.
    new_queue는 다음 iter에서 queue로써 재사용된다. (이번 턴에 녹은 치즈가 다음턴에 다른 치즈를 녹임)
    종료조건에 대해. -> 처음 치즈의 갯수를 세서. 하나 녹을 때마다 1씩 감소한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

Deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
cheese = list(list(map(int, input().split())) for _ in range(N))
count = sum(map(sum, cheese))       # 초기 총 치즈 수
queue = deque()
queue.append((0, 0))
visited = [[0] * M for _ in range(N)]


def bfs():
    global count
    new_queue = deque() # 이번 턴에 녹은 치즈 = 다음 턴에 사용될 queue
    while queue:
        y, x = queue.popleft()
        for dy, dx in Deltas:
            if 0 <= (ny := y + dy) < N and 0 <= (nx := x + dx) < M and visited[ny][nx] < 2:
                if cheese[ny][nx]:
                    if visited[ny][nx]:
                        visited[ny][nx] = 2
                        cheese[ny][nx] = 0
                        count -= 1
                        new_queue.append((ny, nx))
                        continue
                    visited[ny][nx] += 1
                else:
                    visited[ny][nx] = 2
                    queue.append((ny, nx))
    return new_queue


time = 0
while count:
    time += 1
    queue = bfs()

print(time)




"""
    요약 : bfs를 돌며, 0인 칸은 한번만(visited를 2로 초기화) 1인 칸을 만나면 visited를 증가
    한 번의 루프에서 치즈가 있는 칸에 visited가 2회 쌓이면 이번 턴에 녹는다.
"""
"""
import sys
from collections import deque
input = sys.stdin.readline

Deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
cheese = list(list(map(int, input().split())) for _ in range(N))


def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * M for _ in range(N)]
    while queue:
        y, x = queue.popleft()
        for dy, dx in Deltas:
            if 0 <= (ny := y + dy) < N and 0 <= (nx := x + dx) < M and visited[ny][nx] < 2:
                if cheese[ny][nx]:
                    if visited[ny][nx]:
                        visited[ny][nx] = 2
                        cheese[ny][nx] = 0
                        continue
                    visited[ny][nx] += 1
                else:
                    visited[ny][nx] = 2
                    queue.append((ny, nx))


def is_finished():
    for row in cheese:
        if 1 in row:
            return False
    return True


time = 0
while not is_finished():
    time += 1
    bfs()

print(time)
"""