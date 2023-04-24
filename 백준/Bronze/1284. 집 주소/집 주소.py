import sys
input=sys.stdin.readline

while True:
    n=input().strip()
    if n=='0':
        break
    res=2+len(n)-1
    for s in n:
        if s=='1':
            res+=2
        elif s=='0':
            res+=4
        else:
            res+=3
    print(res)