# 1012 유기농 배추
"""
    아이디어 : 농장의 배추 배치와 move를 이용하여 상하좌우로 진행하며 bfs 기반 탐색
    0, 0 부터 m-1, n-1까지 for문을 돌며, 각각에 bfs를 실행한다. bfs로 탐색된 배추는 -1로 표시하고 다시 체크하지 않는다.
    bfs 함수 내부에서는 move를 이용해 상하좌우에 연결된 배추를 queue에 저장한다.
    배추가 인접한 부분(컴포넌트)에 대해 bfs 1회 실행 시, 인접한 배추 모두가 탐색된다.
"""
import sys
from collections import deque
input = sys.stdin.readline

move = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(row, column):
    queue = deque()

    queue.append((row, column))
    farm[row][column] = -1

    while len(queue):
        row, column = queue.popleft()

        for x, y in move:
            new_x = column + x
            new_y = row + y

            if farm[new_y][new_x] == 1:
                farm[new_y][new_x] = -1
                queue.append((new_y, new_x))


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    farm = list([0] * (M+2) for _ in range(N+2))
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y+1][x+1] = 1

    count = 0

    for row in range(1, N+1):
        for column in range(1, M+1):
            if farm[row][column] == 1:
                bfs(row, column)
                count += 1

    print(count)


"""
# 오답 코드
# 처음에는 단순 이중 for문을 이용하는 방법을 썼다.
# 이 방법의 문제점은 검사 방향이 정해져있다는 것이다.
# 즉, 같은 행의 뒤에 부분과 연결된 경우는 잡아내지 못 한다.
# ex) 
#       2 3
        0 0
        1 0
        1 1
        1 2
        0 2
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = list([-1] * (M+2) for _ in range(N+2))
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y+1][x+1] = 0

    count = 0
    for row in range(1, N+1):
        for column in range(1, M+1):
            if farm[row][column] == -1:
                continue
            for move_x, move_y in move:
                if farm[row + move_y][column + move_x] > 0:
                    farm[row][column] = 1
            if not farm[row][column]:
                count += 1
                farm[row][column] = 1

    print(count)
    """