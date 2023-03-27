# 2798 블랙잭
"""
    거꾸로 정렬하면 더 빠르다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort(reverse=True)

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = card[i] + card[j] + card[k]
            if temp <= M:
                ans = max(ans, temp)
                break
print(ans)
"""
    처음 풀이 : 완탐 combination
"""
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()

def blackjack():
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                temp = card[i] + card[j] + card[k]
                if temp <= M:
                    ans = max(ans, temp)
                else:
                    break
    return ans

print(blackjack())
"""