# 1620 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_poketmon = dict()
for i in range(1, N+1):
    name = input().rstrip()
    num_poketmon[str(i)] = name
    num_poketmon[name] = str(i)
ans = []
for _ in range(M):
    ans.append(num_poketmon[input().rstrip()])
print('\n'.join(ans))