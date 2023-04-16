import sys
input=sys.stdin.readline

n, k = map(int, input().split())
a=k*(k+1)//2
if n<a:
    print(-1)
elif (n-a)%k==0:
    print(k-1)
else:
    print(k)