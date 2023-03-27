# 1920 수 찾기
import sys
input = sys.stdin.readline

_ = int(input())
num = set(map(int, input().split()))
_ = int(input())
ans = []
for i in map(int, input().split()):
    if i in num:
        print(1)
    else:
        print(0)
