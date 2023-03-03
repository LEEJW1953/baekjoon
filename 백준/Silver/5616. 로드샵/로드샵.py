import sys
input=sys.stdin.readline

def fac(x):
    result=1
    for i in range(x):
        result*=(i+1)
    return result

n, m, r = map(int, input().split())
r-=n*m
if r>=0:
    print(fac(n+r-1)//fac(n-1)//fac(r))
else:
    print(0)