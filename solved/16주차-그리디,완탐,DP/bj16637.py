# 16637 괄호 추가하기
"""
  완탐, 거의 뭐 어거지로 풀었다.
  자바의 binaryString 즉, 파이썬의 format(num,'b') 이용해서 연산자마다 0이면 괄호 x 1이면 괄호 o
"""
import sys
input = sys.stdin.readline

N = int(input())
sentence = input().rstrip()

def calc(oper, a, b):
    if oper == '+':
        return a+b
    elif oper == '-':
        return a-b
    else:
        return a*b


num = []
oper = []   # +, -, *
for i in range(N):
    if i % 2:
        oper.append(sentence[i])
    else:
        num.append(int(sentence[i]))

preCalc = []
for i in range(N//2):
    if oper[i] == '+':
        preCalc.append(num[i] + num[i+1])
    elif oper[i] == '-':
        preCalc.append(num[i] - num[i+1])
    else:
        preCalc.append(num[i] * num[i + 1])

state = 0
ans = num[0]
for i in range(N//2):
    if oper[i] == '+':
        ans += num[i+1]
    elif oper[i] == '-':
        ans -= num[i+1]
    else:
        ans *= num[i + 1]
#print(ans)

while state < 2**(N//2-1):
    binaryString = format(state, 'b')
    flag = True
    for i in range(len(binaryString)-1):
        if binaryString[i] == "1" and binaryString[i+1] == "1":
            flag = False
            break

    binaryString = "0" * (N // 2 - len(binaryString)) + binaryString

    if flag:
        i = 0
        temp = num[0]
        while i < N//2-1:
            if binaryString[i+1] == "1":
                temp = calc(oper[i], temp, preCalc[i+1])
                i += 2
            else:
                temp = calc(oper[i], temp, num[i+1])
                i += 1
        if i < N//2:
            temp = calc(oper[i], temp, num[i+1])
        #print(binaryString, temp)
        ans = max(ans, temp)

    state += 1

print(ans)