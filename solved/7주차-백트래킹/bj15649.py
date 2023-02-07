# 15649 N과 M (1)
"""
    아이디어 : (입력) m번의 for문 반복이 필요하다 => 재귀함수로 작성
                m의 길이가 되면 출력 => m==0 기저조건 및 재귀함수 호출마다 매개변수로 m-1 전달.
                tmp에 원소를 추가하고, 재귀함수 호출 => 하나 선택 후, 다음꺼 선택.
                재귀 함수 호출이 끝나면, 돌아와서 처음 tmp에 추가했던 원소 삭제.
                => for문 다음 iteration 시작
"""
import sys
input = sys.stdin.readline

tmp = []

def make_permutations(m):
    if m == 0:
        print(" ".join(map(str, tmp)))
        return
    for i in range(1, N+1):
        if i not in tmp:
            tmp.append(i)
            make_permutations(m-1)
            tmp.pop()


N, M = map(int, input().split())
make_permutations(M)


"""
# 일부러 사용하지 않았지만, itertools 라이브러리의 permutations 함수를 사용할 수 있다.
from itertools import permutations
N,M = map(int, input().split(' '))
print('\n'.join(list(map(' '.join, permutations(map(str, range(1, N+1)), M)))))
"""