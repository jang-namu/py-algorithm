# 15657 N과 M (8)

""" # 백준
from itertools import combinations_with_replacement
N, M = map(int, input().split())
nums = sorted(input().split(), key=int)     # 입력받은 배열을 int값으로 정렬해서 'string으로 저장'한다!
combs = combinations_with_replacement(nums, M)
print('\n'.join(' '.join(comb) for comb in combs))
"""

"""
    백준 풀이 : 순열을 만들기 위해 함수내부에서 전역변수를 사용하지않고, 지역변수로만 해결했다.
    전역변수를 사용하지 않는, 해결 방법을 잘 볼 것.
"""
import sys
input = sys.stdin.readline()
N, M = map(int, input().rstrip().split())
nums = list(map(str, sorted(map(int, input().rstrip().split()))))

def dfs(s, start, depth):
    if depth == M:
        print(s[:-1])
        return

    for i in range(start, N):
        s_new = s + nums[i] + ' '
        dfs(s_new, i, depth+1)


dfs('', 0, 0)


"""
    아이디어 : 재귀로 풀었다. m만큼의 길이를 만들어야하므로, 매 재귀호출마다 'm-1'과 같이 매개변수에 변화가 있어야 한다. 
        또한, 앞선 15649번 문제와는 다르게, 이 문제는 증가만 해야하므로, 이전에 추가한 요소 뒤부터 for문이 돌도록 짰다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
tmp = []


def print_none_descending_permutations(m, idx=0):
    if m == 0:
        print(" ".join(map(str, tmp)))
        return
    for i in range(idx, N):
        tmp.append(numbers[i])
        print_none_descending_permutations(m-1, i)
        tmp.pop()   # 중요! 재귀호출 후, pop으로 원소를 다시 빼준다!!! 위치가 의미하는 바를 이해하자

print_none_descending_permutations(M)
