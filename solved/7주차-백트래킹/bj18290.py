# 18290 NM과 K (1)
"""
    아이디어 : 보드와 같은 크기의 check 리스트를 만들어, 갈 수 있는 칸인지 체크한다.
                인덱스와 체크를 간편하게 하기위해 보드와 체크는 N+2, M+2 크기로
                보드에 상하좌우에는 0을 추가했다.
                ex            0 0 0 0
                   1 2   ->   0 1 2 0
                   3 4        0 3 4 0
                              0 0 0 0
                이로써, 체크할 때 인덱스를 벗어나지 않는지 비교할 필요가 없어졌다.

        처음에는 check를 정수가 아닌, bool 자료형, False와 True를 통해 나타내려고 했고,
        그 결과 재귀호출이 끝난 후, True로 해줬던 것들을 다시 False로 바꾸는 과정에서,
        이전 iteration에서 막힌 칸들이 다시 False로 바뀌어 버리는 문제가 있었다.

        이 문제를 해결하기 위해 정수 0으로 시작해, +1, -1로 조작을해서 중복되서 체크되는 칸들도
        문제없도록 했다.

        속도 향상을 위해, 백트래킹에 가장 중요한 부분인 중간 탐색 종료는
        백준에서 확인한 방법을 이용했고, 간단하게
        res > 얻은 점수 + (전체 칸 - 선택한 칸) * 1만(최대 점수)를 통해 처리했다.
"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0] * (M+2)]
for _ in range(N):
    board.append([0] + list(map(int, input().split())) + [0])
board.append([0] * (M+2))

check = [[0] * (M+2)]
for _ in range(N):
    check.append([0]+[0] * M + [0])
check.append([0] * (M+2))

res = -10e9


def get_point_on_board(point=0, choose=0):
    if choose == K:
        global res
        if point > res:
            res = point
        return

    if res > point + (K - choose) * 10000:
        return

    for i in range(1, N+1):
        for j in range(1, M+1):
            if check[i][j]:
                continue
            check[i][j] += 1
            check[i - 1][j] += 1
            check[i + 1][j] += 1
            check[i][j - 1] += 1
            check[i][j + 1] += 1
            get_point_on_board(point + board[i][j], choose+1)
            check[i][j] -= 1
            check[i - 1][j] -= 1
            check[i + 1][j] -= 1
            check[i][j - 1] -= 1
            check[i][j + 1] -= 1


get_point_on_board()
print(res)



"""
import sys

n, m, k = map(int, sys.stdin.readline().split())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visited = [[0] * n for _ in range(m)]

max_num = -10e9


def solution(depth, result, pre):
    global max_num
    if depth == k:
        max_num = max(max_num, result)
        return

    if max_num >= result + 10000 * (k - depth):
        return

    for i in range(pre, m * n):
        row = i // m  # 행과 열의 다른 표현.
        col = i % m
        if visited[row][col]:
            continue

        flag = True
        for x, y in move:
            if 0 <= (x + row) < n and 0 <= (y + col) < m:
                if visited[x + row][y + col] == 1:
                    flag = False
                    break

        if flag:
            visited[row][col] = 1
            solution(depth + 1, result + nums[row][col], i + 1)
            visited[row][col] = 0


solution(0, 0, 0)
print(max_num)
"""