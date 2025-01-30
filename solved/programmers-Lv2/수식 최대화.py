# https://school.programmers.co.kr/learn/courses/30/lessons/67257
OPERATOR = ["*", "+", "-"]
PRIORITY = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]


def solution(expression):
    # 1. 파싱
    operand = []
    operator = []
    parseExpression(expression, operand, operator)
    # 2. 계산
    result = calculateMaxPrize(operand, operator)
    return result


def parseExpression(expression, operand, operator):
    tmp = ""
    for ch in expression:
        if ch in OPERATOR:
            operand.append(int(tmp))
            tmp = ""
            operator.append(ch)
        else:
            tmp += ch
    operand.append(int(tmp))
    return


def calculateMaxPrize(operand, operator):
    result = 0
    for priority in PRIORITY:
        iterResult = calculate(priority, operand, operator)
        result = max(result, abs(iterResult))
    return result


def calculate(priority, original_operand, original_operator):
    # 복사
    operand = [e for e in original_operand]
    operator = [e for e in original_operator]

    for prior in priority:
        new_operator = []
        new_operand = []
        while len(operator) > 0:
            op = operator.pop(0)
            if OPERATOR[prior] == op:
                if not operand:
                    break
                x = operand.pop(0)
                if not operand:
                    break
                y = operand.pop(0)
                tmp = calculateInfering(x, y, op)
                operand.insert(0, tmp)
            else:
                new_operator.append(op)
                new_operand.append(operand.pop(0))
        # 남은 operator와 operand 순서를 초기와 같은 상태로 만들어야한다.
        operator = new_operator
        operand = new_operand + operand
    return operand[0]


def calculateInfering(x, y, op):
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    return -1  # Error

