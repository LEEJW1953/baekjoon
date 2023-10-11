arr=list(map(int,input().split()))
arr1=[]
ans=1
for i in arr:
    if i%2:
        arr1.append(i)
if arr1:
    for i in arr1:
        ans*=i
else:
    for i in arr:
        ans*=i
print(ans)