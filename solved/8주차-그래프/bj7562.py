# 7562 나이트의 이동
"""
    아이디어 : 나이트의 이동을 move로 표현, chess 보드판을 만들고 목적지 -1, 시작 0 으로 초기화
                현재 갈 수 있는 칸들을 deque에 저장하고, 원소를 빼서 거기서 갈 수 있는 칸 저장. => 반복
                chess 에는 해당 좌표에 도달하기 위해 몇번 움직였는지를 저장한다.
                목적지에 도달하면 종료
"""
import sys
from collections import deque
input = sys.stdin.readline

move = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

T = int(input())
for _ in range(T):
    l = int(input())
    x, y = map(int, input().split())
    ob_x, ob_y = map(int, input().split())

    chess = [[-999] * l for _ in range(l)]
    night = deque()
    chess[y][x] = 0
    chess[ob_y][ob_x] = -1
    night.append((y, x))

    if chess[y][x] == -1:
        print(0)
        continue
    sign = False
    while night:
        y, x = night.popleft()
        for my, mx in move:
            ny = y + my
            nx = x + mx
            if 0 <= nx < l and 0 <= ny < l:
                if chess[ny][nx] == -1:
                    sign = True
                    break
                if chess[ny][nx] == -999:
                    chess[ny][nx] = chess[y][x] + 1
                    night.append((ny, nx))
        if sign:
            break

    print(chess[y][x] + 1)