import sys
input = sys.stdin.readline

T = int(input())
for seq in range(1, T+1):
    result = sum(i if i % 2 == 1 else 0 for i in map(int, input().split()))
    print(f'#{seq} {result}')