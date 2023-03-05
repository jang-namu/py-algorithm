# 5427 불
# 백준 풀이
import io, os, sys


def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    for _ in range(int(input())):
        cols, rows = map(int, input().split())
        board = [list(input().rstrip()) for _ in range(rows)]
        answer = problem(rows, cols, board)
        if answer == -1:
            print("IMPOSSIBLE")
        else:
            print(answer)


def problem(rows, cols, board):
    VOID, WALL, REACH, FIRE = 46, 35, 64, 42
    DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    fires = []
    reaches = []
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            if elem == FIRE:
                fires.append((i, j))
            if elem == REACH:
                reaches.append((i, j))

    time = 0
    while True:
        time += 1

        next_fires = []
        for y, x in fires:
            for dy, dx in DELTAS:
                if 0 <= (ny := y + dy) < rows and 0 <= (nx := x + dx) < cols and board[ny][nx] == VOID:
                    next_fires.append((ny, nx))
                    board[ny][nx] = FIRE
        fires = next_fires

        next_reaches = []
        for y, x in reaches:
            for dy, dx in DELTAS:
                if 0 <= (ny := y + dy) < rows and 0 <= (nx := x + dx) < cols:
                    if board[ny][nx] == VOID:
                        next_reaches.append((ny, nx))
                        board[ny][nx] = REACH
                else:               # 보드를 벗어나면 탈출!!
                    return time
        reaches = next_reaches

        if not reaches:
            return -1


if __name__ == "__main__":
    sys.exit(main())



"""
    아이디어 : 3055-탈출 문제와 비슷하게 불이 먼저 번지고 이동한다.
    탈출조건이 조금 까다로운데, 네 모퉁이를 제외하고 가장자리에 '.'이 있으면 탈출구다.
    즉, row가 0 또는 h-1이거나 column이 0 또는 w-1인 경우 탈출구이다.
    count는 탈출구를 빠져나가는 것까지 세는 것을 원칙으로 한다.
    visited를 관리해야 시간, 메모리 초과가 발생하지 않는다.
"""
"""
import sys
from collections import deque
input = sys.stdin.readline


def turn():
    while sangeun:
        length_fire = len(fire)
        for _ in range(length_fire):
            row, column = fire.popleft()
            for dy, dx in move:
                ny = row + dy
                nx = column + dx
                if 0 <= nx < w and 0 <= ny < h:
                    if building[ny][nx] == '.' or building[ny][nx] == '@':
                        building[ny][nx] = '*'
                        fire.append((ny, nx))

        length_sangeun = len(sangeun)
        for _ in range(length_sangeun):
            row, column = sangeun.popleft()
            if is_success(row, column):         # (1, 1)과 같은 특수한 경우에 유의, 아래 for문에서 ny, nx로 검사하면 안 된다.
                return visited[row][column] + 1
            for dy, dx in move:
                ny = row + dy
                nx = column + dx
                if 0 <= nx < w and 0 <= ny < h:
                    if not visited[ny][nx] and building[ny][nx] == '.':
                        visited[ny][nx] = visited[row][column] + 1
                        sangeun.append((ny, nx))
    return "IMPOSSIBLE"


def is_success(row, column):
    if row in [0, h-1] or column in [0, w-1]:
        return True
    return False


T = int(input())
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


for _ in range(T):
    w, h = map(int, input().split())

    building = list()
    fire = deque()
    sangeun = deque()
    visited = [[0] * w for _ in range(h)]

    for i in range(h):
        line = input().rstrip()
        for j in range(w):
            if line[j] == '*':
                fire.append((i, j))
            elif line[j] == '@':
                sangeun.append((i, j))
        building.append(list(s for s in line))

    print(turn())
"""