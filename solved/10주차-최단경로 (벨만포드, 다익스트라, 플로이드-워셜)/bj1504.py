# 1504 특정한 최단 경로
"""
    "1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오."
    문제를 잘못 이해했다. 1->N->v1->v2->N 같은 경우는 없다.
    1부터 시작해서 N번 노드에 도착하기 전에 v1과 v2를 방문해야한다.
    즉, 1->v1->v2->N과 1->v2->v1->N 두가지 경우의 수 밖에 존재하지 않는다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, E = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))
v1, v2 = map(int, input().split())

def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance = [1e10] * (N+1)
    distance[start] = 0
    processed = [False] * (N+1)
    while pq:
        _, node, = heappop(pq)
        if processed[node]: continue
        processed[node] = True
        for v, w in adj[node]:
            if distance[v] > distance[node] + w:
                distance[v] = distance[node] + w
                heappush(pq, (distance[v], v))
    return distance

second = dijkstra(v1)
third = dijkstra(v2)

ans = min(second[1] + second[v2] + third[N], third[1] + third[v1] + second[N])

print(ans if ans < 1e10 else -1)