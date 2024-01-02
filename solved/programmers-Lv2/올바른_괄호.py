# list에 pop 연산을 사용하면 너무 느림.
def solution(s):
    open_brackets = 0
    for ch in s:
        if ch == '(':
            open_brackets += 1
        else:
            if open_brackets == 0:
                return False
            open_brackets -= 1

    return open_brackets == 0


"""
def solution(s):
    answer = True

    brackets = []
    for ch in s:
        if ch == '(':
            brackets.append(ch)
        else:
            # 생각해보면 brackets에는 '('만이 들어간다. != '(' 비교식이 의미없음.
            if len(brackets) == 0 or brackets.pop(0) != '(':
                return False

    return True if len(brackets) == 0 else False
"""