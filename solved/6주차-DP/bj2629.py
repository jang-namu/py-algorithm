# 2629 양팔저울
"""
아이디어 : 1. 구슬끼리 더해가면서 가능한 것을 체크
        2. 1에서 구하 배열에 차를 구해가면서 체크
        직관적으로 해결하기에 간단하지만 최적화가 쉽지않은 문제
"""
import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
T = int(input())
gems = list(map(int, input().split()))

limit = sum(weights)
dp = [False] * (limit + 1)
dp[0] = True

for w in weights:
    for i in range(limit, w-1, -1):
        dp[i] |= dp[i-w]
for w in weights:
    for i in range(w, limit-w+1):
        dp[i] |= dp[i+w]

res = []
for gem in gems:
    if gem <= limit and dp[gem]:
        res.append('Y')
    else:
        res.append('N')
print(" ".join(res))



"""
# 백준 풀이 : set()을 사용하고, 추가하는 식. union은 합집합
num_weight = int(input())
weights = [0] + list(map(int, input().split()))
num_gem = int(input())
gems = list(map(int, input().split()))

dp = set()

for weight in weights:
    new = set({weight})

    for num in dp:
        new.add(abs(num-weight))
        new.add(num+weight)
    
    dp = dp.union(new)

for gem in gems:
    print("Y" if gem in dp else "N", end=" ")
print()
"""