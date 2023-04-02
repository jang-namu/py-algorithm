# 2309 일곱 난쟁이
"""
    아홉 중 일곱을 선택하는 조합이다.
    즉, 아홉 중 난쟁이가 아닌 둘을 선택하는 조합으로, 10C2 = 10 *9 / 2
    itertools의 combinations를 사용해 풀었다.
"""
import sys
from itertools import combinations
input = sys.stdin.readline

height = [int(input()) for _ in range(9)]
for com in combinations(height, 7):
    if sum(com) == 100:
        print("\n".join(map(str, sorted(com))))
        break
