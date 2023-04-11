# 5014 스타트링크
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
building = [0] * (F+1)


if S == G:
    print(0)
    exit(0)

def bfs():
    pq = []
    heappush(pq, S)
    building[S] = 1

    while pq:
        now = heappop(pq)
        for delta in (U, -D):
            next = now+delta
            if 1 <= next <= F and not building[next]:
                if next == G:
                    print(building[now])
                    return
                building[next] = building[now] + 1
                heappush(pq, next)
    print("use the stairs")
    return


bfs()