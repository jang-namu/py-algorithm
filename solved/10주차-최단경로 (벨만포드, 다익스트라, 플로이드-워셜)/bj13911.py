# 13911 집 구하기
"""
    알고리즘문제해결능력 다익스트라 소방차 문제와 같다.
    해당 문제에서는 소방서가 맥도날드와 스타벅스 두 종류로 분리된다.
    즉, 다익스트라를 한 번은 모든 맥도날드를 시작 노드로, 한 번은 모든 스타벅스를 시작 노드로 적용한다.
    나온 거리 배열을 이용해 적절한 집을 찾는다.

    소방서 문제에 핵심은 다음과 같다.
    그래프 내에 몇몇 집에는 불이 났다. 몇몇 노드에는 소방서가 주어진다. 각 불난 집에 모두 소방차를 보내는 최소 시간의 합을 구해라.

    해설 : 각 불난 집은 어떤 소방서에서 소방차가 와도 상관없다. 그저 빨리 오기만하면 된다.
    즉, 모든 소방서 노드를 시작노드로 (우선순위 큐에 가중치가 0인 초기노드로 넣는다.) 다익스트라를 적용하면,
    모든 집 노드는 가장 가까운 소방서에서 떨어진 거리를 알 수 있다.

    이해가 잘 되지 않는다면 임의의 정점을 추가하고 각 소방서에 가중치가 0인 간선을 잇는다.
    그리고 임의의 정점에서 다익스트라를 시작해도 결과는 같다.

    이해 : 우선순위 큐에 가중치가 0으로 같은 여러 정점이 들어가도, 빼내는 순서와는 상관없이 결과는 동일하다. (음수간선이 없을경우)
            위 예제에서, 소방서를 제외한 다른 집 노드를 우선순위 큐에서 빼내려면, 이미 모든 소방서 노드는 우선순위큐에서 빠져있다.
            즉, 우선순위 큐에는 모든 소방서를 기준으로, 소방서와 연결된 집 중 가장 가까운 거리의 집 정보가 들어가있다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    adj[b].append((a, w))
m, x = map(int, input().split())
mcdonald = map(int, input().split())
s, y = map(int, input().split())
starbucks = map(int, input().split())


def dijkstra(start):
    pq = []
    distance = [1e10] * (V + 1)
    processed = [False] * (V + 1)
    for i in start:
        heappush(pq, (0, i))
        distance[i] = 0

    while pq:
        _, u = heappop(pq)
        """
        # processed 대신 좀 더 트리킨한 방법
        if distance[u] < dist:  # dist는 바로 윗라인에서 heappop()한 '_' 거리
                continue
        """
        if processed[u]:
            continue
        processed[u] = True
        for v, w in adj[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                heappush(pq, (distance[v], v))
    return distance


mc_path = dijkstra(mcdonald)
#print(mc_path)
sb_path = dijkstra(starbucks)
#print(sb_path)
ans = 1e10
for i, j in zip(mc_path, sb_path):
    if i == 0 or j == 0: continue
    if i > x or j > y:
        continue
    #print(i, j)
    ans = min(ans, i+j)
print(ans if ans < 1e10 else -1)