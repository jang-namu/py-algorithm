# 1005 ACM Craft
"""
    위상정렬을 이용한 문제해결. 각 건물을 노드로 보면 규칙은 간선의 방향으로 볼 수 있다.
    이를 이용하여 각 노드에 진입차수 in_degree를 만들고 조건이 충족될 때마다 in_degree를 1씩 감소시켜
    0이 되는 즉시 큐에 넣는다.(건설 시작)

"""
import sys
from collections import deque
input = sys.stdin.readline


def topological_sort(time, rule, in_degree, N, W):
    queue = deque()
    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
    ans = [0] * (N+1)

    while queue:
        node = queue.popleft()
        ans[node] += time[node]                     # 해당 건물의 건설시간을 더한다
        for next in rule[node]:
            ans[next] = max(ans[next], ans[node])   # 이전까지의 건설시간을 반영한다.
            in_degree[next] -= 1
            if in_degree[next] == 0:
                queue.append(next)
    return ans[W]


tc = int(input())
for _ in range(tc):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    rule = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)
    for _ in range(K):
        X, Y = map(int, input().split())
        in_degree[Y] += 1
        rule[X].append(Y)
    W = int(input())
    print(topological_sort(time, rule, in_degree, N, W))