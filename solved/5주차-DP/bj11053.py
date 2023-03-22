# 11053 가장 긴 증가하는 부분 수열
"""
아이디어 : dp = max(이전최대값 + 1, 현재값), dp는 현재 자리 숫자를 '포함한' 최대길이 부분수열
"""
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

dp = [1] * (n) # 각 자리는 자기 자신만으로 최소 1의 길이를 가짐.

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j] + 1
            # dp[i] = max(dp[j] + 1, dp[i])
print(dp)
print(max(dp))

"""
# 백준, 초기 nums[0], 1 부터 n-1번째 요소까지 돌아가며 for문수행ㅇ
# stack에는 가장 긴 부분수열만이 남게된다. but, stack의 길이가 가장 긴 부분수열의 길이와 같은 것이지
# stack자체가 가장 긴 부분수열은 아니다. 즉, 길이만을 신경쓰고 저장한다.
def sol():
    N = int(input())
    nums = [*map(int,input().split())]
    stack = [nums[0]]

    for i in nums[1:]:
        if stack[-1] < i:   # 현재 stack 마지막원소보다 크면 추가
            stack.append(i)
        else:
            for j,v in enumerate(stack):    # enumerate는 인덱스와 원소를 반환
                if i <= v:      # stack에서 i의 위치를 찾아 바꿈
                    stack[j] = i
                    break
    return len(stack)

print(sol())
"""