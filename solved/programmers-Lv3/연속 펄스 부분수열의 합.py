"""
    연속된 부분 수열의 합이 가장 큰 것을 고르는 문제와 같다.
    구하고자 하는 연속 펄스 부분 수열은, 펄스 수열 1, -1, 1, -1... 이나 -1, 1, -1, 1...을 각 자리에 곱한 것과 같다.
    따라서 원래 수열의 첫번째부터 1, -1, 1, -1... 식으로 곱한 수열 중에, 부분 수열의 합이 가장 큰 것과
    원래 수열의 첫번째부터 -1, 1, -1, 1... 식으로 곱한 수열 중, 합이 가장 큰 부분 수열을 구해 비교하면 된다.

    즉, 부분 수열의 합이 가장 큰 것을 구하는 과정을 두번 하면된다.
"""

# dp 풀이, 현재 인덱스를 '포함한' 가장 큰값
def maxSum(arr):
    for i in range(1, len(arr)):
        arr[i] = max(arr[i], arr[i - 1] + arr[i])
    return max(arr)


def solution(sequence):
    fSequence = [ele * (-1) ** i for i, ele in enumerate(sequence)]  # 1, -1, 1, -1...
    sSequence = [-ele * (-1) ** i for i, ele in enumerate(sequence)]  # -1, 1, -1, 1...

    answer = max(maxSum(fSequence), maxSum(sSequence))

    return answer


"""
# 이거 왜 안될까
def maxSum(arr):
    maximum = max(arr)
    total = 0

    temp = []
    plus = 0
    minus = 0
    for i in arr:
        if i >= 0:
            plus += i
            if minus:
                temp.append(minus)
                minus = 0
        else:
            minus += i
            if plus:
                temp.append(plus)
                plus = 0

    if plus: 
        temp.append(plus)
    if minus:
        temp.append(minus)

    if temp[0] >= 0:
        total = temp[0]
    else:
        if len(temp) == 1:
            return maximum
        else:
            total = temp[1]
            temp = temp[1:]


    if len(temp) >= 3:
        for i in range(2, len(temp), 2):
            total = max(temp[i-2], temp[i-2] + temp[i-1] + temp[i], temp[i])

    return max(total, maximum)

    """
