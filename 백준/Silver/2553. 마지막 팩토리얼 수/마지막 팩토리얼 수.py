import sys
input=sys.stdin.readline

n=int(input())
ans=1
for i in range(1, n+1):
    ans*=i
for i in str(ans)[::-1]:
    if i!='0':
        print(i)
        exit(0)