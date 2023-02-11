# 14888 연산자 끼워넣기
"""
# 백준 답 : 재귀함수 내부에서 for문의 사용을 없애고 재귀호출로 대체하면 훨씬 빠르고, 이해하기 쉬운 코드가 된다.
# 재귀 함수 내부에서 for문을 최소화하자!
# 어차피 각 연산은 호출하므로, operate 함수를 없애고 나눗셈만 따로 처리해주면 더 빠름
def get_expression(p, m, mul, div, total=numbers[0], idx=1):
    if idx == N:
        global max_res, min_res
        min_res = min(min_res, total)
        max_res = max(max_res, total)

    if p:
        get_expression(p-1, m, mul, div, operate(0, total, numbers[idx]), idx+1)
    if m:
        get_expression(p, m-1, mul, div, operate(1, total, numbers[idx]), idx+1)
    if mul:
        get_expression(p, m, mul-1, div, operate(2, total, numbers[idx]), idx+1)
    if div:
        get_expression(p, m, mul, div-1, operate(3, total, numbers[idx]), idx+1)


get_expression(operators[0], operators[1], operators[2], operators[3])
print(max_res)
print(min_res)
"""


import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))


def operate(op_code, num1, num2):
    if op_code == 0:
        return num1 + num2
    elif op_code == 1:
        return num1 - num2
    elif op_code == 2:
        return num1 * num2
    else:
        return num1 // num2 if num1 >= 0 else -((-num1) // num2)


def get_max_expression(total=numbers[0], op_num=0, idx=1):
    maximum = -(10e9 + 1)
    if op_num == N-1:
        maximum = total
    for i in range(idx, N):
        for j in range(4):
            if operators[j] != 0:
                new_total = operate(j, total, numbers[i])
                operators[j] -= 1
                #print("depth:", idx, "연산:", j,"total:", total, new_total))
                maximum = max(maximum, get_max_expression(new_total, op_num+1, i+1))
                operators[j] += 1
    return maximum


def get_min_expression(total=numbers[0], op_num=0, idx=1):
    minimum = 10e9 + 1
    if op_num == N-1:
        minimum = total
    for i in range(idx, N):
        for j in range(4):
            if operators[j] != 0:
                new_total = operate(j, total, numbers[i])
                operators[j] -= 1
                minimum = min(minimum, get_min_expression(new_total, op_num+1, i+1))
                operators[j] += 1
    return minimum


print(get_max_expression())
print(get_min_expression())


