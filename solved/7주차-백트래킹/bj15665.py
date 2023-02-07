# 15665 N과 M (11)
"""
# 백준 답, itertools의 product 함수를 이용하면 중복 순열을 구할 수 있다. 'repeat = 구할 순열 길이'
import sys
from itertools import product

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(set(map(int, input().split())))

arr.sort()

print('\n'.join(map(' '.join, product(map(str, arr), repeat=M))))
"""


"""
    아이디어 : 중복 선택이 가능하므로, 같은 수열이 출력되는 것을 방지하기 위해,
                입력 부분에서 set으로 중복제거 후 리스트로 변환했다.
                함수에서 의미상 'm == M'에서 출력하고 return하는게 맞는 것 같아 수정하였다.
                string형의 sequence를 매개변수로 두어 'tmp = []' 전역변수 대신 매개변수로써 사용하였다.
                !! 재귀함수 내부에서 sequence의 값은 수정하지 않는다. !!
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
numbers = list(set(map(int, input().rstrip().split())))
new_N = len(numbers)
numbers.sort()
permutations = []


def append_permutations(sequence='', m=0):
    if m == M:
        permutations.append(sequence)
        return
    for num in numbers:
        new_sequence = sequence + str(num) + ' '
        append_permutations(new_sequence, m+1)


append_permutations()
print("\n".join(permutations))
