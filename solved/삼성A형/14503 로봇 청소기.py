"""
이 문제는 dfs, bfs 같은 그래프 문제가 아님에 주의.
해당 문제는 시뮬레이션으로, 이전 상태가 중요하지 않다.
모든 입력에 대해 단 하나의 결과밖에 나오지 않는다.
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(25000)

moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N, M = map(int, input().split())
start_r, start_c, d = map(int, input().split())
room = list(list(map(int, input().split())) for _ in range(N))
result = 0


def around(r, c):
    for i, move in enumerate(moves):
        tr = r + move[0]
        tc = c + move[1]
        if room[tr][tc] == 0:
            return True
    return False


def back(r, c):
    direction = (2 + d) % 4
    return r + moves[direction][0], c + moves[direction][1]


def front(r, c):
    return r + moves[d][0], c + moves[d][1]


def turn():
    global d
    d = (3 + d) % 4


def dfs(r, c):
    global result
    if room[r][c] == 0:
        result += 1
        room[r][c] = -1

    if not around(r, c):
        tr, tc = back(r, c)
        if room[tr][tc] != 1:
            dfs(tr, tc)
    else:
        turn()
        tr, tc = front(r, c)
        while room[tr][tc] != 0:
            turn()
            tr, tc = front(r, c)
        dfs(tr, tc)


dfs(start_r, start_c)
print(result)
