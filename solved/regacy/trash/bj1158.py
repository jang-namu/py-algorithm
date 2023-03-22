# 1158 요세푸스 문제
N, K = map(int, input().split())
num = list(i for i in range(1, N+1))
res = []

while num:
    pos = K % len(num) - 1
    res.append(num[pos])
    print(num)
    if pos == -1:
        num = num[:-1]
    else:
        num = num[pos + 1:] + num[:pos]

print("<" + ", ".join(map(str, res))+">")

"""
# 백준 풀이 c
a, b = map(int,input().split())
arr = [i for i in range(1,a+1)]
result = []

idx=0   # iterator 같은 역할을 한다.
for i in range(a):
    idx += b-1
    if idx >= len(arr):
        idx = idx % len(arr)
    result.append(str(arr.pop(idx)))
    
print('<'+', '.join(result)+'>')
"""