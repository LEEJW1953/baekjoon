import sys
input=sys.stdin.readline

n=int(input())
if n%10:
    print(-1)
else:
    c1=n//300
    c2=(n-300*(n//300))//60
    c3=(n-60*(n//60))//10
    print(c1, c2, c3)