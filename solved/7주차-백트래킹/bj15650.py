# 15650 N과 M (2)
"""
   아이디어 : 15649와 비슷하다. 좀 더 깔끔한 함수호출을 위해 함수내부에서만 필요한
                인자들을 default parameter를 사용해 나타냈다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
permutations = []

def make_permutations(sequence = "", length = 0, limit = 1):
    if length == M:
        permutations.append(sequence)
        return
    for num in range(limit, N+1):
        new_sequence = sequence + str(num) + " "
        make_permutations(new_sequence, length + 1, num+1)

make_permutations()
print("\n".join(permutations))


"""
from itertools import combinations
N, M = map(int, input().split())
for cb in combinations([i for i in range(1, N+1)], M):
    print(*cb)
"""