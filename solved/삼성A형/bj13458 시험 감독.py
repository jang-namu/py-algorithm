import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())


result = N
for p in arr:
    if p > B:
        result += ((p - B) + C - 1) // C

print(result)