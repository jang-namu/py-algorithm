# 17219 비밀번호 찾기
import sys
input = sys.stdin.readline

N, *S = sys.stdin.read().splitlines()
N, _ = map(int, N.split())
password = dict()
for line in S[:N]:
    key, value = line.split()
    password[key] = value
ans = []
for line in S[N:]:
    ans.append(password[line])
print('\n'.join(ans))

