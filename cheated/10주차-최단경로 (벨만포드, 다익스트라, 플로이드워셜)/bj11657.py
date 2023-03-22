# 11657 타임머신
"""
    반례 3 3
        2 3 -1
        3 2 -1      도시 1에서 도달할 수 없는 음수 사이클, 기존 내 코드에선 is_min_cycle()함수가 무조건 True를 뱉어버림


    해결 : 출발도시가 무한대일때 계산안하도록 변경
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
distance = [1e11] * (N+1)
distance[1] = 0


def bellman_ford():

    for _ in range(N-1):
        updated = False
        for edge in edges:
            u, v, w = edge
            if distance[v] > distance[u] + w and distance[u] != 1e11:
                distance[v] = distance[u] + w
                updated = True
        if not updated:
            break
    return not is_min_cycle()


def is_min_cycle():
    for edge in edges:
        u, v, w = edge
        if distance[v] > distance[u] + w and distance[u] != 1e11:
            return True
    return False


if bellman_ford():
    ans = [i if i != 1e11 else -1 for i in distance]
    print('\n'.join(map(str, ans[2:])))
else:
    print(-1)
