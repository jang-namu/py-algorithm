# 11724 연결 요소의 개수
"""
    아이디어 : 구현이 간단한 dfs로 구현. 컴포넌트의 수를 세기 위해 dfs함수와, dfs함수를 이용하는 count_component함수를 정의
                dfs는 일반적인 dfs와 같음. count_component 함수는 1번 노드부터 N번 노드까지 순차적으로 검사하며
                이전에 방문하지 않은 노드에 대하여 dfs함수를 실행한다.
"""
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)


def dfs(s):
    if visited[s]:
        return
    visited[s] = True
    for v in graph[s]:
        dfs(v)


def count_component():
    res = 0
    for i in range(1, N+1):
        if visited[i]:
            continue
        dfs(i)
        res += 1
    return res


print(count_component())


"""
import sys
input = sys.stdin.readline


def find(target):       # target == parent[target]이 될 때까지.
    if target != parent[target]:    # 즉, 현재 컴포넌트 내에 가장 작은 노드의 번호로 모두 업데이트하고 리턴하는 함수
        parent[target] = find(parent[target])
    return parent[target]


def union(x, y):
    find_x = find(x)
    find_y = find(y)
    if x < y:           # 정점번호가 가장 작은 노드를 기준으로 컴포넌트를 만듬.(컴포넌트 내 노드들의 parent값을 가장 작은 번호로)
        parent[find_y] = find_x
    else:
        parent[find_x] = find_y


n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    union(u, v)

s = set()
for x in range(1, n+1):     # s에는 컴포넌트 별, 가장 작은 번호의 노드가 저장.
    s.add(find(x))

print(len(s))
