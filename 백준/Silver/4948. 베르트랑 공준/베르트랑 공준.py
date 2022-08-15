while True:
    n=int(input())
    if n==0:
        break
    arr=[0]*(2*n+3)
    arr[0]=arr[1]=1
    for i in range(2,int((2*n)**0.5)+1):
        if arr[i]==0:
            for j in range(2*i, 2*n+1, i):
                arr[j]=1
    count=0
    for i in range(n+1,2*n+1):
        if arr[i]==0:
            count+=1
    print(count)