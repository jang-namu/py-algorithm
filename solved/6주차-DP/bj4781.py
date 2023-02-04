# 4781 사탕 가게

"""
# 이 문제에 한해서, 소수점 두자리로 고정이므로 아래와 같이 입력을 받아도 된다.
n, m = map(conv, input().split())

# 정수문자열은 정수로, 실수문자열은 100을 곱하여 소수점아래를 버린 정수로 반환
def conv(num):
    return int(num.replace('.', ''))
"""
# 또는
"""
# truncation 하는 int() 형변환의 특징을 이용하여 다음과 같이 사용할 수도 있다.
p = int(float(p) * 100 + 0.5)
"""


"""
아이디어 : 16493, knapsack 문제. 입력 범위가 소수점으로 나온다. 돈과 관련된 변수들이 모두 소수점 둘째자리로 입력된다.
따라서, 이를 1~10000까지의 범위로 바꿔 생각하면 쉽게 풀 수 있다.
마무리 오차를 방지하기 위해 약간의 트릭이 필요하다.
"""
import sys
input = sys.stdin.readline

while 1:
    n, m = input().split()
    if n == "0":
        break
    n = int(n)
    m = int(float(m)*100 + 2e-9)    # numrical error를 해결하기 위한 트릭
    # m = int(float(m) * 100)   # 이와같이 쓸 경우 2.01이 200이 되버림 numerical error 발생.
    print(m)

    candies = []
    for _ in range(n):
        c, p = input().split()
        c = int(c)
        p = int(float(p)*100 + 2e-9)
        candies.append((c, p))

    dp = [0] * (m+1)
    for c, p in candies:
        for i in range(p, m+1):
            dp[i] = max(dp[i-p] + c, dp[i])
    print(dp)
    print(dp[-1])