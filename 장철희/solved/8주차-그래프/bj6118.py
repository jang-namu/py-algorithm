# 6118 숨바꼭질
"""
    아이디어 : bfs 구현, distance 배열만들고 거리를 저장한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

distance = [0] * (N + 1)


def bfs(s):
    queue = deque()
    visited = [False] * (N+1)

    queue.append(s)
    visited[s] = True

    while len(queue):
        v = queue.popleft()
        for x in adj[v]:
            if visited[x]:
                continue
            visited[x] = True
            distance[x] = distance[v] + 1
            queue.append(x)


bfs(1)
print(distance.index(max(distance)), max(distance), distance.count(max(distance)))

