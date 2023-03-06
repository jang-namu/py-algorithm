# 2636 치즈
"""
    아이디어 : 거꾸로 풀기. 치즈가 놓인 칸 '1'이 아닌 바깥쪽 '0'을 탐색한다.
    바깥쪽 0과 맡붙어 있는 '1'을 찾아 이번 턴에 녹인다.
"""
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

board = list(list(map(int, input().split())) for _ in range(r))
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs():
    air = deque()
    air.append((0, 0))
    visited = [[False] * c for _ in range(r)]

    count = 0
    while air:
        y, x = air.popleft()
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                if board[ny][nx] == 0:
                    visited[ny][nx] = True
                    air.append((ny, nx))
                if board[ny][nx] == 1:
                    count += 1
                    visited[ny][nx] = True
                    board[ny][nx] = 0
    return count


def check():
    for row in board:
        if 1 in row:
            return False
    return True


time = 0
while True:
    time += 1
    last = bfs()

    if check():
        print(time)
        print(last)
        break

