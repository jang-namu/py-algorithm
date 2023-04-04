# 1120 문자열
"""
    완전탐색, 문자열 길이가 굉자히 짧읍 => 50
    최대 49 * 50

    문자열의 길이가 길어지면 비트마스킹을 생각해볼 수 있다.
"""
import sys
input = sys.stdin.readline

a, b = input().split()
count = 0
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    print(count)
else:
    diff = len(b) - len(a)
    temp1 = 1e10
    for di in range(diff+1):
        temp = 0
        for i in range(len(a)):
            if a[i] != b[i+di]:
                temp += 1
        temp1 = min(temp1, temp)
    print(temp1)

