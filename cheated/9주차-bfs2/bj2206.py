# 2206 벽 부수고 이동하기
"""
    오랜만에 솔루션을 보고 해결할 수 있던 문제다. 5시간 넘게 고민을 했지만 풀리지 않았다.
    처음에는 queue에만 세번째변수로 flag를 저장해 사용했다. 그 결과 벽을 뚫고간 경우와 그렇지 않은 경우의
    방문여부를 따로 관리해야 했고, 배열이 엄청나게 사용되야 했다.
    두번째는 재귀, dfs를 이용해 N, M 지점까지 경로를 먼저 찍었고, 이는 성공하는 듯 했지만 너무 많은 연산으로 인해 시간초과가
    났다.
    시간초과를 해결하기 위해 이 문제는 bfs를 이용해 N, M에 도달하는 즉시 return을 통해 함수를 종료해야했고, 동시에
    visited를 만들어 방문한 노드도 관리해야했다.

    3차원 배열을 이용하면 문제가 풀렸다. 벽을 뚫고 먼저간 경우와 뚫지 않은 경우를 따로 저장해야 했다.
    그렇게 할 경우 처음 flag 변수'만' 사용했을 떄와는 다르게, 뚫고 온 경우, 뚫고 오지 않은 경우 모두 최단거리를 유지할 수 있었다.

    마지막까지 잘못이해한 것이, 처음 접근법대로 풀어서
    5 5
    00000
    11101
    00001
    01111
    00010
    입력이 들어왔을 때, 서로 다른 경로마다 visited를 따로 관리하는 방법을 계속 찾았는데,
    사실 서로 다른 경로가 아닌, 벽을 뚫고 온 경우와 그렇지 않은 경우로 나누면 훨씬 더 간단하다.
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = list(list(input().rstrip()) for _ in range(N))   # 문자열 -> 리스트

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]   # 3차원 리스트, 벽을 뚫고 온 경우, 안 뚫고 온 경우
visited[0][0][0] = 1    # 벽을 안 뚫은 경우
# visited[0][0][1] = 1    # 벽을 뚫고온 경우


def bfs():
    queue = deque()
    queue.append((0, 0, False)) # 이전에 벽을 뚫었으면 True

    while queue:
        y, x, state = queue.popleft()
        if y == N - 1 and x == M - 1:   # 입력이 N = 1, M = 1일 경우 예외도 생각해야한다.
            return visited[y][x][state]
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx][state] == 0: # visited[][]['state']로 방문여부 확인
                if maze[ny][nx] == '1' and not state:   # 벽을 마주쳤는데 뚫을 기회가 있는 경우
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    queue.append((ny, nx, True))
                elif maze[ny][nx] == '0':   # 빈 공간의 경우 이전 state에서 현재 state로 + 1만큼 거리 증가
                    visited[ny][nx][state] = visited[y][x][state] + 1   # False = 0, True = 1
                    queue.append((ny, nx, state))
    return -1

print(bfs())


"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
maze = list(list(input().rstrip()) for _ in range(N))   # 문자열 -> 리스트

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]  #

visited = [[9999] * M for _ in range(N)]
visited[0][0] = 1
ans = 9999


def dfs(y, x, state):
    if y == N-1 and x == M-1:
        global ans
        ans = min(ans, visited[y][x])
    for dy, dx in delta:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 9999:
            visited[ny][nx] = visited[y][x] + 1
            if maze[ny][nx] == '1':
                if not state:
                    dfs(ny, nx, True)
            else:
                dfs(ny, nx, state)
            visited[ny][nx] = 9999


dfs(0, 0, False)
print(ans if ans != 9999 else -1)
"""

"""
5 5
00001
11101
00001
01111
00010
"""