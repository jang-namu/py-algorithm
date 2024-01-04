"""
효율성
테스트 1 〉	통과 (34.81ms, 18.9MB)
테스트 2 〉	통과 (23.08ms, 17.5MB)
테스트 3 〉	통과 (36.14ms, 19.4MB)
테스트 4 〉	통과 (25.47ms, 18.2MB)
테스트 5 〉	통과 (18.26ms, 16.8MB)
"""


def solution(prices):
    length = len(prices)
    answer = [0] * length

    stack = []
    for i, price in enumerate(prices):
        while len(stack) and stack[-1][1] > price:
            idx, _ = stack.pop()
            answer[idx] = i - idx
        stack.append((i, price))

    for i, _ in stack:
        answer[i] = length - i - 1

    return answer


"""
효율성 
테스트 1 〉	통과 (110.82ms, 18.8MB)
테스트 2 〉	통과 (158.16ms, 17.4MB)
테스트 3 〉	통과 (253.81ms, 19.4MB)
테스트 4 〉	통과 (92.42ms, 18.1MB)
테스트 5 〉	통과 (117.15ms, 17MB)

def solution(prices):
    answer = []

    length = len(prices)    
    for i in range(length):
        for j in range(i+1, length):
            idx = j
            if prices[i] > prices[j]:
                break
        answer.append(idx - i)

    return answer
"""