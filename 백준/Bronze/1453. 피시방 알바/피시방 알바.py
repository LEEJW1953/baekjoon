n=int(input())
arr=list(map(int, input().split()))
d={}
ans=0
for i in arr:
    if i in d:
        ans+=1
    else:d[i]=1
print(ans)