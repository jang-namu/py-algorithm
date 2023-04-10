# 2870 수학숙제
import sys
input = sys.stdin.readline

n = int(input())
ans = []
for _ in range(n):
    sentence = input().rstrip()
    word = ''
    for ch in sentence:
        if ch.isdigit():
            word += ch
        elif word != '':
            ans.append(int(word))
            word = ''
    if word != '':
        ans.append(int(word))
print(*sorted(ans), sep='\n')   # sep 사용