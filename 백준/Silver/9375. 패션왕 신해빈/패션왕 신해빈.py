import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    n=int(input())
    dict={}
    for j in range(n):
        a, b=map(str, input().split())
        dict[a]=b
    aa=set(dict.values())
    bb=list(aa)
    arr=[]
    for j in range(len(aa)):
        arr.append(len([key for key, value in dict.items() if value == bb[j]])+1)
    sum=1
    for j in range(len(arr)):
        sum*=arr[j]
    print(sum-1)