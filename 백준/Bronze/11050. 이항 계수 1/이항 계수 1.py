import sys
input=sys.stdin.readline

def fac(x):
    if x==0:
        return 1
    else:
        return x*fac(x-1)

n, k=map(int,input().split())
print(fac(n)//fac(k)//fac(n-k))