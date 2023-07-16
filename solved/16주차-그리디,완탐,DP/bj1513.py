# 1513 경로 찾기
import sys
input = sys.stdin.readline

Delta = ((1, 0), (0, 1))

N, M, C = map(int, input().split())

path = [[[1] * (M+1) for _ in range(N+1)] for _ in range(C+1)] # [x][y]까지 가는 방법 가짓수, (오락실 0번, 1번, 2번... 들리고 해당 지점까지 가는 방법)

world = [[False] * (M+1) for _ in range(N+1)]   # 행 = N, 열 = M  [1][1]부터 지도 시작

for _ in range(C):
    x, y = map(int, input().split())
    world[x][y] = True  # x행 y열은 오락실

# 0번
for i in range(2, N+1):
    for j in range(2, M+1):
        if world[i][j]:
            path[0][i][j] = 0
            continue
        path[0][i][j] = path[0][i-1][j] + path[0][i][j-1]

for p in path[0][1:]:
    print(p[1:])

# 오락식 1번~C번
for visit in range(1, C+1):
    for i in range(2, N+1):
        for j in range(2, M+1):
            if world[x][y]:
                path[visit][x][y] = path[visit-1][i-1][j] + path[visit-1][i][j-1]
            else:
                path[i][j] = path[visit][i-1][j] + path[visit][i][j-1]

    print()
    print("-----------")
    print()
    for p in path[visit][1:]:
        print(p[1:])

print(' '.join(map(str, [path[i][N][M] for i in range(C+1)])))