# 1865 웜홀
"""
    이 문제는 언뜻보면 모든 노드간의 거리를 구하는 플로이드-워셜을 사용해야 할 것만 같다.
    하지만 플로이드-워셜은 입력과 테스트 케이스의 크기 때문에 시간초과가 된다.
    실상은 그래프 내에 음수 사이클이 존재하는지만 판단하면 되는 문제이기 때문에
    벨만-포드 알고리즘을 사용하는 것이 적절하다.
    11657번과는 다르게 그래프 내 어디든 간에 음수 사이클이 존재하는지 확인해야하기 때문에
    'distance[u] != INF' 조건을 지워야 한다.
"""
import sys
input = sys.stdin.readline
TC = int(input())

for r in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((u,v,w))
        edges.append((v,u,w))
    for _ in range(W):
        u, v, w = map(int, input().split())
        edges.append((u,v,-w))

    distance = [1e11] * (N+1)
    distance[1] = 0

    for i in range(N-1):
        updated = False
        for edge in edges:
            u, v, w = edge
            if distance[v] > distance[u] + w: # and distance[u] != 1e11: 여기는 왜 지워야 할까?
                distance[v] = distance[u] + w
                updated = True
        if not updated:
            break

    is_min_cycle = False
    for edge in edges:
        u, v, w = edge
        if distance[v] > distance[u] + w: # and distance[u] != 1e11: 음수사이클이 그래프내에 존재하기만 하면 된다.
            is_min_cycle = True
            break

    if is_min_cycle:
        print("YES")
    else:
        print("NO")




"""
import sys
input = sys.stdin.readline
TC = int(input())


def floyd_warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if road[i][j] > road[i][k] + road[k][j]:
                    road[i][j] = road[i][k] + road[k][j]


for r in range(TC):
    N, M, W = map(int, input().split())
    road = [[1e10] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        if road[u][v] > w:
            road[u][v] = w
        if road[v][u] > w:
            road[v][u] = w
    for _ in range(W):
        u, v, w = map(int, input().split())
        if road[u][v] > -w:
            road[u][v] = -w
    for i in range(1, N+1):
        road[i][i] = 0

    bellman_ford()
    res = 'NO'
    for i in range(1, N+1):
        if road[i][i] != 0:
            res = 'YES'
    print(res)
"""