# 12015 가장 긴 증가하는 부분 수열 2
"""
이 문제의 핵심은 속도에 있다. 입력이 작고 시간제한이 널널하면 그냥 풀기에 어려움이 없겠지만, 이 문제는 가속을 위해
좀 더 생각할게 많다.
맨 아래, 이전의 모든 값을 비교하는 방식으로 너무 느리다. 따라서 좀 더 빠른, dp에 큰 원소를 추가하며, 작은 원소를 replace
하는 방식으로 바꿨다.
다만, 이 문제는 입력이 너무 커서, else 안에서 for문을 돌리게 되면 시간초과가 났다.
따라서, for문을 돌려 원소가 재배치될 자리를 찾는 대신, bisect 라이브러리를 이용하여 효율적으로 재배치하는 방법으로
제한 시간내에 풀 수 있었다.
이번에도 코드를 작성하면서 느꼈지만 bisect를 이용할 때에는, 인덱스 바깥으로 범위가 벗어나지 않는지 조심해야한다.
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
    else:       # 좀 더 가속화하기 위한 아이디어론, elif로 바꿔 A[i]<dp[-1]일 경우에만, dp[bisect(~~)] = A[i]로 업데이트 해준다.
        left = bisect.bisect_left(dp, A[i])
        right = bisect.bisect_right(dp, A[i])
        if left == right:
            dp[left] = A[i]
print(len(dp))


"""
# 당연히 시간초과

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [1] * (n+1)

for i in range(2, n+1):
    for j in range(1, i):
        if A[i-1] >= A[j-1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
"""