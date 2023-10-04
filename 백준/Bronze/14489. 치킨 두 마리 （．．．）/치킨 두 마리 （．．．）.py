import sys
input=sys.stdin.readline

a, b = map(int, input().split())
c=int(input())
total=a+b
if total>=2*c:
    print(total-2*c)
else:
    print(total)