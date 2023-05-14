# 1339 단어 수학
"""
    각 알파벳이 들어간 자릿수가 중요하다.
    알파벳은 A~Z까지 종류가 많으므로 dictinary로 관리
    각 자릿수마다 등장횟수가 중요 => 10 ** (등장자릿수-1)를 더해가며 저장
    ex) ABABA이면 A는 10101, B는 1010이 된다.
    ex) ABC, AAB이면 A는 210, B는 11, C는 1이 된다.
    가장 큰 부터 9, 8, 7, ... 순으로 할당받으면 된다.
"""
import sys
input = sys.stdin.readline

N = int(input())
alpha = dict()

for _ in range(N):
    word = input().rstrip()
    for i, ch in enumerate(word):
        idx = len(word) - i     # 자릿수 위치
        alpha[ch] = alpha.get(ch, 0) + 10**(idx-1)

ans = 0
for idx, v in enumerate(sorted(alpha.values(), reverse=True)):  # 가장 큰수부터 할당
    now = (9-idx) * v   # 큰수부터 9, 8, 7, ...로 할당받는다.
    ans += now
print(ans)
