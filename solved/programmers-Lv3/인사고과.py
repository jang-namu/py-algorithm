def solution(scores):
    wanho = sum(scores[0])
    higher = [i for i in scores if sum(i) > wanho]

    higher.sort()

    cnt = 0
    record = -1
    dp = [i for i in higher]

    # 시간 단축
    # 처음 record가 -1 (배열의 마지막)일 때, dp[-1][0]과 dp[-2][0] (, dp[-3][0] ...)이 같다면?
    # 우리는 이를 해결하기 위해 'if dp[i][1] < dp[record][1]:' 내부에
    # dp[i][0] < dp[record][0]을 검증하기 위한if 조건을 하나 떠 써야한다.
    # 이런한 불필요한 반복을 줄이기 위해, 사전에 같은 값으로 변경해둔다.
    for i in range(len(higher) - 1, 0, -1):
        if higher[i][0] != higher[i - 1][0]:
            break
        dp[i - 1][1] = dp[i][1]

    for i in range(len(higher) - 2, -1, -1):
        if dp[i][0] == dp[i + 1][0]:
            if dp[i][1] < dp[record][1]:
                cnt += 1

            # 이 아래는 안 된다. record는 [i][0]와 [i+1][0]가 다를 경우 인센티브를 받지 못하는지 확인하기 위한 숏컷이다.
            # dp[i][1]은 [i][0]이 같은 사원 중 [i][1]이 가장 큰 값으로 유지되어야 한다.
            # dp[i][1] = max(dp[record][1], dp[i][1])

            # 정답.
            dp[i][1] = dp[i + 1][1]
            continue
        else:
            record = i + 1
            if dp[i][1] < dp[record][1]:
                cnt += 1
            dp[i][1] = max(dp[i][1], dp[record][1])

    for i in range(len(higher)):
        if scores[0][0] < dp[i][0]:
            if scores[0][1] < dp[i][1]:
                return -1
            else:
                break
        else:
            continue

    return len(higher) - cnt + 1


"""
def solution(scores):    
    wanho = sum(scores[0])
    higher = [i for i in scores if sum(i) > wanho]


    # len이 0인경우 원호가 1등
    # len이 1인경우 원호가 2등 or -1
    if len(higher) == 0:
        return 1
    elif len(higher) == 1:
        return -1 if (higher[0][0] > scores[0][0] and higher[0][1] > scores[0][1]) else 2

    higher.sort()

    cnt = -1
    record = -1
    dp = [i for i in higher]

    #시간 단축
    for i in range(len(higher)-1, 0, -1):
        if higher[i][0] != higher[i-1][0]:
            break
        dp[i-1][1] = dp[i][1]

    for i in range(len(higher) - 2, -1, -1):

        # 시간 단축.
        if dp[i][0] == dp[i+1][0]:
            if dp[i][1] < dp[record][1]:
                #if dp[i][0] < higher[record][0]:
                cnt += 1
            dp[i][1] = max(dp[record][1], dp[i][1])
            continue

        #for j in range(i + 1, len(higher)):
            #if higher[i][0] == higher[j][0]:
             #   continue 
        else:
            j = i+1
            record = j
            if dp[i][1] < dp[j][1]:
                cnt += 1
            dp[i][1] = max(dp[j][1], dp[i][1])
            #break

    for i in range(len(higher)):
        if scores[0][0] < dp[i][0]:
            if scores[0][1] < dp[i][1]:
                return -1
            else:
                break
        else:
            continue

    return len(higher) - cnt


    """
