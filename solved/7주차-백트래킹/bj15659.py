# 15659 연산자 끼워넣기 (3)
# 15658 연산자 끼워넣기 (2)
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_res = -(10e9 + 1)
min_res = 10e9 + 1

def operate(op_code, num1, num2):
    if op_code == -1:

    if op_code == 1:
        return num1 - num2
    elif op_code == 2:
        return num1 * num2

def divide(num1, num2):
    if num1 >= 0:
        return num1 // num2
    else:
        return -(-num1 // num2)


def make_expression(p, m, mul, div, op_code=-1, pre=numbers[0], now=numbers[1], idx=1):
    if idx == N:
        global max_res, min_res
        total = operate(op_code, pre, now) if op_code != -1 else now
        print(total)
        max_res = max(max_res, total)
        min_res = min(min_res, total)
        return
    if p:
        make_expression(p-1, m, mul, div, 0, operate(op_code, pre, now), numbers[idx], idx+1)
    if m:
        make_expression(p, m-1, mul, div, 1, operate(op_code, pre, now), numbers[idx], idx+1)
    if op_code == -1:
        if mul:
            make_expression(p, m, mul-1, div, op_code, 0, pre * numbers[idx], idx+1)
        if div:
            make_expression(p, m, mul, div-1, op_code, 0, divide(pre, numbers[idx]), idx+1)
    else:
        if mul:
            make_expression(p, m, mul-1, div, op_code, pre, now* numbers[idx], idx+1)
        if div:
            make_expression(p, m, mul, div-1, op_code, pre, divide(now, numbers[idx]), idx+1)


make_expression(operators[0], operators[1], operators[2], operators[3])
print(max_res)
print(min_res)


