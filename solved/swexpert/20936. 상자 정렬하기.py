# D4
# 작업 최대 1500번 -> 1개 위치 맞추는데 최대 3번 소요.
# 3 * 500 = 1500

"""
최적화 문제라면?

"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    result = []

    count = 0
    for i in range(N):
        if a[i] != i+1:
            result.append(i+1)
            count += 1
            for j in range(i+1, N):
                if a[j] == i+1:
                    result.append(j+1)
                    result.append(N+1)
                    count += 2
                    a[j], a[i] = a[i], a[j]
                    break
    print(count)
    print(*result)


