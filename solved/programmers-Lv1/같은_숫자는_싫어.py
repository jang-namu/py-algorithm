def solution(arr):
    """
    answer = [-1]
    for ele in arr:
        if ele != answer[-1]:
            answer.append(ele)
테스트 1 〉	통과 (63.27ms, 28.1MB)
테스트 2 〉	통과 (59.21ms, 28MB)
테스트 3 〉	통과 (56.92ms, 28.1MB)
테스트 4 〉	통과 (56.86ms, 28.1MB)
    """

    answer = [i for i, j in zip(arr, arr[1:]) if i != j]
    if len(arr) >= 2:
        if len(answer) != 0:
            if arr[-1] != answer[-1]:
                answer.append(arr[-1])
        else:
            answer.append(arr[-1])
    return answer


"""
테스트 1 〉	통과 (48.16ms, 32.3MB)
테스트 2 〉	통과 (47.87ms, 32.4MB)
테스트 3 〉	통과 (51.69ms, 32.4MB)
테스트 4 〉	통과 (51.12ms, 32.3MB
"""

