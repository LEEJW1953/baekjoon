import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    n=int(input())
    d={}
    arr1=list(map(int, input().split()))
    for j in arr1:
        if j not in d:
            d[j]=1
    m=int(input())
    arr2=list(map(int, input().split()))
    for j in arr2:
        if j in d:
            print(1)
        else:
            print(0)