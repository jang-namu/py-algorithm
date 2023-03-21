# 2745 진법 변환
"""
# int() 함수는 진법변환을 수행한다. default = 10진법.ㄴ
a, b = input().split()
print(int(a, int(b)))
"""

"""
    ord() : char를 int(ascii)로 변환, chr() : int(ascii)를 char로 변환
"""
import sys
input = sys.stdin.readline

nums, rule = input().split()
rule = int(rule)

ans = 0
for i, ele in enumerate(nums[::-1]):
    #print(ord(ele),rule, i)
    if ele.isdigit():   # 각 자리 숫자가 A(10)보다 작을 때,
        ans += int(ele) * (rule**i)
    else:   # A(10) 이상일 때, ascii 코드로 'A' == 65
        ans += (ord(ele) - 55) * (rule**i)
print(ans)