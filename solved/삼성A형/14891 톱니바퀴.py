"""
돌리기 전 상태에서 맞닿은 극이 같은지 확인한다.
현재 톱니바퀴에 회전으로 인한 좌우 톱니바퀴의 회전을 left_propagation, right_propagation으로 분리하여 생각한다.
좌전파와 우전파는 서로 독립적이므로 호출하는 순서는 상관없다.
"""

import sys
input = sys.stdin.readline

gears = list(list(map(int, list(ch for ch in input().strip()))) for _ in range(4))
K = int(input())


def turn(N, d):
    if d == 1:
        gears[N] = [gears[N][-1]] + gears[N][:-1]
    else:
        gears[N] = gears[N][1:] + [gears[N][0]]


def right_propagation(N, d):
    if N == 3:
        return
    if gears[N][2] == gears[N+1][6]:
        return
    right_propagation(N+1, -d)
    turn(N+1, -d)


def left_propagation(N, d):
    if N == 0:
        return
    if gears[N][6] == gears[N-1][2]:
        return
    left_propagation(N-1, -d)
    turn(N-1, -d)


for _ in range(K):
    gear, d = map(int, input().split())
    gear -= 1
    right_propagation(gear, d)
    left_propagation(gear, d)
    turn(gear, d)


print(sum(gear[0] * (2 ** i) for i, gear in enumerate(gears)))
