"""
    가로, 세로, 대각선으로 나올수 있는 8개의 빙고를 O, X인 경우를 각각 센다.
    if 빙고가 하나도 없으면 o == x+1 또는 o == x를 만족해야하고
    if x가 이기면 o == x를 만족.
    if o가 이기면 o == x+1을 만족해야 한다. (주의할 점은 마지막에 o를 두면서 빙고가 두개가 생기고 끝날 수 있다.)
"""


def solution(board):
    world = []
    for line in board:
        world += [ch for ch in line]
    print(world)

    x = world.count("X")
    o = world.count("O")

    if o != x and o != x + 1:
        return 0

    lineX = 0
    lineO = 0

    # 세로 방향으로 빙고
    for i in range(3):
        if world[i] == world[i + 3] and world[i] == world[i + 6]:
            if world[i] == "O":
                lineO += 1
            elif world[i] == "X":
                lineX += 1

    # 가로 방향 빙고
    for i in range(0, 7, 3):
        if world[i] == world[i + 1] and world[i] == world[i + 2]:
            if world[i] == "O":
                lineO += 1
            elif world[i] == "X":
                lineX += 1

    # 대각선 1
    if world[0] == world[4] and world[0] == world[8]:
        if world[0] == "O":
            lineO += 1
        elif world[0] == "X":
            lineX += 1
    # 대각선 2
    if world[2] == world[4] and world[2] == world[6]:
        if world[2] == "O":
            lineO += 1
        elif world[2] == "X":
            lineX += 1

    ## 마지막에 o를 두면서 두개의 빙고가 만들어질 수 있다.!!!
    if lineO >= 1 and lineX == 0:
        if o - x == 1:
            return 1
    elif lineO == 0 and lineX == 1:
        if o - x == 0:
            return 1
    elif lineO == 0 and lineX == 0:
        return 1
    return 0
