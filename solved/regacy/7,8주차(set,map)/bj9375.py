# 9375 패션왕 신해빈
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    clothes = dict()
    for _ in range(N):
        _, category = input().split()
        clothes[category] = clothes.get(category, 0) + 1
    ans = 1
    for count in clothes.values():
        ans *= (count+1)    # 해당 부위가 두개인경우 벗든, 1 입든, 2 입든 세가지 경우의수
    print(ans-1)    # 알몸 제외