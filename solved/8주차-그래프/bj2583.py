# 2583 영역 구하기
"""
    아이디어 : 이 문제에서 분리된 영역은 컴포넌트, 영역의 넓이는 컴포넌트의 크기를 의미한다.
                직사각형 넓이를 배열로 바꾸면서 길이가 하나 줄어든다.
                또한, a, b, x, y로 입력받을때, y축을 기준으로 배열을 탐색해야함에 주의하자.
"""
import sys
from collections import deque
input = sys.stdin.readline

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
M, N, K = map(int, input().split())

paper = list([1] * N for _ in range(M))
for _ in range(K):
    a, b, x, y = map(int, input().split())
    for i in range(b, y):
        for j in range(a, x):
            paper[i][j] = 0


def bfs(row, column):
    res = 0
    queue = deque()
    queue.append((row, column))
    paper[row][column] = 0

    while queue:
        row, column = queue.popleft()
        res += 1
        for dx, dy in move:
            nx = column + dx
            ny = row + dy
            if 0 <= nx < N and 0 <= ny < M:
                if paper[ny][nx]:
                    paper[ny][nx] = 0
                    queue.append((ny, nx))
    return res


ans = []
for i in range(M):
    for j in range(N):
        if paper[i][j]:
            ans.append(bfs(i, j))
ans.sort()
print(len(ans))
print(" ".join(map(str, ans)))