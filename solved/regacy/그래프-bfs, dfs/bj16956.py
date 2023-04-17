# 16956 늑대와 양
"""
    이 문제는, 울타리의 최소 개수를 구하는 문제가 아니다.
    => 양을 늑대로부터 격리, 울타리로 감싼다.
"""
import sys
input = sys.stdin.readline

Deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))
r, c = map(int, input().split())

farm = []
sheep = []
for i in range(r):
    row = [ch for ch in input().rstrip()]
    for j, ch in enumerate(row):
        if ch == 'S':
            sheep.append((i, j))
    farm.append(row)


def bfs():
    for i, j in sheep:
        for dy, dx in Deltas:
            if 0 <= (ny := i + dy) < r and 0 <= (nx := j + dx) < c:
                if farm[ny][nx] == 'W':
                    return False
                if farm[ny][nx] != 'S':
                    farm[ny][nx] = 'D'

    return True


if bfs():
    print(1)
    for i in range(r):
        print(''.join(farm[i]))
else:
    print(0)