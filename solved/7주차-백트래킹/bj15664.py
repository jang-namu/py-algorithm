# 15664 N과 M (10)
"""
    아이디어 : 15663에서 idx를 조절해서 비내림차순이 되도록한다.
                duplicate_check 변수를 추가해서 정렬된 numbers로 for문을 돌 동안, 이전 iteration에서 이미 한번 for문을
                돈 수는 더 이상 돌지 않는다.(즉, 같은 수는 한번만 돌게된다.)
"""
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(sorted(map(int, input().split()), key=int))
permutations = list(sorted(set(combinations(numbers, M))))
for element in permutations:
    print(*element)

"""
N, M = map(int, input().split())
numbers = list(map(int, input().split()))


def print_permutations(permutation='', idx=0, length=0):
    if length == M:
        print(permutation)
        return
    duplicate_check = -1
    for i in range(idx, N):
        if numbers[i] != duplicate_check:
            duplicate_check = numbers[i]
            print_permutations(permutation+str(numbers[i])+' ', i+1, length+1)

print_permutations()
"""