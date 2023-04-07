import sys
input=sys.stdin.readline

n=int(input())
arr=sorted(list(map(int, input().split())))
ans=0
total=sum(arr)
for i in range(n-1):
    a=arr.pop(0)
    total-=a
    ans+=(a*total)
print(ans)