# 17208 카우버거 알바생
"""
아이디어 : 2차원 배열을 이용해 각 인덱스가 버거와 감튀 수를 의미하도록 만든다.
            ex) dp[1][2]는 버거 1개, 감튀 2개로 받을 수 있는 최대 주문 갯수.

"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
orders = list(map(int, input().split()) for _ in range(N))

# 긱 열은 버거, 행은 감튀를 의미한다.
dp = [[-1] * (M+1) for _ in range(K+1)]
dp[0][0] = 0

for burger, fries in orders:
    for i in range(M, burger-1, -1):    # burger fries 요구량이 인덱스 범위를 벗어날 경우는
        for j in range(K, fries-1, -1):     # for문 range에서 걸러진다.
            if dp[j-fries][i-burger] != -1:     # 현재 주문 하나 처리, or dp[j-fries][i-burger]가 이전에 처리한 주문일 경우에만
                dp[j][i] = max(dp[j-fries][i-burger] + 1, dp[j][i])     # 꼭 max로 비교하고 값을 업데이트 할 것.
                #dp[j][i] = dp[j - fries][i - burger] + 1   # 이와같은 문장은, 값을 더 작게만들 수 도 있음.
    print(dp)

print(max(map(max, dp)))



# 아래 대신 이렇게 쓰면된다.
"""
MAX = 0
for i in range(1, K+1):
    MAX = max(max(dp[i]), MAX)
print(MAX)
"""

"""
# 카이스트생의 풀이.. 마지막 출력 감탄..
# 0부터 cheese-c까지 돌아가며(즉, 앞에서부터 돌며, 풀었다,
# dp의 의미가 조금 다른게, 처음에 dp[cheese][potato]를 0으로 초기화 시켜서
# dp[0][0]이 오히려 모든 재료를 다 쓸 경우를 의미하고. 
# 초기 dp값을 -999로 지정해 최대 100개 주문을 다 받아도 -이므로 상관이없다.(조건문으로 가려내지 않아도 됨)
MIS = lambda: map(int,input().split())

n, cheese, potato = MIS()
dp = [[-999]*(potato+1) for i in range(cheese+1)]
dp[cheese][potato] = 0

for ORDER in range(n):
    c, p = MIS()
    for i in range(cheese+1-c):
        for j in range(potato+1-p):
            dp[i][j] = max(dp[i][j], dp[i+c][j+p]+1)
print(max(map(max,dp)))
"""