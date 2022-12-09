import sys
input=sys.stdin.readline

n=int(input())
if n>=0:
    arr=[0, 1]
    for i in range(2, n+1):
        arr.append((arr[i-2]+arr[i-1])%1000000000)
elif n<0:
    arr=[1, 0, 1]
    for i in range(2, -n+1):
        if arr[i-1]-arr[i]<0:
            arr.append(-((-arr[i-1]+arr[i])%1000000000))
        else:
            arr.append((arr[i-1]-arr[i])%1000000000)
if n==0:
    print(0)
    print(0)
else:
    if arr[-1]>0:
        print(1)
    elif arr[-1]==0:
        print(0)
    else:
        print(-1)
    print(abs(arr[-1]))