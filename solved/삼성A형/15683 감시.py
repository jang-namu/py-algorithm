"""
문제에서 가장 어려웠던 부분은 순열을 어떻게 만들어야 하는가 -> 반복으로는 어렵고 재귀로 작성하는 것이 자연스럽다.
또한, 이번 문제에서 많이 마주한 '경계값'에는 항상 주의하며 풀도록 하자.

여기서 더 성능을 높이는 방법은 https://www.acmicpc.net/source/79736297의 풀이를 참조하자.
매 번 calculate를 위해 N * M 행렬을 순회하는 대신 Set 자료구조를 통해 현재 recursive_depth 까지 0이 아닌 블록으로 채운
위치에 대한 정보를 관리한다.
"""

import sys
input = sys.stdin.readline

moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, M = map(int, input().split())
office = list(list(map(int, input().split())) for _ in range(N))
result = N * M


def calculate(arr):
    return sum(sum(1 if e == 0 else 0 for e in es) for es in arr)


def line(arr, d, r, c):
    while True:
        r += moves[d][0]
        c += moves[d][1]
        if not ((0 <= r < N) and (0 <= c < M)):
            return
        if arr[r][c] == 0:
            arr[r][c] = -1
        elif arr[r][c] == 6:
            return


def one(arr, d, r, c):
    line(arr, d, r, c)


def two(arr, d, r, c):
    line(arr, d, r, c)
    line(arr, (d + 2) % 4, r, c)


def three(arr, d, r, c):
    for i in range(2):
        line(arr, (d + i) % 4, r, c)


def four(arr, d, r, c):
    for i in range(3):
        line(arr, (d + i) % 4, r, c)


def five(arr, r, c):
    for i in range(4):
        line(arr, i, r, c)


def call(arr, r, c, perm, idx):
    d = perm[idx]
    num = arr[r][c]
    if num == 1:
        one(arr, d, r, c)
    elif num == 2:
        two(arr, d, r, c)
    elif num == 3:
        three(arr, d, r, c)
    elif num == 4:
        four(arr, d, r, c)
    else:
        five(arr, r, c)
    return idx + 1


def solve_one_case(perm):
    global result
    arr = [[e for e in off] for off in office]

    idx = 0
    for i in range(N):
        for j in range(M):
            if idx == len(perm):
                break
            if 1 <= arr[i][j] <= 5:
                idx = call(arr, i, j, perm, idx)
    tmp = calculate(arr)
    result = min(result, tmp)


def init(arr):
    for i in range(N):
        for j in range(M):
            if office[i][j] != 0 and office[i][j] != 6:
                arr.append(office[i][j])


def recursive_call(idx, perm):
    if idx == length:
        solve_one_case(perm)
        return

    if candidates[idx] == 2:
        for k in range(2):
            recursive_call(idx + 1, perm + [k])
    elif candidates[idx] == 5:
        recursive_call(idx + 1, perm + [0])
    else:
        for k in range(4):
            recursive_call(idx + 1, perm + [k])


candidates = []
init(candidates)
length = len(candidates)
recursive_call(0, [])
print(result)
