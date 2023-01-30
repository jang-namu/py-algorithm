# 2293 동전 1
"""
아이디어 : 15989 숫자 문제와 같다.
마지막으로 value를 뽑았으면, k-value에서 value를 뽑은 경우의 수이므로, 더해주면 된다.
예를 들어 value가 1, 2, 5이고 k가 10인 경우
10을 만드는 경우의 수는 마지막으로 5를 뽑을 경우, 2를 뽑을 경우, 1을 뽑는 경우가 있다.
동전의 순서만 다른 것은 같은 경우로 보기 때문에, 각 동전을 하나씩 추가하면서 더해줘야 한다.
즉, 처음에는 가장 작은 동전으로만 만들 수 있는 경우들을 추가하고,
그 다음큰 동전, 그리고 그 다음 순으로 동전을 추가해 나간다. (중복을 포함하지 않기위해)
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))
coin.sort()
MIN = coin[0]

if MIN > k:
    print(0)
    exit(0)

dp = [0] * (k+1)
# !!!중요한 것은 초기 dp[0]을 무조건 1로 설정해야 한다.!!!
# because 어떤 값어치의 동전이던, "0 + 동전 = 동전"이기 때문
dp[0] = 1

"""
# 생각해보니 이것 또한 필요없음. 아래에 포함된다.
for i in range(MIN, k+1):
    if i % MIN == 0:
        dp[i] += 1
"""

for value in coin:
    for i in range(MIN, k+1):
        if i-value >= 0:    # 음수 인덱싱이 되는 것을 방지
            dp[i] += dp[i-value]
    #print(dp)

print(dp[k])