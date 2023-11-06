# 택배 배송
"""
최단 경로 문제. 간선의 가중치의 음수가 없다 -> 다익스트라
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]

for _ in range(M):
    dest, src, w = map(int, input().split())
    matrix[dest].append((w, src))
    matrix[src].append((w, dest))

MAX = 10e9


def dijkstra():
    heap = []
    heappush(heap, (0, 1))

    min_distance = [MAX] * (N + 1)
    min_distance[1] = 0
    visited = [False for _ in range(N+1)]

    while heap:
        _, src = heappop(heap)
        visited[src] = True
        for w, dest in matrix[src]:
            if visited[dest]:
                continue
            if min_distance[src] + w < min_distance[dest]:
                min_distance[dest] = min_distance[src] + w
                heappush(heap, (min_distance[dest], dest))
    return min_distance


min_distance = dijkstra()
print(min_distance[-1])
