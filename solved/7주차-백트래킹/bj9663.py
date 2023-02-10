# 9663 N-Queen
import sys
N = int(input())

board = [[1] * N for _ in range(N)]


def get_N_Queen(n=0):
    res = 0
    global board
    if n == N:
        res += 1
    for i in range(N):
        for j in range(N):
            board[i] = [0] * N
            for k in range(N):
                board[k][j] = 0

            get_N_Queen(n+1)
    return res