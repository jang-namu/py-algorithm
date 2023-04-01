# 2252 줄 세우기
"""
    해당 문제는 가중치도 주어지지 않고, 간선의 방향만이 주어지는 문제이다.
    즉, 직관적으로 위상정렬을 이용해 풀 수 있다.
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
in_degree = [0] * (N+1)
sequence = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    sequence[a].add(b)
    in_degree[b] += 1


def toplogical_sort():
    queue = deque()
    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
    ans = []

    while queue:
        student = queue.popleft()
        ans.append(str(student))
        for next in sequence[student]:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                queue.append(next)
    return ans


print('\n'.join(toplogical_sort()))