# 10491 Quite a problem
"""
    문자열 매칭에 기본. lower case로 변경 후 찾는다.
"""

import sys

paragraph = sys.stdin.readlines()
for sentence in paragraph:
    if "problem" in sentence.lower():
        print("yes")
    else:
        print("no")
