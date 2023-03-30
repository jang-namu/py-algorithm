# 10815 숫자 카드
import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
check = list(map(int, input().split()))

ans = []
for i in check:
    if bisect_right(card, i) != bisect_left(card, i):
        ans.append(1)
    else:
        ans.append(0)

"""
# 파이썬의 set은 해쉬를 이용해 삽입과 삭제 연산이 O(1)시간안에 처리된다.   
import sys
input = sys.stdin.readline

N = int(input())
card = set(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

ans = []
for i in check:
    ans.append(1 if i in card else 0)
print(' '.join(map(str, ans)))
"""