# 15654 N과 M (5)
"""
    itertools 라이브러리 permutations(순열) 함수 사용
    출력하는 부분, 두번째 join()함수를 map()을 이용하여 map(join, per...)으로 iterator 객체 원소에 적용한다.
"""
import sys
from itertools import permutations
input = sys.stdin.readline

_, M = map(int, input().split())
numbers = list(input().split())
print("\n".join(map(" ".join, permutations(sorted(numbers, key=int), M))))