# 2217 로프
"""
    주어진 로프로 최대중량을 들기 위해선, 주어진 로프 하나씩의 길이를 기준으로 최대중량을 구해본다.
    2 10 15가 주어졌을 때, 하나의 로프당 12의 무게를 주는 바보는 없다.
"""
import sys
input = sys.stdin.readline

n = int(input())
rope = list(int(input()) for _ in range(n))
rope.sort(reverse=True)

max_weight = 0
for i in range(n):
    weight = rope[i] * (i+1)
    if max_weight < weight:
        max_weight = weight
print(max_weight)

