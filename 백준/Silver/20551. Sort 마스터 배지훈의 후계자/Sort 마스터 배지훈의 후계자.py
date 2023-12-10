import sys
input=sys.stdin.readline

arr=[]
dic={}
n,m=map(int, input().split())
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]]=i
for i in range(m):
    d=int(input())
    if d in dic:
        print(dic[d])
    else:
        print(-1)