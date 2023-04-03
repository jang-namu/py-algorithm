# 4096 팰린드로미터
"""
    팰린드롬 = 회문
    순환적인 방법으로 풀이, check는 회문이 완성됐는지 확인.
    회문이 될 때 까지 recurs를 반복한다. => 193 과 같은 경우는 8을 더하면 201이 됨 -> 한 번 더 해줘야한다.

    아이디어 : 맨앞과 맨뒤부터 비교해가며, 숫자를 맞춘다.
    매번 구한 차이를 distance에 반영한다.

"""
import sys
input = sys.stdin.readline


def check(distance):
    for i in range(len(distance)//2):
        if distance[i] != distance[-i-1]:
            return False
    return True


def recurs(distance):
    ans = []
    length = len(distance)
    for i in range(length//2):
        if distance[i] < distance[-i-1] and distance[-i-1] != '0':  # 뒤에가 더 클 경우 자릿수를 하나 넘겨야 하므로 10을 더해줌.
            ans.append((10 + int(distance[i]) - int(distance[-i-1])) * 10**i)
        else:
            ans.append((int(distance[i]) - int(distance[-i-1])) * 10**i)

        distance = str(int(distance) + ans[i])  # 매 반복마다 구한 값을 바로 적용해준다.
        while len(distance) != length:  # int변환 시 앞에 0 이 사라지는 걸 다시 붙여준다.
            distance = '0' + distance

    if length % 2 == 0 and distance[length//2-1] > distance[length//2]:     # 자릿수가 짝수인 경우, 가운데 두 숫자 중 뒷자리가 크면
        ans.append(10**(length//2-1))   # 자릿수만큼 더해준다. (가운데 두 자리 중 뒷자리가 크면 1을 넘기고, 뒷자릿가 1만큼 작아진다.)
        distance = str(int(distance) + ans[-1])
        while len(distance) != length:
            distance = '0' + distance

    answer = sum(ans)
    if not check(distance):
        answer += recurs(distance)
    return answer

while True:

    distance = input().rstrip()
    if distance == '0':
        break
    print(recurs(distance))




"""
while True:
    
    distance = input().rstrip()
    if distance == '0':
        break
    length = len(distance)//2

    front = distance[:length]
    front = front[::-1]
    if length % 2:
        rear = distance[length:]
        front = int(front)
        rear = int(rear)

        if front == 0:
            front = 10 ** (length)
            print(front - rear + 10 ** (length - 1))
        else:
            print(front - rear)

    else:
        rear = distance[length+1:]
        front = int(front)
        rear = int(rear)

        if front == 0:
            front = 10 ** (length)

        print(front - rear)
"""

