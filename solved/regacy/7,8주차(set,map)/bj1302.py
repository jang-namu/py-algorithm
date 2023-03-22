# 1302 베스트셀러
"""
    dict 자료구조 메소드
    keys = 키의 집합
    items = (키, 밸류) 쌍의 집합
    values = 밸류의 집합
"""
import sys
input = sys.stdin.readline

input()
arr = sys.stdin.read().splitlines()
book = {}
for name in arr:
    book[name] = book.get(name, 0) + 1
print(book.items())