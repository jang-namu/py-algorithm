from collections import deque


def solution(board):
    move = ((1, 0), (0, 1), (-1, 0), (0, -1))

    # board를 재구성한 world를 만든다.
    world = [['D'] * (len(board[0]) + 2)]
    for b in board:
        world.append(['D'] + [i for i in b] + ['D'])
    world.append(['D'] * (len(board[0]) + 2))

    shortest = [[10e9] * len(world[0]) for _ in range(len(world))]

    goal = 0  # G
    robot = 0  # R
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == 'G':
                goal = (i, j)
            elif world[i][j] == 'R':
                robot = (i, j)
        print(world[i])

    que = deque()
    que.append(robot)
    shortest[robot[0]][robot[1]] = 0  # 로봇 시작지점 0으로 초기화
    while que:
        y, x = que.popleft()
        for dy, dx in move:
            ny = y
            nx = x
            while world[ny + dy][nx + dx] != 'D':  # 한번에 쭉간다.
                ny += dy
                nx += dx
            if world[ny][nx] == 'G':  # 쭉간곳이 골이면 바로리턴 => deque 사용 (큐로 사용) 하기 때문
                return shortest[y][x] + 1

            if shortest[ny][nx] == 10e9:  # 한 번도 안 간 곳 & 큐 사용 => 현재 루트가 [ny][nx] 까지의 최단경로!
                shortest[ny][nx] = shortest[y][x] + 1
                que.append((ny, nx))
            else:
                continue
    return -1

