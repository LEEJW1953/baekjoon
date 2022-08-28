import sys
input=sys.stdin.readline

def GCD(n, m):
    while(m):
        n, m=m, n%m
    return n

def LCM(n, m):
    return (n*m)//GCD(n, m)

x, y=map(int, input().split())
print(GCD(x, y))
print(LCM(x, y))