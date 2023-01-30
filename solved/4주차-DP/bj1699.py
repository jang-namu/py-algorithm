# 1699 제곱수의 합
"""
아이디어 : 숫자가 n이면 최소 sqrt(n)으로 1개 항의 제곱수 합으로 표현 가능하다.
1부터 sqrt(n)까지의 제곱수를 기준으로 1부터 n까지 '최소항'을 계산한다.
min으로 계속해서 최소항을 비교해야 하므로, 처음 dp 배열은 n+1로 초기화했다.
"""
import math
n = int(input())
dp = [n+1] * (n+1)

for sqrt_num in range(1, math.floor(math.sqrt(n))+1):
    num = sqrt_num*sqrt_num
    dp[num] = 1     # 1, 4, 9, 16 ... 등은 최소항의 갯수가 1이다.
    for idx in range(num, n+1):
        if dp[idx-num]+1 < dp[idx]:
            dp[idx] = dp[idx - num] + 1
        # dp[idx] = min(dp[idx - num] + 1, dp[idx])     # if문이 더 빠르다. min을 사용하면 대입연산자까지 계산하기 때문
    print(num, dp)
print(dp)
print(dp[-1])

"""
# 제곱수의 성질을 이용한다.
sq = [i * i for i in range(1, 317)] # 100000은 316.2xx의 제곱

N = int(input())

if N in sq: print(1)    # 그 자체가 최소항이 1개인 제곱수면 1
else:
    for i in sq:
        for j in sq:
            if i + j == N: print(2); exit()     # 1이 아니면 최소항은 2다. 제곱수 둘을 더해서 N이면 2 
    while N % 4 == 0:   # 
        N //= 4
    if N % 8 == 7: print(4)     # 나머지가 7이면, ?**2+1+1+1 이므로 4 
    else: print(3)
    """
