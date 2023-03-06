# 14442 벽 부수고 이동하기 2
"""
    공간 지역성과, java에서는 헤더의 수로 인해, 다차원 배열 선언에 따른 메모리 사용량에 대해 알게해준 문제
    arr[1000][1000][2] 보다 arr[2][1000][1000]이 더 메모리 사용이 적고 그만큼 빠르다.

    이 문제의 복병은 예상했던 대로 visited를 통해 방문횟수를 줄여주는 것.
    처음에는  "if 0 <= (ny := y + dy) < N and 0 <= (nx := x + dx) < M 와 같이 visited[count][ny][nx] == 0: 만을 검사했지만,
    생각해보면 visited[count][ny][nx] == 0과 visited[count + 1][ny][nx] == 0는 별개의 상황이기 때문에
    벽을 뚫고 갈 때에는 visited[count + 1][ny][nx] == 0를 검사해야한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

Deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M, K = map(int, input().split())
maze = list(list(input().rstrip()) for _ in range(N))
visited = [[[0] * M for _ in range(N)] for _ in range(K+1)] # 공간 지역성에 따라 arr[10][2] 보다 arr[2][10]이 메모리를 덜 사용한다.
visited[0][0][0] = 1    # 큰 숫자가 뒤로

if N == M == 1:
    print(1)
    exit(0)

def bfs():
    queue = deque()
    queue.append((0, 0, 0))     # y, x, count(벽뚤은 횟수)

    while queue:
        y, x, count = queue.popleft()
        for dy, dx in Deltas:
            if 0 <= (ny := y + dy) < N and 0 <= (nx := x + dx) < M:
                if ny == N - 1 and nx == M - 1:
                    return visited[count][y][x] + 1
                if maze[ny][nx] == '1' and count < K and visited[count + 1][ny][nx] == 0:   # 벽을 만났는데 부술수 있을 때
                    visited[count + 1][ny][nx] = visited[count][y][x] + 1
                    queue.append((ny, nx, count + 1))
                elif maze[ny][nx] == '0' and visited[count][ny][nx] == 0:   # 벽이 아닌 경우
                    visited[count][ny][nx] = visited[count][y][x] + 1
                    queue.append((ny, nx, count))
    return -1


print(bfs())