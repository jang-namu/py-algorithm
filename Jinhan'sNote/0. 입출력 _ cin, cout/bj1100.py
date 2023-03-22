# 1100 하얀 칸
import sys
input = sys.stdin.readline

count = 0
for i in range(8):
    row = input().rstrip()
    for j in range(8):
        if abs(i - j) % 2 == 0 and row[j] == 'F':
            count += 1

print(count)


