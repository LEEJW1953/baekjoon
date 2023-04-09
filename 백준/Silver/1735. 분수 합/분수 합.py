import sys
input=sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x%y
    return int(x)

def lcm(x, y):
    return x*y//gcd(x, y)

a, b = map(int, input().split())
c, d = map(int, input().split())
g=gcd(a*d+b*c, b*d)
print((a*d+b*c)//g, b*d//g)