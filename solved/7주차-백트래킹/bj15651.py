# 15651 N과 M (3)

# itertools의 product 함수는 데카르트 곱을 구한다.
# 즉, 원소를 중복해서 뽑는 순열을 만드는데 사용 가능하다. 'repeat = 순열 길이'
import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(str(i) for i in range(1, N+1))
print("\n".join(map(" ".join, product(numbers, repeat=M))))

"""
    배열이 아닌 문자열로 저장했을 때에 장점은, join 한번 만으로 출력포맷에 맞춰 출력할 수 있다는 것이다.
"""
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
permutations = []

def make_repeat_permutations(sequence = "", length = 0):
    if length == M:
        permutations.append(sequence)
        return
    for num in range(1, N+1):
        new_sequence = sequence + str(num) + " "
        make_repeat_permutations(new_sequence, length + 1)


make_repeat_permutations()
print("\n".join(permutations))

"""