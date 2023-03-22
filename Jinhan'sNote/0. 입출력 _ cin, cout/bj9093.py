# 9093 단어 뒤집기
""" 람다를 이용해 문자열에 map 슬라이싱을 쓸 수 있다."""

import sys
input = sys.stdin.readline
n = int(input())
res = []
for _ in range(n):
    res.append(' '.join(map(lambda x: x[::-1], input().split())))
print('\n'.join(res))


