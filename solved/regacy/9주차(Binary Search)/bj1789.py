# 1789 수들의 합
import math
S = int(input())
print(int((-1 + math.sqrt(1+8*S))/2))   # 근의공식
"""
from bisect import bisect_right
import math
S = int(input())

dp = [*range(1, int(math.sqrt(2*S))+1)]
for i in range(1, len(dp)):
    dp[i] += dp[i-1]

print(bisect_right(dp, S))

"""