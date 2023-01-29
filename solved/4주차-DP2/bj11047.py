# 11047 동전 0

# 개선, 사실 이 문제는 bisect가 필요없다. N이 충분히 작다.
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))

count = 0
for value in coin[::-1]:
  if k // value > 0:
    count += k // value
    k %= value
print(count)

"""
아이디어 : 탐욕법, 가치가 큰거부터 최대한 고름. bisect 사용해서 풀었다.
"""
"""
import sys
from bisect import *
input = sys.stdin.readline

n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))

num = 0
while k != 0:
    num += k // coin[bisect_right(coin, k)-1]
    k %= coin[bisect_right(coin, k)-1]
print(num)
"""