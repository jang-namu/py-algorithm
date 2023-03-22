# 1978 소수 찾기
import sys
input = sys.stdin.readline
input()
num = list(map(int, input().split()))

prime_number = [1] * (1001)
prime_number[0] = prime_number[1] = 0
for i in range(2, 501):
    if prime_number[i]:
        for j in range(i+i, 1001, i):
            prime_number[j] = 0

print(len(list(i for i in num if prime_number[i])))