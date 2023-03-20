# 14425 문자열 집합
"""
    compare에는 같은 문자열이 입력될 수 있다. (교집합 x)
"""
"""
import os
n,_,*s=os.read(0,os.fstat(0).st_size).split()               // __contains__는 string 내장 메소드에 사용 ex) 'in'
print(sum(map(set(s[:int(n)]).__contains__,s[int(n):])))    //   포함되는지 여부 확인
"""
import os
N, _, *sentence = os.read(0,os.fstat(0).st_size).split()
N = int(N)
ans = sum(i in sentence[:N] for i in sentence[N:])
print(ans)
