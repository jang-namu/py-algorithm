# 2805 나무 자르기
import sys
from collections import Counter
n,m = map(int, sys.stdin.readline().split())
trees = Counter(map(int, sys.stdin.read().split()))

s = 1
e = 1000000000

while s<=e:
    mid = (s+e)//2
    tot = sum((h-mid)*i for h, i in trees.items() if h>mid)

    if tot >= m:
        s = mid+1
    elif tot <m:
        e = mid-1

print(e)
"""
    왜 못 풀었을까? 단순하게 생각하면 풀 수 있었을 것 같은데..
    단순히 전 범위에 대해 (0 ~ 1e9) 이진탐색을 수행하고, 모든 과정에서 나무와 톱의 높이를 비교해 얻을 수 있는 목재를 
    계산한다.
    
    
"""
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()


def bisect():
    start = 0
    end = sum(trees)

    while start <= end:
        mid = (start + end) // 2
        wood = 0
        for tree in trees:
            if tree > mid:
                wood += tree - mid
        if wood >= M:
            start = mid + 1
        elif wood < M:
            end = mid - 1
     return end


print(bisect())
"""


