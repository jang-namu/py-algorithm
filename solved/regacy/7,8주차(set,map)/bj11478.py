# 11478 서로 다른 부분 문자열의 개수
"""
    문자열 파싱, set을 이용한 중복요소 제거
"""
sentence = input().strip()

length = len(sentence)
ans = list()
for i in range(length):
    for j in range(i, length):
        ans.append(sentence[i:j+1])
print(len(set(ans)))
