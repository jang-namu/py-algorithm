# 1697 숨바꼭질
"""
    아이디어 : deque를 이용해 브루트포스. 순차적으로 거리(횟수, 초)를 증가해가며 발견할때까지 반복한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())


def bfs(N, K):
    queue = deque()
    visited = [-1] * 100001
    if N == K:
        return 0

    queue.append(N)
    visited[N] = 0

    while queue:
        pos = queue.popleft()
        for move in (1, -1, pos):
            npos = pos + move
            if 0 <= npos < 100001 and visited[npos] == -1:
                if npos == K:
                    return visited[pos] + 1
                visited[npos] = visited[pos] + 1
                queue.append(npos)

print(bfs(N, K))



"""
# 커팅, dfs, 재귀 이용
# //2는 없으므로 n >= K일 시 n-K
# k가 2로 나눠떨어질 때만, 2로 나눈다.
def find(n, k):
    if n >= k:
        return n - k
    elif k == 1:
        return 1
    elif k % 2:
        return min (find(n, k + 1), find(n, k - 1)) +1     
    else:
        return min (k - n, find(n, k // 2) + 1)

print(find(*map(int, input().split())))
"""
