# 15663 N과 M (9)
"""
    이 문제에서 중요한 것은 1. 1 7 8 9가 입력됐을 때, '1 1'이 뽑히는 경우처럼 중복 선택을 막아야 한다.
                            2. 중복선택은 막으면서, 갯수대로는 뽑을 수 있게 해야한다.
    따라서 일반적으로 set를 이용해 중복을 제거한다.
    까다로운 것은 set를 이용하면 아무리 앞에서 정렬해둔 자료들도, 순서가 뒤섞이게 된다.
    가운데 공백이 들어간 문자열로 표신된 수를 비교하는 것은 생각보다 까다롭다.
    따라서, 첫번째 풀이처럼 배열로 저장된 상태로 정렬하거나, 두번째 방법에서처럼
    출력단에서 중복을 제거한다.
"""
"""
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
permutations = list(sorted(set(permutations(numbers, M))))
for permutation in permutations:
    print(*permutation)
"""

"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(sorted(input().split(), key=int))
permutations = []
check = [False] * N


def make_permutations(N, M, seq='', m=0):
    if m == M:
        permutations.append(seq)
        return
    for i in range(N):
        if check[i]:
            continue
        new_seq = seq + numbers[i] + ' '
        check[i] = True
        make_permutations(N, M, new_seq, m+1)
        check[i] = False


make_permutations(N, M)

duplicate = set()
for permutation in permutations:
    if permutation not in duplicate:
        duplicate.add(permutation)
        print(permutation)

"""
# dictionary를 이용하는 방법, 나오는 숫자의 갯수를 세고 숫자:갯수 쌍으로 저장
# for i in string_dict.keys()로 같은 숫자는 한번밖에 for문을 돌지않으며, 갯수만큼 사용될 수 있다.
# tngus980706님의 풀이
import sys
from collections import Counter
input = sys.stdin.readline

def perm(depth=0, result=''):
    if depth == M:
        print(result)
        return
    for i in string_dict.keys():
        if string_dict[i]:
            string_dict[i] -= 1
            perm(depth+1, result+i+" ")
            string_dict[i] += 1


N, M = map(int, input().split())
integers = sorted(input().split(), key=int)
string_dict = dict(Counter(integers))

perm()
