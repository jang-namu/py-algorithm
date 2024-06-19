"""
slope -> 경사로를 놓은 장소 = True로 표시

solve는 처음에는 행으로, 두번째는 열로 하나의 line(길)을 만들어 checkRoad() 함수를 호출

앞에서부터 탐색을 해나가는 경우, 크게 세 가지로 나눌 수 있다.
1. 현재와 다음 높이가 같음 -> 다음으로 이동 (별 다른 처리가 필요하지 않음)
2. 현재가 더 높음 -> 앞을 살펴보며 L칸 만큼 경사로를 둔다.
3. 현재가 더 낮음 -> (왔던 길을 되돌아보며) 뒤를 살펴보며 L칸 만큼 경사로를 둘 수 있었는지 확인
"""
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]


def checkFront(arr, i):
    return abs(arr[i] - arr[i+1]) == 1


def checkFrontL(arr, slope, i):
    if i + L >= N:
        return -1

    criteria = i+1
    for j in range(i+2, i+L+1):
        if arr[criteria] != arr[j]:
            return -1
    for j in range(i+1, i+L+1):
        slope[j] = True
    return i + L


def checkBackL(arr, slope, i):
    if i-L+1 < 0:
        return -1

    criteria = i
    if slope[i]:
        return -1

    for j in range(i-L+1, i):
        if (arr[criteria] != arr[j]) or slope[j]:
            return -1
    for j in range(i-L+1, i+1):
        slope[j] = True
    return i + 1


def checkRoad(arr):
    slope = [False] * N
    i = 0
    while i < N-1:
        if arr[i] == arr[i+1]:
            i += 1
            continue

        if not checkFront(arr, i):
            return False

        if arr[i] > arr[i + 1]:
            i = checkFrontL(arr, slope, i)
        elif arr[i] < arr[i+1]:
            i = checkBackL(arr, slope, i)
        if i == -1:
            return False
    return True


def solve(matrix):
    result = 0
    for line in matrix: # 행
        if checkRoad(line):
            result += 1
    for i in range(N): # 열
        line = []
        for j in range(N):
            line.append(matrix[j][i])
        if checkRoad(line):
            result += 1
    return result


print(solve(map))