# 10451 순열 사이클
"""
    재귀를 이용한 dfs구현
    처음에는 문제를 잘못이해했는데, 단순화하면 각 자리(1, 2, ... n)은 입력되는 순열로의 간선을 갖는것과 같다.
    우리는 컴포넌트의 수를 구하면된다.
    각 자리는 한번씩 나와야하므로 최소한 하나의 싸이클이 형성되고,
    하나의 숫자는 하나의 간선만을 가지므로 모든 컴포넌트는 싸이클이다.
    따라서 싸이클의 형성은 고민하지 않아도 된다.
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def count_cycle(n):
    if visited[n]:
        return
    visited[n] = True
    count_cycle(sequence[n])


T = int(input())
for _ in range(T):
    n = int(input())
    visited = [False] * (n+1)
    count = 0
    sequence = [0] + list(map(int, input().split()))

    for i in range(1, n+1):
        if not visited[i]:
            count_cycle(i)
            count += 1
    print(count)
