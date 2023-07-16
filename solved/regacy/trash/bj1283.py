# 1283 단축키 지정

import sys
input = sys.stdin.readline
n = int(input())
words = [[input().split()] for _ in range(n)]

dic = dict()

for idx, word in enumerate(words):
    sign = False
    for wor in word:
        if wor[0] not in dic:
            dic[wor[0]] = idx
            sign = True
            break
    if sign:
        for wor in word:
            for ch in wor:
                if ch not in dic:
                    dic[ch] = idx
                    break