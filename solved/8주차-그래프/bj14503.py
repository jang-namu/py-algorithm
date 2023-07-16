# 14503 로봇 청소기
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

Deltas = ((1,0),(0,1),(-1,0),(0,-1))
N, M = map(int,input().split())
r, c, d = map(int, input().split())
room = list(map(int, input().split()) for _ in range(N))
visited = [[0] * (M-2) for _ in range(N-2)]


def rotate(d):
    return (d+3) % 4

def bfs(r, c, d):
    pq = []
    heappush(pq, (r, c, d))
    visited[r-1][c-1] = 1

    while pq:
        r, c, d = heappop(pq)
        room[r][c] = 1
        for dy, dx in Deltas:
            ny = r + dy
            nx = c + dx
            if 0 < ny < N and 0 < nx < M and not visited[ny][nx]:
                d = rotate(d)
                Deltas[d][0]
