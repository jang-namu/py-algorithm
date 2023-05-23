# 10775 공항
"""
    유니온 "파인드"
    => 공항 기준, 각 공항은 초기 자기 자신을 가리킨다.
    => 비행기가 도착한 공항은 자신-1의 공항을 가리킨다.
    => 이미 자신-1 공항에도 비행기가 정작했다면, 이전-1 공항을 가리키는 것을 반복한다.
    => 최후에 0번째 공항(존재x)을 가리키게 되면 더 이상 비행기는 정착할 수 없어 공항은 폐쇄된다.

    ++ find함수 내부에서 airport[g]를 다음 find(airport[g])로 치환하면서 진행
       함수 실행되면서 동시에 배열의 값이 바뀜. => 외부에서 바꿀 필요 x

       또한, 밖에서 airport[temp] -= 1을 하는 것보다 airport[temp] = airport[temp-1]로
       이전 공항이 가리키는 부모를 가리키게 해야 빠른 해결이 가능하다.
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

G = int(input())
P = int(input())
airplane = list(int(input()) for _ in range(P))

airport = [*range(G + 1)]


def find(g):
    if airport[g] != g:
        airport[g] = find(airport[g])
        return airport[g]
    return g


count = 0
for g in airplane:
    temp = find(g)
    if airport[g] == 0:
        break
    airport[temp] = airport[temp - 1]
    count += 1

print(count)
