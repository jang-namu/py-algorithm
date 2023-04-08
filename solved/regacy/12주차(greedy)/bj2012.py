# 2012 등수 매기기
"""
    abs(최종 등수 - 예상 등수)의 합을 최소화 하기 위해선,
    최종 등수는 예상 등수 보다 높을(숫자로 작은)수 없다.
    예상등수에서 멀리 떨어지면 불만은 그만큼 커지므로, 예상등수 순으로 나열하면 모두 최선의 경우가 나온다.

"""
import sys
input = sys.stdin.readline

n = int(input())
predict = list(int(input()) for _ in range(n))
predict.sort()

disapoint = 0
for i in range(1, n+1):
    disapoint += abs(predict[i-1] - i)
print(disapoint)