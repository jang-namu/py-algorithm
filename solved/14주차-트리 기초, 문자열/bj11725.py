# 11725 트리의 부모 찾기
"""
    작성. 2023.05.02
    트리는 그래프의 일종. 입력을 그래프에서 두 정점 간 edge로 본다.
    dfs에서 현재 노드와 부모노드를 같이 stack에 추가한다.
    함수 내부에서 인덱스의 부모노드를 저장하는 answer 배열을 만들어 반환한다.
"""
import sys
input = sys.stdin.readline


def dfs():
    visited = [False] * (n + 1)
    answer = [0] * (n + 1)
    stack = [(1, 0)]  # 루트는 1, 루트의 부모는 없다.
    visited[1] = True

    while stack:
        node, parent = stack.pop()
        answer[node] = parent
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            stack.append((child, node))

    return answer


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
   start, end = map(int, input().split())
   graph[start].append(end)
   graph[end].append(start)

answer = dfs()
print("\n".join(map(str, answer[2:])))
