# 13141
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
dist = [[0] * (N+1) for _ in range(N+1)]
sentence = sys.stdin.readlines()
for line in sentence:
    a, b, w = map(int, line.split())
    adj[a].append((b, w))
    adj[b].append((a, w))
    dist[a][b] = max(dist[a][b], w)
    dist[b][a] = max(dist[b][a], w)


def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance = [1e11] * (N+1)
    distance[start] = 0
    processed = [False] * (N+1)
    while pq:
        w, node = heappop(pq)
        if processed[node]:
            continue
        processed[node] = True
        for dest, weight in adj[node]:
            if distance[dest] > distance[node] + weight:
                distance[dest] = distance[node] + weight
                heappush(pq, (distance[dest], dest))
    return distance


def long_dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance = [1e11] * (N+1)
    distance[start] = 0
    processed = [False] * (N+1)

    while pq:
        w, node = heappop(pq)
        if processed[node]:
            continue
        processed[node] = True
        for dest, weight in enumerate(dist[node]):
            if weight == 0:
                continue
            if distance[dest] > distance[node] + weight:
                distance[dest] = distance[node] + weight
                heappush(pq, (distance[dest], dest))
    return distance


time = 1e10
for i in range(1, N+1):
    short_path = dijkstra(i)
    long_path = long_dijkstra(i)
    print(short_path)
    print(long_path)
    #time = min(time, max((j-i)/2 + i for i, j in zip(short_path, long_path)))
print(time)


"""
import copy
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dist = [[[] for _ in range(N+1)]  for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    dist[u][v].append(w)
    if v != u:
        dist[v][u].append(w)    # 자기자신 한테 가는 경로가 두번 추가되 것 방지


def iter_ond_second(dist, start, M):
    time = 0
    node_set = set()
    node_set.add(start)
    float_time = []
    while M:
        float_time = []
        new_set = {*node_set}
        for node in node_set:
            for i in range(len(dist[node])):


def check(dist):
    return sum(sum(sum(dist[i][j]) for j in range(1, N+1)) for i in range(1, N+1))

ans = 1e10
for i in range(1, N+1):
    ans = min(ans, iter_ond_second(copy.deepcopy(dist), i ,M))
print('%.1f' %ans)
"""