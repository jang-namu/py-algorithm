# 1764 듣보잡
""" 두 집합합의 교집합"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hear = set(input().rstrip() for _ in range(N))
see = set(input().rstrip() for _ in range(M))

hear_and_see = hear & see
print(len(hear_and_see))
print('\n'.join(sorted(hear_and_see)))