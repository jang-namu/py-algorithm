# 2143 두 배열의 합
"""
    A와 B 배열의 가능한 subset들의 합과 개수를, 각각의 딕셔너리에 키:값 형태로 저장한다.
    A를 돌아보며 B에서 T-keyA의 값을 이분탐색으로 찾는다.
    B의 keys에 T-keyA가 존재하면, ans += valA * valB로 각각의 연결될 수 있는 경우의 수를 구해 더해준다.

    처음에는 for문에서 bisect를 이용하지 않고, for문으로 B의 딕셔너리를 순회하며 keyA+keyB가 T인지 확인했다.
    그 결과 시간초과가 났는데,..

    투포인터로는 어떻게 풀 수 있을까?

"""

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

T = int(input())
n = int(input())
arrA = list(map(int, input().split()))
m = int(input())
arrB = list(map(int, input().split()))


def get_sumArr(arr, n):
    sum_arrNow = dict()
    for i in range(n):
        sumNow = 0
        for j in range(i, n):
            sumNow += arr[j]
            sum_arrNow[sumNow] = sum_arrNow.get(sumNow, 0) + 1
    return sum_arrNow


sum_arrA = get_sumArr(arrA, n)
sum_arrB = get_sumArr(arrB, m)
keysA = sorted(sum_arrA.keys())
keysB = sorted(sum_arrB.keys())
ans = 0
for keyA in keysA:
    left = bisect_left(keysB, T-keyA)
    right = bisect_right(keysB, T-keyA)
    if left != right:
        ans += sum_arrA[keyA] * sum_arrB[T-keyA]

print(ans)



"""
sumA = 0
startA = 0
endA = 0

while True:
    while sumA < T and endA < n:
        endA += 1
        sumA += arrA[endA-1]
        sum_arrA[sumA] = sum_arrA.get(sumA, 0) + 1
    startA += 1
    if startA >= n:
        break
    sumA -= arrA[startA-1]
    sum_arrA[sumA] = sum_arrA.get(sumA, 0) + 1
"""
