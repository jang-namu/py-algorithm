# 2468 안전 영역
"""
    contour를 따로 복사하지 않기위해 MAX부터 MIN까지 역으로 감소해가며 체크.
    rain을 dfs의 매개변수로 받아 침수되지 않는 지역은 rain으로 초기화 => 이번 iter에서만 중복제거.
    다음 iter부터는 침수되지 않음
    그 밖에, visited 배열을 따로두어 복사문제를 해결해도된다.
"""

import sys
input = sys.stdin.readline

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N = int(input())

# 등고선
contour = list(list(map(int, input().split())) for _ in range(N))
MAX = max(map(max, contour))
MIN = min(map(min, contour))


def dfs(row, column, rain):
    queue = [(row, column)]
    contour[row][column] = rain
    while queue:
        row, column = queue.pop()
        for dx, dy in move:
            nx = column + dx
            ny = row + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if contour[ny][nx] > rain:
                contour[ny][nx] = rain
                queue.append((ny, nx))

ans = set()
ans.add(1)
for rain in range(MAX, MIN-1, -1):
    tmp = 0
    for i in range(N):
        for j in range(N):
            if contour[i][j] > rain:
                dfs(i, j, rain)
                tmp += 1
    ans.add(tmp)

print(max(ans))
