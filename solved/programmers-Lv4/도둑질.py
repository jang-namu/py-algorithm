"""
집들이 원형으로 줄지어있다.
고려해야할 점: 0번째 집과 마지막집을 동시에 선택할 수 없다.
=> 0번째 집을 포함해서 한 번 구하고, 포함하지 않는 걸로 한 번 더 구한후 최종 MAX 구함.
0번째 집을 포함하고 들어가는 경우, dp[-1]은 제외한다.
=> 만일 마지막집이 포함된 경우가 MAX라면 0번째 집을 제외하고 들어가는 경우에서 찾을 수 있다.
반대로, 1번째 집이 들어가야 MAX인 경우는 0번째을 포함하는 예제에서 얻을 수 있다.
"""


def solution(money):
    length = len(money)

    dp1 = [0] * length
    for i, m in enumerate(money):  # 0번째 집 포함
        if i >= 3:
            dp1[i] = max(dp1[i - 2], dp1[i - 3]) + m
        elif i >= 2:
            dp1[i] = dp1[i - 2] + m
        else:
            dp1[i] = m
    dp1.pop(length - 1)

    dp2 = [0] * length
    for i, m in enumerate(money[1:]):  # 0번째 집 제외
        if i >= 3:
            dp2[i] = max(dp2[i - 2], dp2[i - 3]) + m
        elif i >= 2:
            dp2[i] = dp2[i - 2] + m
        else:
            dp2[i] = m
    dp2.pop(length - 1)

    return max(max(dp1), max(dp2))