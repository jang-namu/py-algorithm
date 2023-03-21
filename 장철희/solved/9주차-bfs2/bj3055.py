# 3055 탈출
"""
    아이디어 : 고슴도치는 물이 이동할 칸으로 갈 수 없다 => 물부터 이동시키고 고슴도치 이동
    한턴씩 지나갈 때마다, 물을 이동시키고 고슴도치가 갈 수 있는 칸을 queue에 저장한다.

"""
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

water = deque()
world = list()
for i in range(r):
    tmp = input().rstrip()
    for j in range(c):
        if tmp[j] == '*':
            water.append((i, j))
        if tmp[j] == 'S':
            row, column = i, j
    world.append(list(i for i in tmp))

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * c for _ in range(r)]


def bfs(row, column):
    queue = deque()
    queue.append((row, column))
    count = 0

    while queue:
        count += 1
        length = len(queue)
        len_water = len(water)

        for _ in range(len_water):
            i, j = water.popleft()
            move_water(i, j)

        for _ in range(length):
            row, column = queue.popleft()
            for dx, dy in move:
                nx = column + dx
                ny = row + dy
                if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx]:
                    if world[ny][nx] == 'D':
                        return count
                    elif world[ny][nx] == '.':
                        visited[ny][nx] = True
                        queue.append((ny, nx))

    return "KAKTUS"


def move_water(row, column):
    for dx, dy in move:
        nx = column + dx
        ny = row + dy
        if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx]:
            if world[ny][nx] == '.':
                visited[ny][nx] = True
                world[ny][nx] = '*'
                water.append((ny, nx))



print(bfs(row, column))