# 5618 공약수
"""
    gcd = greatest common divison
    lcm = lowest common multiple
    유클리드 알고리즘 : gcd(a,b) =  if b != 0: gcd(b, a mod b) elif b == 0: a
    x = gcd(a,b)에서 x는 a와 b의 약수이다. 따라서, a mod b의 약수이기도 하다. 모듈러 정리.
    (a+b) % x = (a%x + b%x) % x

    공약수 = 최대 공약수의 약수 집합
"""
import sys
from math import sqrt
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))


def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a


if n == 2:
    greatest = gcd(nums[0], nums[1])
else:
    greatest = gcd(nums[0], gcd(nums[1], nums[2]))

ans = set()
for i in range(1, int(sqrt(greatest)) + 1):     # 기존 greatest/2 +1 로는, 만약 greatest가 1억이라면, 5000만번 검사
    if greatest % i == 0:                       # 생각해보면 sqrt(greatest)까지만 검사하고, 몫도 추가해주면 된다.
        ans.add(i)
        ans.add(greatest // i)

if greatest > 1:
    ans.add(greatest)
print('\n'.join(map(str, sorted(ans))))