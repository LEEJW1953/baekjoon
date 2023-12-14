import sys
input=sys.stdin.readline

p, n =map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()
ans=0
for i in range(n):
    if p>=200:
        break
    p+=arr[i]
    ans+=1
print(ans)