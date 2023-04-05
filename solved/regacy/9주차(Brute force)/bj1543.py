# 1543 문서 검색
"""
    전체범위 슬라이싱하면서 문자열 비교.
    앞에서부터 찾고, 해당하는 문자열을 찾았을 경우, 문자열 크기만큼 건너뛴다
"""
import sys
input = sys.stdin.readline

sentence = input().rstrip()
find = input().rstrip()

if len(find) > len(sentence):
    print(0)
    exit(0)


k = len(find)
pos = len(find)
count = 0
while pos <= len(sentence):     # 같을 때도 포함, bscause :pos로 슬라이싱하기 때문에, 해당범위 +1
    if find == sentence[pos-k:pos]:
        count += 1
        pos += k
        continue
    pos += 1

print(count)