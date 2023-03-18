# 2609 최대공약수와 최소공배수
num = sorted(map(int, input().split()))
ans = []
for i in range(num[0], 0, -1):
    if num[0] % i == 0 and num[1] % i == 0:
        ans.append(i)
        break

for i in range(num[0] * (num[1]//num[0]), num[1] * num[0]+1, num[0]):
    if i % num[0] == 0 and i % num[1] == 0:
        ans.append(i)
        break
print('\n'.join(map(str, ans)))
