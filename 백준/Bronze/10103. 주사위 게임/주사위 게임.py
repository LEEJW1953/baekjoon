import sys
input=sys.stdin.readline

n=int(input())
x, y = 100, 100
for i in range(n):
    a, b = map(int, input().split())
    if a<b:
        x-=b
    elif a>b:
        y-=a
print(x)
print(y)