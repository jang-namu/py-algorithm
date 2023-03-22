# 2805 나무 자르기
import sys
from bisect import bisect_left
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

wood = [0] * max(tree)
for ele in tree:
    wood[ele] =
#print(wood)
print(bisect_left(wood, -M))

