# 2624 동전 바꿔주기
"""
https://one10004.tistory.com/281 해설
중복을 피하기 위해 뒤부터 구한다.
중요한 것은 점화식을 세우는 것. coin의 갯수 범위 안에서 사용갯수를 늘려가며 계산하는 것이 중요하다.
"""
import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = list(list(map(int, input().split())) for _ in range(k))
coins.sort()

dp = [0] * (T + 1)
dp[0] = 1

for p, n in coins:
    for i in range(T, p-1, -1): # 뒤부터 계산 # 역 인덱싱 조심!!! 항상 마지막 항은 포함되지 않는다.!!!!!
        for cnt in range(1, n+1): # 사용하는 동전의 개수를 늘려가면 계산한다.
            if i - p * cnt >= 0:
                dp[i] += dp[i - p*cnt]  # 점화식 dp[i] += dp[i-p*cnt]
    #print(dp)
print(dp[T])

for coin, cnt in coins:
    for money in range(T, 0, -1):  # T원부터 1원까지 내려가며 진행
        for i in range(1, cnt + 1):  # 현재 동전 coin의 개수만큼 for문 진행
            if money - coin * i >= 0:  # 0원 이상인 경우
                dp[money] += dp[money - coin * i]

"""
# 백준 정답. 동전마다 금액별로 배열을 생성해서, 작은 동전부터 쓰고
# 그 다음 큰 동전을 사용할 때, 작은 동전을 이용해 만들 수 있는 경우의수를 더하는 식으로 구할수도 있다.
T=int(input())
k=int(input())
L=[[0,0]] #[금액,동전가지수]
for i in range(k):
    L.append(list(map(int,input().split())))
L.sort()
dp=[[0 for j in range(T+1)] for i in range(k+1)]
for i in range(k+1):
    dp[i][0]=1

# i번째 동전까지 사용
for i in range(1,k+1):
    #print(L[i],"금액,가용개수")
    # i번째 동전을 num번 사용
    for num in range(L[i][1]+1):
        #print(num,"번사용했을떄")
        for j in range(T+1):
            temp=j+num*L[i][0]
            if temp==0:
                continue
            if temp<T+1:
                dp[i][temp]+=dp[i-1][j]
            else:
                break

print(dp[k][T])
"""

""" # 반례
40
3
1 5
10 2
5 3

=> 답 1
=> 오답 3
"""
"""
# 틀렸다. 내 아이디어는 코인의 개수만큼 상한값을 정하는 것, 
# 문제는 중복을 어떻게 해결할지. 중복을 피하지 못 함.
import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = list(list(map(int, input().split())) for _ in range(k))
coins.sort()

dp = [0] * (T + 1)
dp[0] = 1

limit = 0 # 동전의 개수를 제한한다.
for coin in coins:
    p, n = coin
    for i in range(p, T+1):
        if p * n < i - limit:
            break
        if i-p >= 0:
            dp[i] += dp[i-p]
            if p * n == i-p: # 중복되는 것을 빼준다.
                dp[i] -= 1
    limit += p * n
    print(p, dp)

print(dp[T])
"""