# 11023 더하기 3
#print(sum(map(int, input().split())))

# 11024 더하기 4
#for _ in range(int(input())):
 #   print(sum(map(int, input().split())))

import sys
input = sys.stdin.readline
sum = 0
n = int(input())
word = input().rstrip()
tmp = 0
for i in range(n):
    if word[i].isdigit():
       tmp = tmp * 10 + int(word[i])
    else:
        sum += tmp
        tmp = 0
print(sum + tmp)

"""
14
ab13c9d07jeden
"""
