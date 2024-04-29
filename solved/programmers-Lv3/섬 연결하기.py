# 42861 Union Find
from heapq import heappush, heappop

def find_parent(a, info):
    while a != info[a]:
        a = info[a]
        info[a] = info[info[a]]
    return a


def union(a, b, info, size):
    parent = find_parent(a, info)
    info[b] = parent
    size[parent] += size[b]


def join(a, b, info, size):
    a = find_parent(a, info)
    b = find_parent(b, info)
    if size[a] < size[b]:
        tmp = a
        a = b
        b = tmp
    union(a, b, info, size)


def check(a, b, info):
    return find_parent(a, info) == find_parent(b, info)


# 현재 섬, 이어진 섬 기록, 건설비용 지도
def dfs(n, vectors):
    info = list(range(n))
    size = [1] * n

    result = 0
    while n > 1:
        cost, s1, s2 = heappop(vectors)
        if not check(s1, s2, info):
            join(s1, s2, info, size)
            result += cost
            n -= 1
    return result


def solution(n, costs):
    heap = []
    for s1, s2, cost in costs:
        heappush(heap, (cost, s1, s2))

    answer = dfs(n, heap)
    return answer