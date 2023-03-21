# 2667 단지번호붙이기
"""
    아이디어 : 탐색을 이용해 컴포넌트 찾기
                탐색 함수 작성 시, 해당 컴포넌트에 속하는 노드의 갯수를 리턴

"""
import sys
from collections import deque
input = sys.stdin.readline

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N = int(input())
residence = [[0] * (N+2)]
residence += list([0] + list(int(x) for x in input().rstrip()) + [0] for _ in range(N))
residence += [[0] * (N+2)]


def bfs(row, column):
    ans = 0
    queue = deque()
    queue.append((row, column))
    residence[row][column] = 0  # 시작하는 점도 0으로 초기화 => 해주지 않으면 1씩 늘어나지만
                                # 입력: 1 1 과 같은 상황에선 늘어나지 않음 -> ans - 1을 리턴하면 오답의 원인이 된다.
    while queue:
        row, column = queue.popleft()
        ans += 1
        for x, y in move:
            ny = row + y
            nx = column + x
            if residence[ny][nx]:
                residence[ny][nx] = 0
                queue.append((ny, nx))
    return ans


res = []
for row in range(1, N + 1):
    for column in range(1, N + 1):
        if residence[row][column]:
            res.append(bfs(row, column))

res.sort()
print(len(res))
print('\n'.join(map(str, res)))
