# 1182 부분수열의 합
"""
    문제설명이 매우 매우 불친절하다.
    중의해야할 점은 문제에서 말한 부분 '수열'과 '순열'을 헷갈리면 안된다는 것이다.
    '부분 수열'은 원래 집합에 순서는 유지한 채, 만들어지는 부분 집합이라고 생각하면 편하다.
    또한, 주의해야할 점은 목표 S가 0일 될 경우이다.
    S가 0이 될 경우, 시작부터 'if s== S:'에 걸린다. 따라서 if 구문에서 return하는 코드를 작성하는 경우,
    프로그램이 비정상적으로 종료된다.
"""
"""
# ex)
    if s == S:
        res += 1
    """
"""
    또한, S가 0일 경우는, 함수가 모두 끝난 후에 값을 사용하기전에 -1을 해줘야한다. 
    문제에서 크기가 양수인 부분 수열이라 했으므로 공집합은 포함되지 않는다.
    이를 함수의 return 부분에서 처리하려 할 경우, 모든 재귀호출된 반환값에 영향을 끼치므로, 비정상적인 실행의 원인이 된다."""

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()


def count_partial_permutations(s=0, idx=0):
    res = 0
    if s == S:
        res += 1
    for i in range(idx, N):
        res += count_partial_permutations(s+numbers[i], i+1)
    return res


if S:
    print(count_partial_permutations())
else:
    print(count_partial_permutations()-1)



"""
# 구글링..
# 전역변수를 사용한다. 
n, s = map(int,input().split())
n_list = list(map(int,input().split()))

cnt = 0

def dfs(num,sum):
	global cnt
	if num >= n:    # num이 n보다 크면 return
		return
	sum += n_list[num]
	if sum == s:
		cnt += 1


	dfs(num+1,sum)      # 이번 차례에 list[num]을 사용하는 경우
	dfs(num+1,sum-n_list[num])  # 사용하지 않는 경우

dfs(0,0)
print(cnt)
"""