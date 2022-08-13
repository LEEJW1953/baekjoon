t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    arr=[]
    for j in range(n):
        arr.append(j+1)
    for j in range(k):
        for l in range(1,n):
            arr[l]+=arr[l-1]
    print(arr[-1])