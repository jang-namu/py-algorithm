# 1007 벡터 매칭
"""
    완전탐색, Combination(20, 10) = 18만 정도밖에 안된다.
    '벡터의 합'의 길이의 최소값,
    벡터의 합은 N = 20일 때, 10개는 그대로 더하고 나머지 10개는 -1을 곱해서 더한 후,
    최종 벡터의 길이를 구한다. sqrt(x^2 + y^2)

    요건은, -1을 곱할 10개를 어떻게 다 선택해보냐 => 재귀함수 이용.
    n = 나머지 중에서 -1을 곱할 갯수.
    depth = 재귀 호출의 깊이와 동시에 현재 보고있는 원소의 인덱스
    x, y = 재귀호출에서 누적 합 저장
"""

import math
import sys
input = sys.stdin.readline


def brforce(n, depth, x, y):
    res = 10e9
    if depth + n > maximum:
        return 10e9
    if n == 0:
        for i in range(depth, maximum):
            x += arr[i][0]
            y += arr[i][1]
        return math.sqrt(x**2 + y**2)
    res = min(res, brforce(n-1, depth+1, x-arr[depth][0], y-arr[depth][1]),
                    brforce(n, depth+1, x+arr[depth][0], y+arr[depth][1]))
    return res


for _ in range(int(input())):
    maximum = int(input())
    arr = []
    for _ in range(maximum):
        x, y = map(int, input().split())
        arr.append((x, y))

    ans = brforce(maximum/2, 0, 0, 0)
    print(ans)