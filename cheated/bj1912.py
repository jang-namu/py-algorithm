# 1912 연속합
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = [0] * n
dp[0] = lst[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + lst[i], lst[i])
print(max(dp))
""" 처음 문제를 풀 떄, 막연히 max(이전최대 + 현재값, 현재값)으로 떠올림
문제 : 이전최대와 현재 사이 음수가 있을 경우???
but 이전최대 + 현재값이 아닌, 이전까지 sum이라고 생각하면 문제는 쉽게풀림
매 iteration마다 현재값과 이전까지 sum+현재값 중 큰것으로 결정되기 때문
즉, dp[i-1]이 양수면 더하고 음수면 안 더함. 
마지막에 max(dp)로 출력하는 것을 꼭 확인한다. 어차피 이후 값에 음수가 섞여서 더 작아진다 해도 상관없음
"""

"""
# 내가 시도했던 답, 답은 나오지만 시간초과 매번 for문이 너무 많음.
# 점화식이 잘 정리되지 않음
def chainSum(arr: list):
    dp = [-1000] * n
    dp[0] = arr[0]
    if max(arr) < 0:
        return max(arr)
    for i in range(1, len(arr)):
        if arr[i] <= 0:
            dp[i] = dp[i-1]
            continue

        # 이전 최대값부터 현재 인덱스까지 합
        new_max = dp[i-1] + arr[i]
        for j in range(i-1, 0, -1):
            if dp[j] != dp[j-1]:
                break
            new_max += arr[j]

        # 가장 최근 음수 다음부터 현재 인덱스까지 합
        cur = 0
        for j in range(i, 0, -1):
            if arr[j] < 0:
                break
            cur += arr[j]

        dp[i] = max(new_max, cur)
    return max(dp)

n = int(input())
arr = list(map(int, input().split()))
print(chainSum(arr))
"""