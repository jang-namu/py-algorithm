# 13305 주유소
"""
    현재 주요소가 다음 주요소보다 비싼 경우, 딱 다음 도시까지만 갈 수 있는 양을 채우면 된다.
    문제를 해체하면, 중요한 것은 주요소의 비용이지 도로의 길이는 중요하지 않다.
    => 주요소의 비용이 저렴하면 더 저렴한 주요소가 나오기 전까지, 갈 수 있는 기름을 풀로 채운다.
        즉, 현재 주요소가 다음 주요소보다 저렴하면, 다음 마을에서도 현재 주요소의 비용으로 계산한다.
"""
import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = []
for i in range(n-1):
    if price[i] <= price[i+1]:
        price[i+1] = price[i]
    ans.append(road[i] * price[i])
print(sum(ans))