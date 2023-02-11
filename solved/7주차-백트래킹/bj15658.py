# 15658 연산자 끼워넣기 (2)
"""
    15657에서는 연산자 수가 딱 맞아서, return 하지 않았지만, 이 문제는 연산자 수가 더 많을 수 있기 때문에
    return해서 종료해줘야함.
    대입이 많을 경우 max와 if문 중 if문이 훨씬 빠르다. 고쳐쓰자.
"""
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_res = -(10e9 + 1)
min_res = 10e9 + 1


def divide(num1, num2):
    if num1 >= 0:
        return num1 // num2
    else:
        return -(-num1 // num2)


def make_expression(p, m, mul, div, total=numbers[0], idx=1):
    if idx == N:
        global max_res, min_res
        max_res = max(max_res, total)
        min_res = min(min_res, total)
        return
    if p:
        make_expression(p-1, m, mul, div, total + numbers[idx], idx+1)
    if m:
        make_expression(p, m-1, mul, div, total - numbers[idx], idx+1)
    if mul:
        make_expression(p, m, mul-1, div, total * numbers[idx], idx+1)
    if div:
        make_expression(p, m, mul, div-1, divide(total, numbers[idx]), idx+1)


make_expression(operators[0], operators[1], operators[2], operators[3])
print(max_res)
print(min_res)


