# 11054 가장 긴 바이토닉 부분 수열
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

left = [0]
right = [0]

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:     # left는 자기 자신을 기준으로, 왼쪽에 최대 길이 증가 수열 (자기 자신 미포함)
            left[i] = max(left[j] + 1, left[i])

for i in range(-1, -n-1, -1):
    for j in range(-1, i, -1):
        if A[j] < A[i]:     # right는 자기 자신을 기준으로, 오른쪽에 최대 길이 감소 수열 (자기 자신 미포함)
            right[i] = max(right[j] + 1, right[i])

res = list(l + r for l, r in zip(left, right))
print(max(res) + 1)

"""
아이디어 : 바이토닉 수열은, 자신의 왼쪽 오른쪽이 가면 갈수록 작아져야한다.
바이토닉 부분수열의 길이를 세기 위해서는, 현재 위치에서 왼쪽과 오른쪽에 내가 가장 큰, 증가, 감소 수열의 길이르 각각 구한다.
그 후 구해진 증가, 감소 수열의 길이를 더한후, 자기 자신도 포함한다(길이 +1)

"""
"""
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

left = [0] * n
right = [0] * n

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:     # left는 자기 자신을 기준으로, 왼쪽에 최대 길이 증가 수열 (자기 자신 미포함)
            left[i] = max(left[j] + 1, left[i])

for i in range(-1, -n-1, -1):
    for j in range(-1, i, -1):
        if A[j] < A[i]:     # right는 자기 자신을 기준으로, 오른쪽에 최대 길이 감소 수열 (자기 자신 미포함)
            right[i] = max(right[j] + 1, right[i])

res = list(l + r for l, r in zip(left, right))
#print(right)
#print(left)
print(max(res) + 1)
"""