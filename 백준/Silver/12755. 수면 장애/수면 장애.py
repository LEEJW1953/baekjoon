import sys
input=sys.stdin.readline

n=int(input())
t=0
for i in range(1, n+1):
    s=str(i)
    t+=len(s)
    if n<=t:
        print(s[len(s)-(t-n+1)])
        break