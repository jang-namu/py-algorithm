# 1753 최단경로
"""
    시작 노드로부터 다른 모든 노드로의 최단경로. 가중치는 음수가 아니다.
    => 즉, 다익스트라 알고리즘 사용.
"""
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):          # 간선 정보 저장
    u, v, w = map(int, input().split())
    adj[u].append((v, w))


def dijkstra(K):
    priority_queue = []     # 탐색하지 않은 노드 중 거리가 가장 짧은 노드를 얻기 위해 우선순위 큐 사용
    heappush(priority_queue, (0, K))
    distance = [1e10] * (V+1)   # 거리, 시작노드 제외 INF로 초기화
    distance[K] = 0
    processed = [False] * (V+1) # 탐색유무

    while priority_queue:
        _, now = heappop(priority_queue)
        if processed[now]: continue
        processed[now] = True
        for v, w in adj[now]:   # 탐색하고 있는 노드에서 출발하는 간선을 검사. 한 번 탐색한 노드에 대해서는 거리가 줄지않음.
            if distance[v] > distance[now] + w:
                distance[v] = distance[now] + w
                heappush(priority_queue, (distance[v], v))
    return [i if i != 1e10 else 'INF' for i in distance]


ans1 = dijkstra(K)

