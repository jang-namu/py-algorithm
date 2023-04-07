# 16028 귀찮음
"""
    XXXXXXxXXXXgreedy 문제로, 매번 남아있는 막대 중에 가장 짧은 막대를 선택해서 만든다.XXXXXXXX
    전체길이를 두고, 그 중 어떤 막대부터 만들어야하는지 선택해야 한다.XXXXXX

    ** 놓치고있던 부분 **
    사실 이 문제는 어떤 방식으로 선택하던 간에 같은 답이 나온다.
    즉, 무엇부터 선택하던 결과는 같다.
     a1, a2, a3, a4, a5일 때,
     (a1+ a2+ a3+ a4) * a5 + (a1+ a2+ a3) * a4 + (a1+ a2) * a3 + a1 * a2
     (a2+ a3+ a4+ a5) * a1 + (a3+ a4+ a5) * a2 + (a4+ a5) * a3 + a4 * a5
     는 같다.!!!
"""
import sys
input = sys.stdin.readline

n = int(input())
lengths = list(map(int, input().split()))
total = sum(lengths)
lengths.sort()

ans = 0
for i in lengths:
    total -= i
    ans += i * total
print(ans)