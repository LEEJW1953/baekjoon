import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    arr=[1, 1, 1, 2, 2]
    n=int(input())
    if 1<=n and n<=5:
        print(arr[n-1])
    else:
        for j in range(5, n):
            arr.append(arr[j-5]+arr[j-1])
        print(arr[-1])