# 1644 소수의 연속합
"""
    소수 배열을 구해야한다. => 에라토스테네스의 체
    소수 배열을 구성한 후, 연속합을 구하기위해 투포인터 사용
"""
import sys
input = sys.stdin.readline

n = int(input())

nums = [*range(n+1)]
for i in range(2, int(n**(0.5))+1):
    if nums[i] == 0:
        continue
    for j in range(2*nums[i], n+1, nums[i]):
        nums[j] = 0

num = [i for i in nums if i != 0]
end = 0
m = 0
count = 0
length = len(num)
for start in range(length):
    while m < n and end < length:
        end += 1
        m += num[end-1]
    if m == n:
        count += 1
    m -= num[start]
print(count)