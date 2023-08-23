n, k=map(int, input().split())
arr=list(map(int, input().split()))
dp=[]
for i in range(n-k+1):
    t=0
    for j in range(k):
        t+=arr[i+j]
    dp.append(t)
print(max(dp))