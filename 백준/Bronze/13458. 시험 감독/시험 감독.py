n=int(input())
arr=list(map(int, input().split()))
x, y = map(int, input().split())
ans=0
for i in range(n):
    arr[i]-=x
    ans+=1
    if arr[i]>0:
        if arr[i]%y:
            ans+=1
        ans+=arr[i]//y
print(ans)