# 2623 음악프로그램
"""
    주의 : in_degree 초기화할 때, set으로 연산 후 구하지 않으면 같은 값이 중복으로 계산된다.
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [set() for i in range(N+1)]
temp = [set() for i in range(N+1)]
for _ in range(M):
    sequence = list(map(int, input().split()))[1:]
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            edges[sequence[i]].add(sequence[j])
            temp[sequence[j]].add(sequence[i])
in_degree = [len(i) for i in temp]
#print(in_degree)
#print(edges)


def topological_sort():
    ans = []
    queue = deque()
    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        ans.append(now)
        for next in edges[now]:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                queue.append(next)
    return ans


ans = topological_sort()
if len(ans) == N:
    print('\n'.join(map(str, ans)))
else:
    print(0)