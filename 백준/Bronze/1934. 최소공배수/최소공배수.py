import sys
input=sys.stdin.readline

def GCD(n, m):
    while(m):
        n, m=m, n%m
    return n

def LCM(n, m):
    return (n*m)//GCD(n, m)

t=int(input())
for i in range(t):
    x, y=map(int, input().split())
    print(LCM(x, y))