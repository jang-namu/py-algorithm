# 10816 숫자 카드 2
import sys
from collections import Counter
input = sys.stdin.readline

_ = int(input())
counter = Counter(map(int, input().split()))
_ = int(input())
ans = []
for i in map(int, input().split()):
    ans.append(counter.get(i, 0))
print(' '.join(map(str, ans)))

"""
card = dict()
for i in map(int, input().split()):
    card[i] = card.get(i, 0) + 1
M = int(input())
ans = []
for i in map(int, input().split()):
    ans.append(card.get(i, 0))
print(' '.join(map(str, ans)))
"""
