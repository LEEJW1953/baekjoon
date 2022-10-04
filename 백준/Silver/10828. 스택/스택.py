import sys

n=int(input())
arr=[]
for _ in range(n):
    arr1=list(map(str, sys.stdin.readline().strip().split()))
    if len(arr1)==2:
        arr.append(int(arr1[1]))
    else:
        if arr1[0]=='pop':
            if len(arr)==0:
                print(-1)
            else:
                print(arr[-1])
                arr.pop()
        elif arr1[0]=='size':
            print(len(arr))
        elif arr1[0]=='empty':
            if len(arr)==0:
                print(1)
            else:
                print(0)
        elif arr1[0]=='top':
            if len(arr)==0:
                print(-1)
            else:
                print(arr[-1])