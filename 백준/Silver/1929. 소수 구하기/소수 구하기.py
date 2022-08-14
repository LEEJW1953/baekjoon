m, n=map(int, input().split())
arr=[0] *(1000001)
for i in range(n):
    if i==0 or i==1:
        arr[i]=1
    elif arr[i]==0:
        j=2*i
        while j<=n+1:
            arr[j]=1
            j+=i
    elif arr[i]==1:
        continue
for i in range(m,n+1):
    if arr[i]==0:
        print(i)