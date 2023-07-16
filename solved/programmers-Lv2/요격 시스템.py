# **중요!**
"""
    아이디어: 빨리 끝나는 순으로 정렬 한다.
    미사일이 끝나기 전 반드시 요격해야하기 때문에, 앞에서부터 보면된다.
"""


def solution(targets):
    answer = 0

    targets.sort(key=lambda x: (x[1], x[0]))  # 빨리 끝나는 순, 이후 빨리 시작하는 순.
    targets.append((10e11, 10e11))  # 아무거나 1억보다 큰 수. (for문에서 out of range 피하기위함)

    max_x = targets[0][1]  # 첫번째 끝나는 시간
    for i, target in enumerate(targets[:-1]):
        if max_x <= targets[i + 1][0]:  # 다음 미사일 시작시간이 현재 종료시간 이후일때
            answer += 1  # 이전까지의 미사일은 여기서 모두 처리해야함.
            max_x = targets[i + 1][1]  # 다음 미사일 끝나느 시간으로 max_x 다시 초기화

            """
        #else:                           # 이전일 때,
            #max_x = min(max_x, target[1])   # 현재 미사일, 다음 미사일 비교해서 더 빨리 끝난는 걸로 max_x 초기화 

            알고보니! 필요없다! 
            생각해보면 포함되는 경우는 1-5, 2-5와 같은 방식으로 나올 수는 있어도. 
            1-5, 2-3과 같이 뒤에 미사일이 더 빨리 끝날수가 없다 (빨리 끝나는 순으로 정렬했으니까!)
               """

    return answer