# 12738 가장 긴 증가하는 부분 수열 3
"""
    12015 문제를 가져다써도 문제가 없다. 음수, 양수 관계없이 값의 크기를 비교해서 dp에 넣는 방식이기 때문이다.
"""
import sys
import bisect
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [A[0]]

for i in range(1, n):
    if A[i] > dp[-1]:
        dp.append(A[i])
    elif A[i] < dp[-1]:     # A[i] == dp[-1]인 경우를 제외시킨다.
        dp[bisect.bisect_left(dp, A[i])] = A[i]
        # bisect_right - 1을 쓰게되면 값이 dp에 존재하지 않을 시에도 -1이한 장소에 업데이트 되버린다.
print(len(dp))

"""
# 입출력 속도를 줄이기 위해, 초기 arr에 inf를 넣을 수도 있다.
import os, io
from bisect import bisect_left
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

input()
arr = [float('inf')]

for x in map(int, input().split()):
	if arr[-1] < x: arr.append(x)
	else: arr[bisect_left(arr, x)] = x

print(len(arr))
"""