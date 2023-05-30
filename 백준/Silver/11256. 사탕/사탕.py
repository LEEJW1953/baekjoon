import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    j, n = map(int,input().split())
    arr=[]
    for k in range(n):
        a, b = map(int, input().split())
        arr.append(a*b)
    arr.sort(reverse=True)
    count=0
    tmp=0
    while j>0:
        j-=arr[tmp]
        count+=1
        tmp+=1
    print(count)