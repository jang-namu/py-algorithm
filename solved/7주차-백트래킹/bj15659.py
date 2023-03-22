# 15659 연산자 끼워넣기 (3)
"""
    14888을 확장시켜 풀었다.
    문제의 관건은 연산자 우선순위를 어떻게 표현할 것인가.
    곱하기와 나누기는 최상위 우선순위 => 즉, 바로 계산해도 된다.
    반면, '+' '-'는 우선순위가 낮으므로 뒤에 오는 연산자를 확인하고 계산해야한다.
    op_code : '+' = 1, '-' = 2 ('0'은 초기 함수호출 상태를 의미한다.)
"""
import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_res = -(10e9 + 1)
min_res = 10e9 + 1


def operate(op_code, num1, num2):
    if op_code == 0:
        return num1
    if op_code == 1:
        return num1 + num2
    if op_code == 2:
        return num1 - num2


def divide(num1, num2):
    if num2 == 0:  # error : division by zero
        return
    if num1 >= 0:
        return num1 // num2
    else:
        return -(-num1 // num2)


def make_expression(p, m, mul, div, op_code=0, pre=numbers[0], now=numbers[1], idx=1):
    if idx == N:
        global max_res, min_res
        # 마지막 계산, 현재 argument는 마지막 연산자(op_code)와 연산되지않은 pre, now
        total = operate(op_code, pre, now)
        if max_res < total:
            max_res = total
        if min_res > total:
            min_res = total
        return
    """
        각각 '+', '-'를 뜻하는 'p', 'm'는 우선순위가 낮기 때문에, 현재 iter에서 연산하지 않고 다음 순환 호출에 argument로
        보낸다. '+' = 1, '-' = 2 
        이전 iter에서 보내온 op_code와 두 항을 계산한다.
    """
    if p:
        make_expression(p - 1, m, mul, div, 1, operate(op_code, pre, now), numbers[idx], idx + 1)
    if m:
        make_expression(p, m - 1, mul, div, 2, operate(op_code, pre, now), numbers[idx], idx + 1)

    """
        'op_code = 0'은 이전에 처음 호출된 상태이거나 이전에 +나 -연산이 나오지 않았다는 것을 의미한다.
        전자의 경우, 처음 두 항을 계산하여 넘겨야 하는데, pre로 넘겨야 다음 iteration에서 '+', '-' 연산이 이뤄질떼
        operate(0, pre, now) = pre로 다시 값을 되돌려 받을 수 있다.

        op_code가 0이 아닌 경우는 +나 -연산이므로 op_code와 pre값을 그대로 보내고, now와 새로운 값 numbers[idx]를 연산해서
        다음 iter로 보낸다.
    """
    if op_code == 0:
        if mul:
            make_expression(p, m, mul - 1, div, 0, pre * numbers[idx], 0, idx + 1)
        if div:
            make_expression(p, m, mul, div - 1, 0, divide(pre, numbers[idx]), 0, idx + 1)
    else:
        if mul:
            make_expression(p, m, mul - 1, div, op_code, pre, now * numbers[idx], idx + 1)
        if div:
            make_expression(p, m, mul, div - 1, op_code, pre, divide(now, numbers[idx]), idx + 1)


make_expression(operators[0], operators[1], operators[2], operators[3])
print(max_res)
print(min_res)



"""
# 백준 답 : 기본적인 아이디어는, 윈프 때 계산기 문제해결 했던 방법과 같다. *, //는 먼저 계산해서 값을 넣고,
# +는 그대로, - 는 -value로 's'라는 리스트에 저장한 후, 마지막에 sum(s)로 연산. 
# 이를 위해 앞에서부터 숫자를 빼기에 자연스러운 deque을 이용한다.
from collections import deque
max_res, min_res = int(-1e9), int(1e9)

def cal(s, A, plus, minus, mul, div):
    if not A:
        global max_res, min_res
        res_part = sum(s)
        max_res = max(max_res, res_part)
        min_res = min(min_res, res_part)
        return
    else:
        if plus > 0:
            num = A.popleft()
            s.append(num)
            cal(s, A, plus - 1, minus, mul, div)
            s.pop()
            A.appendleft(num)
        if minus > 0:
            num = A.popleft()
            s.append(-num)
            cal(s, A, plus, minus - 1, mul, div)
            s.pop()
            A.appendleft(num)
        if mul > 0:
            if s:
                num = A.popleft()
                k = s.pop()
                s.append(num * k)
                cal(s, A, plus, minus, mul - 1, div)
                s.pop()
                s.append(k)     // 연산이 시작하기 전에, s는 비어있으면 안 됨. (이전 항이 있어야함)
                A.appendleft(num)
        if div > 0:
            if s:
                num = A.popleft()
                k = s.pop()
                if k >= 0:
                    s.append(k // num)
                else:
                    s.append(-(abs(k) // num))
                cal(s, A, plus, minus, mul, div - 1)
                s.pop()
                s.append(k)
                A.appendleft(num)

N = int(input())
A = deque(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
s = []
s.append(A.popleft())
cal(s, A, plus, minus, mul, div)

print(max_res)
print(min_res)
"""

